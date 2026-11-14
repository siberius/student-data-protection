#!/usr/bin/env python3
"""Deterministic k-Anonymity & l-Diversity Gate for School Data Exports & Non-Local AI (v1.2)

Checks:
1. Direct identifier presence (blocklist).
2. Distinct-person k-anonymity (default k >= 5) across quasi-identifiers.
3. Sensitive attribute l-diversity (default l >= 2) per equivalence class.
"""

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

DIRECT_ID_BLOCKLIST = {
    "name", "jmeno", "prijmeni", "fullname", "first_name", "last_name",
    "email", "e-mail", "phone", "telefon", "rodne_cislo", "rc", "ssn", "dni",
    "ip", "ip_address", "device_id", "session_token"
}


def evaluate_dataset(records, person_id_col, quasi_cols, sensitive_cols, k_threshold=5, l_threshold=2):
    if not records:
        return {"passed": False, "error": "Empty dataset."}

    headers = set(records[0].keys())
    exposed_direct = {h for h in headers if h.lower() in DIRECT_ID_BLOCKLIST and h != person_id_col}

    groups = defaultdict(list)
    for idx, row in enumerate(records):
        q_key = tuple((col, str(row.get(col, "")).strip()) for col in quasi_cols)
        groups[q_key].append((idx, row))

    violations_k = []
    violations_l = []
    min_k = float("inf")
    min_l = float("inf")

    for q_key, items in groups.items():
        if person_id_col and person_id_col in headers:
            distinct_persons = len({str(r.get(person_id_col, "")) for _, r in items})
        else:
            distinct_persons = len(items)

        min_k = min(min_k, distinct_persons)

        if distinct_persons < k_threshold:
            violations_k.append({
                "quasi_identifiers": dict(q_key),
                "distinct_persons_k": distinct_persons,
                "row_count": len(items),
                "action_required": "Generalize quasi-identifiers or suppress these rows."
            })

        for s_col in sensitive_cols:
            distinct_sensitive = len({
                str(r.get(s_col, "")).strip()
                for _, r in items
                if str(r.get(s_col, "")).strip() != ""
            })
            min_l = min(min_l, distinct_sensitive)
            if distinct_sensitive < l_threshold:
                violations_l.append({
                    "quasi_identifiers": dict(q_key),
                    "sensitive_column": s_col,
                    "distinct_values_l": distinct_sensitive,
                    "action_required": "Homogeneity risk (inference). Merge equivalence class or suppress."
                })

    passed = (len(exposed_direct) == 0) and (len(violations_k) == 0) and (len(violations_l) == 0)

    return {
        "passed": passed,
        "thresholds": {"k": k_threshold, "l": l_threshold},
        "observed_minimums": {
            "min_k": 0 if min_k == float("inf") else min_k,
            "max_reidentification_prob": round(1.0 / min_k, 4) if min_k and min_k != float("inf") else 1.0,
            "min_l": 0 if min_l == float("inf") else min_l
        },
        "exposed_direct_identifiers_to_drop": sorted(list(exposed_direct)),
        "note_on_person_id": f"Drop '{person_id_col}' and shuffle row order AFTER passing this check before sending to non-local AI." if person_id_col else "Warning: No person_id_col provided; assuming 1 row = 1 distinct student.",
        "k_violations_count": len(violations_k),
        "l_violations_count": len(violations_l),
        "k_violations_sample": violations_k[:5],
        "l_violations_sample": violations_l[:5]
    }


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python3 check_k_anonymity.py <file.csv> <person_id_col|NONE> <quasi_cols_csv> <sensitive_cols_csv> [k=5] [l=2]")
        sys.exit(2)

    path = Path(sys.argv[1])
    p_col = None if sys.argv[2] == "NONE" else sys.argv[2]
    q_cols = [c.strip() for c in sys.argv[3].split(",") if c.strip()]
    s_cols = [c.strip() for c in sys.argv[4].split(",") if c.strip()]
    k_val = int(sys.argv[5]) if len(sys.argv) > 5 else 5
    l_val = int(sys.argv[6]) if len(sys.argv) > 6 else 2

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    res = evaluate_dataset(rows, p_col, q_cols, s_cols, k_val, l_val)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    sys.exit(0 if res["passed"] else 1)
