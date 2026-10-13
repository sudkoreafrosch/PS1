# -*- coding: utf-8 -*-
"""녹취록 엑셀에서 화자·발언을 추출해 인용 검증용 말뭉치를 만든다."""
import os
import unicodedata

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(HERE, "..", "input")

TRANSCRIPTS = {
    "260907": "260907_입법영향분석_산지전용관련_인터뷰_영천시.xlsx",
    "260910": "260910_입법영향분석_산지전용관련_인터뷰_산림청·진천군_정리본.xlsx",
    "260910memo": "260910_입법영향분석_산지전용관련_인터뷰_산림청·진천군_메모본.xlsx",
}


def norm(s):
    if s is None:
        return ""
    s = unicodedata.normalize("NFC", str(s))
    return s.replace("\xa0", " ").replace("\r\n", "\n").replace("\r", "\n")


def load_utterances(key):
    """(화자, 발언) 목록. 2열이 화자, 3열이 발언인 행만 추출."""
    path = os.path.join(INPUT_DIR, TRANSCRIPTS[key])
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb.worksheets[0]
    out = []
    for row in ws.iter_rows(values_only=True):
        if len(row) < 3:
            continue
        speaker, text = row[1], row[2]
        if speaker is None or text is None:
            continue
        out.append((norm(speaker).strip(), norm(text)))
    return out


def find_quote(key, speaker, quote):
    """인용문이 해당 화자의 발언 안에 글자 그대로 들어 있으면 True."""
    q = norm(quote)
    for sp, text in load_utterances(key):
        if sp == speaker and q in text:
            return True
    return False
