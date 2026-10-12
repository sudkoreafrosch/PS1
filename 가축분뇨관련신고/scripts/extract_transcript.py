import openpyxl, sys, json
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src)
ws = wb.worksheets[0]
rows = []
with open(out, 'w', encoding='utf-8') as f:
    for i, r in enumerate(ws.iter_rows(values_only=True), start=1):
        cells = [c for c in r if c is not None]
        if not cells:
            continue
        if r[1] is not None and r[2] is not None:
            f.write(f"[{i}] {r[1]}: {r[2]}\n")
            rows.append({"row": i, "speaker": str(r[1]).strip(), "text": str(r[2])})
            extra = [str(c) for c in r[3:] if c is not None]
            if extra:
                f.write(f"    (extra cols: {extra})\n")
        else:
            f.write(f"[{i}] META: {' | '.join(str(c) for c in cells)}\n")
json.dump(rows, open(out.replace('.txt', '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(out, len(rows), "utterances")
