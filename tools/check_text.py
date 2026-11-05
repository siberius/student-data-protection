"""Kontrola stylu a relativních odkazů v dokumentaci.

Pravidla: žádná dlouhá pomlčka, žádná spojovací pomlčka s mezerami,
žádné šablonové fráze, relativní Markdown odkazy musí existovat.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {'.git', 'node_modules', 'testing'}
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

def check_bundles() -> list[str]:
    """Catch stale/missing security guidance in the distributed native bundles."""
    errors = []
    groups = {
        'workflow': [1], 'legal': [2], 'ai-act': [3], 'data': [4],
        'identity': [5, 6], 'crypto': [7], 'storage': [8], 'web': [9],
        'operations': [10, 11], 'verification': [12, 13, 14],
        'ai-data': [15], 'sso': [16], 'practical-solutions': [17], 'publication': [18],
    }
    editions = [('.', 'student-data-protection.md', 'source-register.md'),
                ('cs', 'ochrana-dat-zaku.md', 'registr-zdroju.md'),
                ('es', 'proteccion-datos-alumnado.md', 'registro-fuentes.md')]
    for directory, filename, register in editions:
        source = ROOT / 'docs' / filename
        bundle = ROOT / directory
        if not source.exists() or not (bundle / 'SKILL.md').exists():
            errors.append(f'Missing source or native core: {directory}')
            continue
        text = source.read_text(encoding='utf-8')
        matches = list(re.finditer(r'^## (\d+)\. .+$', text, re.M))
        sections = {int(m.group(1)): text[m.start():matches[i+1].start() if i+1 < len(matches) else len(text)].strip()
                    for i, m in enumerate(matches)}
        if set(sections) != set(range(1, 19)):
            errors.append(f'Unexpected source sections: {source}')
            continue
        ids = re.findall(r'^\| (AT\d+) \|', text, re.M)
        if ids != [f'AT{i:02d}' for i in range(1, 37)]:
            errors.append(f'Acceptance scenario coverage/order changed: {source}')
        for name, numbers in groups.items():
            target = bundle / 'references' / (name + '.md')
            rendered = target.read_text(encoding='utf-8') if target.exists() else ''
            for number in numbers:
                if sections[number] not in rendered:
                    errors.append(f'Stale reference: {target} section {number}')
        register_source = ROOT / 'docs' / register
        register_target = bundle / 'references/source-status.md'
        if (not register_source.exists() or not register_target.exists()
                or register_source.read_text(encoding='utf-8') not in register_target.read_text(encoding='utf-8')):
            errors.append(f'Stale source register: {register_target}')
        license_file = bundle / 'LICENSE'
        if not license_file.exists() or license_file.read_bytes() != (ROOT / 'LICENSE').read_bytes():
            errors.append(f'License copy differs: {license_file}')
    return errors

def main() -> int:
    errors = check_bundles()
    for path in sorted(ROOT.rglob('*.md')):
        if any(part in SKIP for part in path.parts):
            continue
        errors.extend(check_file(path))
    if errors:
        print('NÁLEZY:')
        for error in errors:
            print(' - ' + error)
        return 1
    print('Texty, relativní odkazy a shoda nativních referencí OK.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
