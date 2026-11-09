import re
from pathlib import Path


def load_art(path: Path) -> tuple[dict[str, int], list[list[tuple[int, str]]]]:
    colors = {}
    rows = []
    sections = set()
    section = None

    try:
        lines = path.read_text(encoding='utf-8').splitlines()
    except UnicodeError as error:
        raise ValueError(f'{path}: file is not valid UTF-8') from error

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if not line or line.startswith('#'):
            continue

        if line.startswith('[') and line.endswith(']'):
            section = line[1:-1].strip().lower()
            if section not in {'colours', 'diagram'}:
                raise ValueError(f'{path}:{line_number}: unknown section {line!r}')
            if section in sections:
                raise ValueError(f'{path}:{line_number}: duplicate section {line!r}')
            sections.add(section)
            continue

        if section is None:
            raise ValueError(f'{path}:{line_number}: content before a section')

        if section == 'colours':
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f'{path}:{line_number}: expected NAME ANSI_CODE')
            name, code_text = parts
            try:
                code = int(code_text)
            except ValueError as error:
                raise ValueError(f'{path}:{line_number}: ANSI code must be an integer') from error
            if code < 0:
                raise ValueError(f'{path}:{line_number}: ANSI code cannot be negative')
            if name in colors:
                raise ValueError(f'{path}:{line_number}: duplicate colour {name!r}')
            colors[name] = code
            continue

        row = []
        for chunk in line.split():
            match = re.fullmatch(r'([0-9]+)([A-Za-z][A-Za-z0-9_]*)', chunk)
            if match is None:
                raise ValueError(f'{path}:{line_number}: invalid diagram chunk {chunk!r}')
            count = int(match.group(1))
            color_name = match.group(2)
            if count == 0:
                raise ValueError(f'{path}:{line_number}: chunk size must be positive')
            if color_name not in colors:
                raise ValueError(
                    f'{path}:{line_number}: undefined colour {color_name!r}'
                )
            row.append((count, color_name))
        rows.append(row)

    if 'colours' not in sections or 'diagram' not in sections:
        raise ValueError(f'{path}: file must contain [colours] and [diagram] sections')
    if not colors:
        raise ValueError(f'{path}: [colours] section must define at least one colour')
    if not rows:
        raise ValueError(f'{path}: [diagram] section must contain at least one row')

    return colors, rows
