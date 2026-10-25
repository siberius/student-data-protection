"""Kontrola stylu a relativních odkazů v dokumentaci.

Pravidla: žádná dlouhá pomlčka, žádná spojovací pomlčka s mezerami,
žádné šablonové fráze, relativní Markdown odkazy musí existovat.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', 'node_modules'}
LINK = re.compile(r'\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
BAD_PHRASES = [
    'v neposlední řadě', 'je důležité si uvědomit', 'v dnešní době',
    'závěrem lze říci', "in today's world", 'it is important to note',
    'to sum up', 'at the end of the day',
]

def check_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding='utf-8')
    for number, line in enumerate(text.splitlines(), 1):
        if '—' in line:
            errors.append(f'{path}:{number}: dlouhá pomlčka (—)')
        if ' – ' in line:
            errors.append(f'{path}:{number}: spojovací pomlčka s mezerami ( – )')
        low = line.lower()
        for phrase in BAD_PHRASES:
            if phrase in low:
                errors.append(f'{path}:{number}: šablonová fráze „{phrase}“')
        for target in LINK.findall(line):
            if re.match(r'(https?:|mailto:|#)', target):
                continue
            clean = target.split('#', 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if not resolved.exists():
                errors.append(f'{path}:{number}: odkaz neexistuje: {target}')
    return errors

def main() -> int:
    errors = []
    for path in sorted(ROOT.rglob('*.md')):
        if any(part in SKIP for part in path.parts):
            continue
        errors.extend(check_file(path))
    if errors:
        print('NÁLEZY:')
        for error in errors:
            print(' - ' + error)
        return 1
    print('Texty a relativní odkazy OK.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
