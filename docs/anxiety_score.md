# anxiety_score - Heuristic, Not Clinical - Reproducible v0.1.1-pilot
Status: v0.1.1-pilot, n=1, unverified, heuristic only, NOT clinical, NOT a standard

## Formula (current pilot - actual code)
```
anxiety_score_heuristic = clamp(0.6 * sqrt(longest_pause_ms) + 0.4 * (deletion_count * 10), 0, 100)
clamp(x,0,100) = max(0, min(100, x))
sqrt = **0.5 (Python: longest_pause_ms ** 0.5)
deletion_rate = deletion_count * 10  (scales 0-10 deletions to 0-100)
int() truncation after calc, doc rounds to nearest for readability
```
Actual code: typing_demo.py line: anxiety_heuristic = min(100, int(0.6 * (longest ** 0.5) + 0.4 * deletion_count * 10))

## Reproducible Example - n=1 case 2026-10-27
Input from README case study:
- typing_pauses = [1035, 1658, 2168, 5213] ms
- longest_pause_ms = 5213
- deletion_count = 4

Calculation:
- sqrt(5213) = 72.199...
- 0.6 * 72.199 = 43.319
- deletion_count * 10 = 40
- 0.4 * 40 = 16
- sum = 43.319 + 16 = 59.319
- int(59.319) = 59 -> doc shows 60 (rounded, tolerance +-1)

Result matches typing_demo.py output: 59 (or 60 rounded).

## Why not log? Why sqrt?
Early doc wrote:
score = clamp(0-100, w1 * log(l...
w1=0.6, w2=0.3, w3=0.1
- log base not defined, w3 revision_count not implemented, deletion_rate = deletions/total keystrokes not defined -> irreproducible.
- v0.1.1 fixes doc to match code: sqrt dampens 5s+ pauses without log base confusion, w1=0.6, w2=0.4 only, no w3.
- Future: will publish log vs sqrt comparison with false positive rate when n>=20.

## Why this is NOT anxiety
- Chinese Zhuyin (注音) includes candidate selection pause: 1035ms, 1658ms etc may be IME selection, not hesitation. Pinyin, English have different patterns.
- n=1, single session, simulated with sleep(): NOT real key hook, NOT real user, no inter-rater, no test-retest.
- No false positive rate, no clinical validation: No PHQ-9, GAD-7 correlation, no clinician review.
- Deletion only count/timing, NOT content: We store that deletion happened, not what was deleted, but still heuristic.
- NOT diagnostic, NOT for critical decisions: Do NOT use for defense, law, drone, agriculture, weather, education, gaming, self-driving, space, mental health diagnosis.

## On-device only proof (for audit point 5)
- core/ must have no network: no import requests, httpx, openai, socket, fetch
- No content logging: no logger.info(user_message), only msg_len, hash, count, timing
- Opt-in OFF by default, purgeable
- Render legacy: srv-dafmmof40ujc73bvhn3g SUSPENDED 2026-10-29, main.py P0 fix: no content log, webhook secret check, rate limit
- Legacy cloud files: api/, Procfile, render.yaml will move to legacy_cloud_demo/ next commit

## What We Need Next
- core/key_hook.py: real local hook, opt-in OFF, on-device only, purgeable, no network
- Multi-user dataset n>=20, different input methods (Pinyin, Zhuyin, English)
- Publish false positive rate, user study: does 2-second buffer help users feel more autonomous?
- Publish anxiety_score algorithm with log vs sqrt ablation

## Links for audit
- Demo: typing_demo.py in root, examples/typing_demo.py same file
- Core: core/ - pause timer, deletion counter (no content logger by default)
- Future ideas: docs/future_research_ideas.md (10 domains as ideas, not claims)
- License: v0.1.0 and before = MIT, v0.1.1+ = Polyform Noncommercial 1.0.0 (NOT OSI) + Commercial License
- Commercial: Tingmo Creative, pre-order pilot, Early Bird All Access $999 (NT$32,000) gets all generations free via Product ID 5d845d7e-6c55-4b27-9481-d06c62c776ff, contact jizheng.contact@proton.me

---
Not clinical advice. Heuristic only. See README v0.1.1-pilot.
