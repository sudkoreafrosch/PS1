# -*- coding: utf-8 -*-
"""생성된 엑셀의 '내용' 열 [발언] 인용문을 녹취록 추출본(notes/transcripts.json)과 독립적으로 재대조한다.
build_xlsx.py의 assert와 별개로, 완성 파일을 읽어 검증한다."""
import json, pathlib, re, sys
import openpyxl

BASE = pathlib.Path(__file__).resolve().parent.parent
TR = json.loads((BASE / "notes" / "transcripts.json").read_text(encoding="utf-8"))
ALL = [(k, u["speaker"], u["text"]) for k, us in TR.items() for u in us]
xlsx = sorted((BASE / "output").glob("*.xlsx"))[-1]
wb = openpyxl.load_workbook(xlsx)
ws = wb["법령개정 필요사항"]
pat = re.compile(r'(?:\(면담자 (\S+)\)|(\S+?):) "([^"]+)"')
bad, total = [], 0
for row in ws.iter_rows(min_row=2, values_only=True):
    no, body = row[0], row[5] or ""
    if "[발언]" not in body:
        continue
    seg = body.split("[발언]", 1)[1]
    for m in pat.finditer(seg):
        spk = m.group(1) or m.group(2)
        frag = m.group(3)
        total += 1
        if not any(s == spk and frag in t for _, s, t in ALL):
            bad.append((no, spk, frag[:50]))
print(f"checked {xlsx.name}: {total} quotes, {len(bad)} mismatches")
for b in bad:
    print("  MISMATCH", b)
sys.exit(1 if bad else 0)
