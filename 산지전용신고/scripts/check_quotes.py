# -*- coding: utf-8 -*-
"""본표 [발언] 인용문을 녹취록과 글자 단위로 대조해 결과를 출력한다(빌드와 별도 실행용)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_xlsx import MAIN_ROWS, verify_quotes  # noqa: E402

ok = True
for i, row in enumerate(MAIN_ROWS, start=1):
    bad = verify_quotes(row["iv"]["key"], row["quotes"])
    total = len(row["quotes"])
    print(f"연번 {i} ({row['iv']['date']}): 인용 {total}건 중 불일치 {len(bad)}건")
    for sp, text in bad:
        ok = False
        print(f"  - {sp}: {text}")
print("결과:", "모두 일치" if ok else "불일치 있음")
sys.exit(0 if ok else 1)
