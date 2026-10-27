"""
Himeko Demo - Typing Pause Capture
v0.1.0 YanRuoWeiYan
Non-Invasive Intent Gestalt Demo
"""
import time
from collections import deque

class HimekoBuffer:
    def __init__(self):
        self.pauses = []
        self.deletions = 0
        self.revisions = deque(maxlen=3)
        self.last_time = time.time()
        
    def on_key(self, char, is_delete=False):
        now = time.time()
        gap = (now - self.last_time) * 1000
        
        if gap > 800:
            self.pauses.append(round(gap))
            print(f"[Intent Gestalt] 猶豫 {round(gap)}ms -> 不追問，只留白")
        
        if is_delete:
            self.deletions += 1
            self.revisions.append(f"刪除 @ {round(now%100)}s")
            print(f"[Strategic Ambiguity] 刪除重打 -> 保留最終判斷權給你")
        
        self.last_time = now
        anxiety = min(100, len(self.pauses)*10 + self.deletions*5)
        bar = "█" * (anxiety//10) + "░" * (10-anxiety//10)
        print(f"[Cognitive Buffer] 焦慮承接 {anxiety}% [{bar}]")
        
        return {
            "typing_pauses": self.pauses,
            "deletion_count": self.deletions,
            "anxiety_score": anxiety
        }

if __name__ == "__main__":
    print("=== 姬子引擎 Demo v0.1.0 ===")
    buf = HimekoBuffer()
    time.sleep(0.2)
    buf.on_key("我")
    time.sleep(0.3)
    buf.on_key("想")
    time.sleep(1.2)  # 猶豫
    buf.on_key("...", is_delete=False)
    time.sleep(0.2)
    buf.on_key("", is_delete=True)
    result = buf.on_key("決定")
    print("\n最終 JSON:", result)
