# anxiety_score - Heuristic, Not Clinical

**Status: v0.1.1-pilot, n=1, unverified**

## Formula (current pilot)
```
score = clamp(0-100, w1 * log(longest_pause_ms) + w2 * deletion_rate + w3 * revision_count)
w1=0.6, w2=0.3, w3=0.1
```
- longest_pause_ms: longest pause in session (5213ms in pilot)
- deletion_rate: deletions / total keystrokes
- revision_count: number of delete-retype cycles

## Why this is NOT anxiety
- Chinese Zhuyin input includes candidate selection (選字) pause
- No ground truth: we did not measure STAI, GSR, or self-reported anxiety
- No baseline per user

## Limitations
- n=1, single user, single session
- No false positive / false negative rate
- IME dependent: Pinyin, Zhuyin, English will differ
- No cross-validation

## What we will publish next
- /docs/study_protocol.md: multi-user protocol (n>=20), consent, task design
- Dataset: anonymized pause/deletion counts only, no content, with opt-in
- Error analysis

## Current implementation
See `core/anxiety.py` - if file logs content, it violates README promise. Should only store counts/timings.
