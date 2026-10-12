# 녹취록 엑셀에서 화자·발언을 추출해 텍스트와 JSON으로 저장한다.
import sys, json, pathlib, openpyxl
base = pathlib.Path(__file__).resolve().parent.parent
out = base / "notes"
allq = {}
for p in sorted((base / "input").glob("*.xlsx")):
    wb = openpyxl.load_workbook(p)
    ws = wb.worksheets[0]
    lines, utt = [], []
    for i, row in enumerate(ws.iter_rows(values_only=True), start=1):
        cells = [c for c in row if c is not None]
        if not cells: continue
        if row[0] is not None and (row[1] is None or i <= 3):
            lines.append(f"[메타 r{i}] " + " | ".join(str(c) for c in cells)); continue
        spk = str(row[1]).strip() if row[1] is not None else "?"
        txt = str(row[2]).strip() if len(row) > 2 and row[2] is not None else ""
        extra = [str(c) for c in row[3:] if c is not None]
        lines.append(f"r{i} {spk}: {txt}" + (f"   [[col4+: {' | '.join(extra)}]]" if extra else ""))
        utt.append({"row": i, "speaker": spk, "text": txt, "extra": extra})
    key = p.stem
    allq[key] = utt
    (out / f"transcript_{key}.txt").write_text("\n".join(lines), encoding="utf-8")
    print(key, "utterances:", len(utt), "chars:", sum(len(u['text']) for u in utt))
(out / "transcripts.json").write_text(json.dumps(allq, ensure_ascii=False, indent=1), encoding="utf-8")
