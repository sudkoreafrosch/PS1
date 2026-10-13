# -*- coding: utf-8 -*-
"""녹취록 인용 검증 모듈.

녹취록 엑셀(화자/발언 2열)에서 발언 텍스트를 추출해 두고,
결과물의 모든 "..." 인용문이 녹취록 안에 글자 단위로 들어 있는지 확인한다.
build_xlsx.py 가 import 해서 assert 로 사용한다.
"""
import re
import sys
from pathlib import Path

import openpyxl

INPUT_DIR = Path(__file__).resolve().parent.parent / "input"
TRANSCRIPTS = {
    "260904": INPUT_DIR / "260904_입법영향분석_식품위생관련신고_인터뷰.xlsx",
    "260917": INPUT_DIR / "260917_입법영향분석_식품위생관련신고_인터뷰.xlsx",
}

_WS = re.compile(r"\s+")


def _norm(s: str) -> str:
    return _WS.sub("", s or "")


def load_transcripts() -> dict:
    """{key: {'speakers': {name: normalized_text}, 'all': normalized_text}}"""
    out = {}
    for key, path in TRANSCRIPTS.items():
        wb = openpyxl.load_workbook(path, read_only=True)
        ws = wb.worksheets[0]
        speakers = {}
        chunks = []
        for row in ws.iter_rows(values_only=True):
            cells = [str(c) for c in row if c is not None]
            if len(cells) >= 2:
                spk, txt = cells[-2], cells[-1]
                speakers.setdefault(spk, []).append(txt)
                chunks.append(txt)
        out[key] = {
            "speakers": {k: _norm("\n".join(v)) for k, v in speakers.items()},
            "all": _norm("\n".join(chunks)),
        }
    return out


QUOTE_RE = re.compile(r'"([^"]+)"')


def extract_quotes(text: str):
    return QUOTE_RE.findall(text or "")


def verify(text: str, key: str, transcripts: dict, label: str = ""):
    """text 안의 모든 "..." 인용이 key 녹취록 안에 있는지 확인. 실패 목록 반환."""
    bad = []
    corpus = transcripts[key]["all"]
    for q in extract_quotes(text):
        if _norm(q) not in corpus:
            bad.append((label, key, q))
    return bad


def verify_any(text: str, transcripts: dict, label: str = ""):
    bad = []
    for q in extract_quotes(text):
        nq = _norm(q)
        if not any(nq in t["all"] for t in transcripts.values()):
            bad.append((label, "any", q))
    return bad


if __name__ == "__main__":
    t = load_transcripts()
    for k, v in t.items():
        print(k, "speakers:", list(v["speakers"].keys()), "chars:", len(v["all"]))
    if len(sys.argv) > 1:
        q = sys.argv[1]
        print(verify_any(f'"{q}"', t, "cli"))
