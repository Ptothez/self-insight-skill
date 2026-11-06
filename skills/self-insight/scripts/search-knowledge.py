"""Search the bundled knowledge locally; no API, account, original course or absolute path required."""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def features(value):
    text = value.lower()
    result = re.findall(r'[a-z0-9]{2,}', text)
    for run in re.findall(r'[\u3400-\u9fff]+', text):
        result.extend(run[i:i+2] for i in range(len(run)-1))
    return Counter(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs='?', default='')
    parser.add_argument('--module')
    parser.add_argument('--id', action='append', default=[])
    parser.add_argument('--source')
    parser.add_argument('--related', action='store_true')
    parser.add_argument('--limit', type=int, default=12)
    parser.add_argument('--offset', type=int, default=0)
    parser.add_argument('--library', type=Path)
    parser.add_argument('--list-sources', action='store_true')
    parser.add_argument('--origin', choices=['all', 'legacy', 'expanded'], default='all')
    parser.add_argument('--include-context', action='store_true')
    args = parser.parse_args()
    base = args.library or Path(__file__).resolve().parent.parent / 'references/full-knowledge'
    catalog = read_json(base / 'catalog.json')
    if args.list_sources:
        print(json.dumps(catalog['sources'], ensure_ascii=False, indent=2))
        return
    records = []
    files = [base / 'records' / (s['id'] + '.jsonl') for s in catalog['sources'] if s.get('records')]
    for path in files:
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            if line.strip():
                row = json.loads(line)
                row.setdefault('source_refs', [{'source_id': path.stem, 'blocks': []}])
                records.append(row)
    legacy = base / 'legacy-records.jsonl'
    if legacy.is_file():
        records.extend(json.loads(line) for line in legacy.read_text(encoding='utf-8-sig').splitlines() if line.strip())
    all_by_id = {r['id']: r for r in records}
    if args.origin == 'legacy':
        records = [r for r in records if r['id'].startswith('legacy:')]
    elif args.origin == 'expanded':
        records = [r for r in records if not r['id'].startswith('legacy:')]
    if args.source:
        records = [r for r in records if any(x['source_id']==args.source for x in r['source_refs'])]
    if not args.include_context and not args.id:
        records = [r for r in records if r.get('retrieval_scope', 'knowledge') == 'knowledge']
    if args.module:
        records = [r for r in records if args.module in r['modules']]
    by_id = {r['id']: r for r in records}
    if args.id:
        missing = [x for x in args.id if x not in by_id]
        if missing:
            raise SystemExit('Unknown id in selected scope: ' + ', '.join(missing))
        selected = [by_id[x] for x in args.id]
        if args.related:
            extra = {edge['target'] for r in selected for edge in r['relations']}
            selected += [all_by_id[x] for x in sorted(extra-set(args.id)) if x in all_by_id]
        total = len(selected)
    else:
        if not args.query and not args.source:
            parser.error('Provide a query, --source or --id')
        query = features(args.query)
        scored = []
        for r in records:
            title = features(r['title'] + ' ' + ' '.join(r['tags']) + ' ' + ' '.join(r.get('alternate_titles', [])))
            body = features(r['content'] + ' ' + ' '.join(r['steps'] + r['conditions'] + r['limits']))
            score = sum(min(n, title[k])*5 + min(n, body[k]) for k, n in query.items())
            if args.query and args.query in r['title']:
                score += 40
            if score or not args.query:
                scored.append((score, r))
        scored.sort(key=lambda x: (-x[0], x[1]['id']))
        total = len(scored)
        selected = [r for _, r in scored[args.offset:args.offset + max(1, args.limit)]]
    print(json.dumps({'total_matches': total, 'returned': len(selected), 'records': selected,
                      'note': 'Source-grounded course knowledge, not clinical or scientific validation.'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
