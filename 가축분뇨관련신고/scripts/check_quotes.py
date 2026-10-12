# -*- coding: utf-8 -*-
"""녹취록 인용 검증 모듈.
extract_transcript.py가 만든 notes/transcript_*.json에서 화자·발언을 읽어,
[발언] 인용문이 녹취록에 글자 단위로 그대로 들어 있는지 확인한다.
"""
import json, sys, pathlib

NOTES = pathlib.Path(__file__).resolve().parent.parent / "notes"
TRANSCRIPTS = {
    "안동": NOTES / "transcript_260914_안동.json",
    "진천": NOTES / "transcript_260911_진천.json",
}

def load(key):
    rows = json.load(open(TRANSCRIPTS[key], encoding="utf-8"))
    by_speaker = {}
    for r in rows:
        by_speaker.setdefault(r["speaker"], []).append(r["text"])
    return by_speaker

_cache = {}
def verify(key, speaker, quote):
    """해당 인터뷰(key)에서 speaker의 발언 중 quote를 부분 문자열로 포함하는 것이 있으면 True."""
    if key not in _cache:
        _cache[key] = load(key)
    texts = _cache[key].get(speaker, [])
    return any(quote in t for t in texts)

def verify_all(items):
    """items: iterable of (key, speaker, quote). 불일치 목록 반환."""
    bad = []
    for key, speaker, quote in items:
        if not verify(key, speaker, quote):
            bad.append((key, speaker, quote))
    return bad

if __name__ == "__main__":
    # 간단 자가 테스트
    assert verify("진천", "구도원", "그건 서식에 나와 있습니다.")
    assert not verify("진천", "구도원", "존재하지 않는 문장")
    print("check_quotes self-test OK")
