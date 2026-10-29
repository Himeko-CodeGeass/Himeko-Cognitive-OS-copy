# Himeko-YanRuoWeiYan
## YanRuoWeiYan Protocol - v0.1.1 Pilot

The first step of Human-AI Alignment is not to see through each other, but to learn respectful blank space.

[Release: v0.1.1-pilot] | [Status: Early Prototype, n=1] | [License: Polyform Noncommercial + Commercial] | [Book: WeiYan (Unsaid)]

### 1. What This Is (and Is Not)
This is a **pilot prototype** for pre-send hesitation, not a standard.

Case Study - 2026-10-27:
- 1 user, 1 session, 4 pauses observed, longest 5213ms
- Input method: Chinese Zhuyin (注音). Pauses include IME candidate selection, not necessarily anxiety.
- This is NOT "The 5.2s Standard". 5213ms is an observed data point, not a universal threshold.

```json
{
  "meta": { "version": "v0.1.1-pilot", "n": 1 },
  "typing_pauses": [1035, 1658, 2168, 5213],
  "deletion_count": 4,
  "anxiety_score_heuristic": 60
}
```

**anxiety_score: How it is calculated (heuristic, not clinical)**
`score = clamp( w1 * log(longest_pause) + w2 * deletion_rate )`
w1=0.6, w2=0.4 in this pilot. No clinical validation, error bars unknown. 
Full algorithm and limitations will be in `/docs/anxiety_score.md`. We will publish a multi-user study before claiming anything.

### 2. Core Principle: User-Owned Buffer, Not Surveillance
We noticed a contradiction in v0.1.0: claiming "non-invasive" while capturing deleted text.

v0.1.1 fix:
- **On-device only**: All pause/deletion data stays on device, never uploaded
- **Opt-in**: Feature is OFF by default, user must enable
- **No log of deleted content**: We store *that* a deletion happened (count + timing), not *what* was deleted, unless user explicitly opts into content logging
- **Purgeable**: One click to delete local buffer
- If we cannot guarantee the above, we do not ship the feature.

### 3. Scope v0.1.1: One Scenario Only
**Pre-send hesitation in messaging: "Should I send this?"**

We are focusing on writing/IM first. Not defense, drones, space, or mental health crisis detection. Those are moved to speculative ideas in `/docs/future_research_ideas.md` and are not claimed as validated use cases.

### 4. Architecture
- `core/` - pause timer, deletion counter (no content logger by default)
- `examples/typing_demo.py` - local demo
- `docs/` - methodology, limitations, future ideas

### 5. Quick Start
```bash
git clone https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan
cd Himeko-YanRuoWeiYan
python examples/typing_demo.py
```

### 6. License - Changed in v0.1.1
**Why changed:** MIT allows free commercial use, so "MIT but pay for commercial" is legally conflicting.

- **Code v0.1.1 and after: Polyform Noncommercial 1.0.0**
  - Free for personal use, research, non-commercial open-source
  - Commercial use requires a separate Commercial License
- **Code before v0.1.0 (commits <=123): Still MIT** as originally published
- **Commercial License: Tingmo Creative**
  - For closed-source products, includes support
  - Buy: https://tingmocreative.lemonsqueezy.com/checkout/buy/5d845d7e-6c55-4b27-9481-d06c62c776ff

Contact: jizheng.contact@proton.me

### 7. What We Need Next
- Multi-user dataset (n>20), different input methods (Pinyin, Zhuyin, English)
- Publish anxiety_score algorithm with false positive rate
- User study: does a 2-second buffer actually help users feel more autonomous?

---
# Himeko-YanRuoWeiYan
## 言若微言 - v0.1.1 原型版

人機共築輝煌的第一步，不是看穿彼此，而是學會尊重的留白。

### 1. 這是什麼（和不是什麼）
這是**單人先導原型**，不是標準。
- 2026-10-27 案例：1 人、1 次輸入、4 次停頓，最長 5213ms
- 輸入法：注音。停頓包含選字時間，不等於焦慮
- 5213ms 是觀察到的數據點，不是全人類的「5.2秒標準」

**anxiety_score 60 怎麼算的**
目前是啟發式：`分數 = log(最長停頓) + 刪除率` 加權，無臨床驗證，誤差未知，演算法將公開在 `/docs/anxiety_score.md`

### 2. 核心原則修正：使用者擁有的緩衝區，不是監控
v0.1.0 矛盾：說「非侵入」卻抓刪除的字。
v0.1.1 修正：
- **只在本地**：不上傳
- **預設關閉**：需使用者主動開啟
- **不存刪除內容**：只存「刪了幾次、停多久」，不存「刪了什麼」，除非使用者主動開啟內容紀錄
- **可一鍵清除**

### 3. 範圍：v0.1.1 只做一件事
**寫訊息前的猶豫：「這句要不要傳？」**
國防、無人機、太空、身心靈危機偵測，全部從主頁移除，移到 `/docs/future_research_ideas.md` 標註為未驗證構想。

### 4. 快速開始
```bash
git clone https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan
python examples/typing_demo.py
```

### 5. 授權 - v0.1.1 已更改
- **v0.1.1 之後：Polyform Noncommercial 1.0.0** 個人、研究、非營利開源免費，商用需另購商業授權
- **v0.1.0 之前：仍為 MIT**
- **商業授權：聽默文創** 購買連結同上

### 6. 下一步需要的證據
多人資料、不同輸入法、誤判率、使用者自主感研究

*Powered by Respectful Buffer - Early Prototype - Tingmo Creative*
