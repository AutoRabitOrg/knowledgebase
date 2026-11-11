#!/usr/bin/env python3
"""Prove a release-notes standardization changed formatting only.

Usage: verify.py <base_rev> <head_rev> [report.csv]

For every release-notes page changed between the two revisions it checks:
  * the page has the same number of lines;
  * every body line (not a heading or a release-date line) is identical,
    apart from heading anchors in links (#...), which the standardizer updates;
  * every heading keeps its version number and adds no new words except
    standard product and section names;
  * every release-date line keeps the same day, month and year.
Every changed heading and date is written to the report for a person to skim.
Exit code 1 if anything fails.
"""
import csv, re, subprocess, sys

ALLOWED_NEW_WORDS = {'autorabit', 'fixes', 'enhancements', 'new', 'features', 'rules', 'rule', 'dataloader', 'and', 'pro',
                     'self-hosted', 'codescan', 'arm', 'vault', 'guard', 'ncino', 'iz', 'suite', 'eagle', 'tiger',
                     'date', 'release', '+'} | set('january february march april may june july august september october november december'.split())
MONTHS = {m[:3]: i + 1 for i, m in enumerate('january february march april may june july august september october november december'.split())}

def git(*a): return subprocess.run(['git', *a], capture_output=True, text=True, check=True).stdout
def show(rev, path):
    r = subprocess.run(['git', 'show', f'{rev}:{path}'], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None

def strip_anchors(line): return re.sub(r'(\.md|\.autorabit\.com/[^\s)"#]*)#[A-Za-z0-9\-._]+', r'\1#', line)
def is_heading(line): return re.match(r'^#{1,6} ', line) is not None
def is_date(line): return re.search(r'release date', line, re.I) is not None and not re.search(r'<t[dh]', line)
def words(s): return re.findall(r"[a-z0-9][a-z0-9.\-+]*|\+", re.sub(r'<[^>]+>|&#x20;|\*\*|\\', ' ', s.lower()))
def visible(s): return re.sub(r'<a [^>]*></a>', '', s)  # hidden anchor tags aren't shown to readers
def versions(s): return re.findall(r'\d+(?:\.\d+)+', visible(s))
def date_of(s):
    t = re.sub(r'<[^>]+>|&#x20;|\*\*|\\', ' ', s)
    m = re.search(r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]{3,})\.?,?\s+(\d{4})', t) or None
    if m and m.group(2)[:3].lower() in MONTHS: return (int(m.group(1)), MONTHS[m.group(2)[:3].lower()], int(m.group(3)))
    m = re.search(r'([A-Za-z]{3,})\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})', t)
    if m and m.group(1)[:3].lower() in MONTHS: return (int(m.group(2)), MONTHS[m.group(1)[:3].lower()], int(m.group(3)))
    return None

def main(base, head, report_path=None):
    files = [f for f in git('diff', '--name-only', base, head, '--', '*.md').split('\n') if f.endswith('.md')]
    errors, rows, stats = [], [], dict(pages=0, body_lines=0, headings=0, dates=0)
    for f in files:
        old, new = show(base, f), show(head, f)
        if old is None or new is None:
            errors.append(f'{f}: page added or deleted (a standardization never does that)'); continue
        stats['pages'] += 1
        a, b = old.split('\n'), new.split('\n')
        if len(a) != len(b):
            errors.append(f'{f}: line count changed from {len(a)} to {len(b)}'); continue
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x == y:
                if not is_heading(x) and not is_date(x): stats['body_lines'] += 1
                continue
            if is_heading(x) != is_heading(y):
                errors.append(f'{f}:{i}: a heading became body text or the reverse'); continue
            if is_heading(x):
                stats['headings'] += 1
                if set(versions(x)) != set(versions(y)):
                    errors.append(f'{f}:{i}: version number changed: "{x}" -> "{y}"')
                extra = [w for w in words(y) if w not in words(visible(x)) and w not in ALLOWED_NEW_WORDS and not re.fullmatch(r'\d+(\.\d+)*', w)]
                if extra: errors.append(f'{f}:{i}: heading gained words {extra}: "{x}" -> "{y}"')
                rows.append((f, i, 'heading', x, y)); continue
            if is_date(x) or is_date(y):
                stats['dates'] += 1
                if date_of(x) != date_of(y): errors.append(f'{f}:{i}: date changed: "{x}" -> "{y}"')
                rows.append((f, i, 'date', x, y)); continue
            if strip_anchors(x) == strip_anchors(y):
                stats['body_lines'] += 1; rows.append((f, i, 'link anchor', x[:200], y[:200])); continue
            errors.append(f'{f}:{i}: body text changed:\n    before: {x[:160]}\n    after:  {y[:160]}')
    if report_path:
        with open(report_path, 'w', newline='') as fh:
            w = csv.writer(fh); w.writerow(['file', 'line', 'kind', 'before', 'after']); w.writerows(rows)
    print(f"Checked {stats['pages']} pages: {stats['body_lines']} body lines unchanged, "
          f"{stats['headings']} headings and {stats['dates']} dates reformatted.")
    for e in errors: print('ERROR', e)
    print('PASS: formatting changed, content did not.' if not errors else f'FAIL: {len(errors)} problem(s).')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:4]))
