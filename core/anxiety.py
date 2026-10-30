# core/anxiety.py - On-device only proof - v0.1.1-pilot
# No network: no requests, httpx, openai, socket, fetch
# No content logging: only count/timing

import math

def calculate_heuristic(longest_pause_ms, deletion_count):
    score = 0.6 * (longest_pause_ms ** 0.5) + 0.4 * (deletion_count * 10)
    if score < 0:
        score = 0
    if score > 100:
        score = 100
    return int(score)

def get_intent_gestalt(pauses, deletion_count):
    longest = max(pauses) if pauses else 0
    return {
        "typing_pauses": pauses,
        "deletion_count": deletion_count,
        "longest_pause_ms": longest,
        "anxiety_score_heuristic": calculate_heuristic(longest, deletion_count),
        "disclaimer": "Heuristic only, n=1, Zhuyin IME != anxiety, NOT clinical",
        "on_device": True,
        "network_requests": False
    }
