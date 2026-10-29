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
Full algorithm in `/docs/anxiety_score.md`.

### 2. Core Principle: User-Owned Buffer, Not Surveillance
v0.1.1 fix:
- **On-device only**: All pause/deletion data stays on device, never uploaded
- **Opt-in**: Feature is OFF by default
- **No log of deleted content**: We store *that* a deletion happened (count + timing), not *what* was deleted
- **Purgeable**: One click to delete local buffer

**Note on legacy cloud files:** `api/`, `Procfile`, `render.yaml` are legacy from v0.1.0 cloud demo and are NOT used in v0.1.1 on-device core. They will be moved to `/legacy_cloud_demo/` in next commit. Core in `core/` runs locally only.

### 3. Scope v0.1.1: One Scenario Only
**Pre-send hesitation in messaging: "Should I send this?"**

Other domains are speculative and moved to `/docs/future_research_ideas.md`, not claimed as validated.

### 4. Architecture
- `core/` - pause timer, deletion counter (no content logger by default)
- `typing_demo.py` - local demo in root
- `examples/` - examples (may contain copy of demo)
- `docs/` - methodology: `docs/anxiety_score.md`, `docs/future_research_ideas.md`

### 5. Quick Start
```bash
git clone https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan
cd Himeko-YanRuoWeiYan
python typing_demo.py
```

### 6. License - Changed in v0.1.1
**Why changed:** MIT allows free commercial use, so "MIT but pay for commercial" is legally conflicting.

- **v0.1.1 and after: Polyform Noncommercial 1.0.0**
  - Free for personal use, research, non-commercial open-source
  - Commercial use requires a separate Commercial License
  - **Note:** Polyform Noncommercial is NOT OSI-approved Open Source. This repo is source-available prototype.
- **Before v0.1.0 (commits <=123): Still MIT** - That version CAN be used commercially under MIT terms. Disclosure for transparency.
- **Commercial License: Tingmo Creative - Contact for pilot partnership**
  - Current stage is prototype (n=1). For closed-source pilot, contact first.
  - Store: https://tingmocreative.lemonsqueezy.com
  - Checkout (pre-order / pilot): https://tingmocreative.lemonsqueezy.com/checkout/buy/5d845d7e-6c55-4b27-9481-d06c62c776ff
  - Contact: jizheng.contact@proton.me

Not legal advice.

### 7. What We Need Next
- Multi-user dataset (n>20), different input methods (Pinyin, Zhuyin, English)
- Publish anxiety_score algorithm with false positive rate
- User study: does a 2-second buffer actually help users feel more autonomous?

---
# Himeko-YanRuoWeiYan
## 言若微言 - v0.1.1 原型版

人機共築輝煌的第一步，不是看穿彼此，而是學會尊重的留白。

### 1. 這是什麼（和不是什麼）
單人先導原型，不是標準。1人1次輸入，最長5213ms，注音選字包含在內，不等於焦慮。不是5.2秒標準。

### 2. 核心原則修正
只在本地、預設關閉、不存刪除內容、一鍵清除。api/、Procfile、render.yaml 為舊版雲端遺留，v0.1.1 核心只在本地跑。

### 3. 範圍：只做一件事
寫訊息前的猶豫：「這句要不要傳？」其他領域移至 docs/future_research_ideas.md，未驗證。

### 4. 快速開始
```bash
git clone https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan
python typing_demo.py
```

### 5. 授權 - v0.1.1 已更改
- v0.1.1之後：Polyform Noncommercial 1.0.0，非OSI認可開源，屬 Source-Available 原型，個人研究非營利免費，商用需另購
- v0.1.0之前：仍為MIT，該版本可依MIT條款商用，已揭露
- 商業授權：聽默文創，現階段為原型，建議先聯絡洽談試點合作，預購連結同上

### 6. 下一步需要的證據
多人資料、誤判率、自主感研究

*Powered by Respectful Buffer - Early Prototype - Tingmo Creative - v0.1.1-pilot*
