# typing_demo.py v0.1.2 - HONEST PILOT
# YanRuoWeiYan Protocol - Pre-send hesitation prototype
# Status: Simulated Demo, n=1, NOT a real keylogger

import time
import json
from datetime import datetime

print("=== YanRuoWeiYan Protocol v0.1.1-pilot ===")
print("Mode: SIMULATED DEMO - sleep() intervals, NOT real keyboard hook")
print("This demo does NOT capture real keystrokes.")
print("==========================================\n")

class IntentGestaltSimulator:
    def __init__(self):
        self.pauses = []
        self.deletion_count = 0

    def on_key(self, char, pause_ms=None):
        if pause_ms:
            self.pauses.append(pause_ms)
            print(f"[Pause: {pause_ms}ms]")
        
    def on_delete(self):
        self.deletion_count += 1
        print(f"[Deletion: count={self.deletion_count}]")

    def get_result(self):
        longest = max(self.pauses) if self.pauses else 0
        anxiety_heuristic = min(100, int(0.6 * (longest**0.5) + 0.4 * self.deletion_count * 10))
        return {
            "meta": {"version": "v0.1.1-pilot", "n": 1, "mode": "simulated", "timestamp": datetime.now().isoformat()},
            "typing_pauses": self.pauses,
            "deletion_count": self.deletion_count,
            "longest_pause_ms": longest,
            "anxiety_score_heuristic": anxiety_heuristic,
            "disclaimer": "Heuristic only, n=1, Zhuyin IME includes selection pause, NOT a standard, NOT clinical anxiety"
        }

def run_simulation():
    engine = IntentGestaltSimulator()
    print("Simulating: typing '我要過嗎' with Zhuyin IME...")
    time.sleep(0.1)
    engine.on_key("我", pause_ms=1035)
    time.sleep(1.035)
    engine.on_key("要", pause_ms=1658)
    time.sleep(1.658)
    engine.on_key("過", pause_ms=2168)
    time.sleep(2.168)
    engine.on_delete()
    engine.on_delete()
    engine.on_delete()
    engine.on_delete()
    engine.on_key("嗎", pause_ms=5213)
    result = engine.get_result()
    print("\n=== Result (Simulated) ===")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("\n- Heuristic only, n=1, Zhuyin IME != anxiety")
    return result

if __name__ == "__main__":
    run_simulation()
