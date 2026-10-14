# -*- coding: utf-8 -*-
"""녹취록 엑셀에서 화자·발언을 추출하고, 인용문이 녹취록에 그대로 들어 있는지 검증한다.

사용:
    python3 -I scripts/check_quotes.py            # 녹취록 추출 결과를 notes/transcript_dump.txt 로 저장
    (build_xlsx.py 가 verify_quote() 를 import 하여 assert 에 사용)

대조 규칙: 인용문과 녹취록 모두 연속 공백(줄바꿈 포함)을 한 칸으로 정규화한 뒤
글자 단위 부분문자열 일치를 요구한다. 공백 정규화 외의 변형(철자·조사 수정 등)은 허용하지 않는다.
"""
import os
import re
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INPUT_DIR = os.path.join(ROOT, "input")

TRANSCRIPTS = {
    "정은지": "260825_신고제도_정은지행정사_녹취록.xlsx",
    "이종서": "260826_신고제도_이종서행정사_녹취록.xlsx",
    "박정모": "260826_신고제도_박정모행정사_녹취록.xlsx",
    "이범원": "260828_신고제도_이범원행정사_녹취록.xlsx",
}


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def load_transcript(path: str):
    """(speaker, text) 리스트 반환. 열 구성이 파일마다 달라(2~4열) 가장 긴 문자열을 발언으로 본다."""
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb.worksheets[0]
    rows = []
    for row in ws.iter_rows(values_only=True):
        cells = [c for c in row if c is not None and str(c).strip() != ""]
        if not cells:
            continue
        strs = [str(c) for c in cells]
        text = max(strs, key=len)
        others = [s for s in strs if s is not text]
        speaker = ""
        for s in others:
            # 화자명: 짧은 한글 이름(2~4자), 시간표기(00:10) 제외
            if re.fullmatch(r"[가-힣]{2,4}", s.strip()):
                speaker = s.strip()
                break
        rows.append((speaker, text))
    return rows


_CACHE = {}


def transcript_text(interviewee: str) -> str:
    if interviewee not in _CACHE:
        path = os.path.join(INPUT_DIR, TRANSCRIPTS[interviewee])
        rows = load_transcript(path)
        _CACHE[interviewee] = norm(" \n ".join(t for _, t in rows))
    return _CACHE[interviewee]


def verify_quote(interviewee: str, quote: str) -> bool:
    return norm(quote) in transcript_text(interviewee)


def dump():
    out = os.path.join(ROOT, "notes", "transcript_dump.txt")
    with open(out, "w", encoding="utf-8") as f:
        for name, fn in TRANSCRIPTS.items():
            f.write(f"===== {name} ({fn}) =====\n")
            for i, (sp, tx) in enumerate(load_transcript(os.path.join(INPUT_DIR, fn)), 1):
                f.write(f"[{i}] {sp} | {norm(tx)}\n")
            f.write("\n")
    print("saved:", out)


if __name__ == "__main__":
    dump()
    if len(sys.argv) > 2:
        print(verify_quote(sys.argv[1], sys.argv[2]))
