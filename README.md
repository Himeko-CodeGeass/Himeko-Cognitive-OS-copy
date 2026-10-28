# Himeko-YanRuoWeiYan
## YanRuoWeiYan 言若微言 - 開源認知作業系統協定

人機共築輝煌的第一步，不是看穿彼此，而是學會尊重的留白。
The first step of Human-AI Alignment is not to see through each other, but to learn respectful blank space.

[License: MIT](https://opensource.org/licenses/MIT) | [Release: v0.1.0](https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan) | [Protocol: YanRuoWeiYan](https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan)

### 1. 初代驗證 - 真實數據 (2026-10-27)
不是理論，是真實捕捉的 digital exhaust

```json
{
  "meta": {
    "version": "himeko-cognitive-os v0.1.0",
    "mode": "Non-Invasive Intent Gestalt"
  },
  "typing_pauses": [
    {"duration_ms": 1035, "context_tail": "_我要"},
    {"duration_ms": 1658, "context_tail": "要過"},
    {"duration_ms": 2168, "context_tail": "要過嗎"},
    {"duration_ms": 5213, "context_tail": "要過嗎_"}
  ],
  "revision_patterns": [
    "PAUSE: 停頓 5213ms at \要過嗎\_",
    "DELETE: 刪除 2 字 \要過嗎\ → \要\",
    "DELETE: 刪除 1 字 \要<< ㄇ\ → \要過嗎"
  ],
  "deletion_count": 4,
  "longest_pause_ms": 5213,
  "anxiety_score": 60,
  "cognitive_buffer_field": {
    "state": "absorbing",
    "label": "承接焦慮中... Absorbing anxiety."
  },
  "intent_gestalt": "hesitation_detected -> 不逼問"
}
```

**解讀：**
捕捉到 4 次猶豫，最長 5.2 秒
捕捉到 4 次刪除重打，完整重寫意圖軌跡
焦慮分數 60% → 進入 absorbing 承接狀態
沒有跳出視窗問「你在想什麼？」，只留白 - 這就是言若微言
這段 JSON 就是 core/ 引擎的正式輸入，初代閉環已通

### 2. 為什麼需要姬子？
現在的 AI 都在犯同一個錯：
- 全透明會衝突：逼你交出所有隱私，結果你更防備
- 全隱藏會孤立：假裝同理，結果是虛偽的和諧
- **姬子提出第三條路：非侵入式意圖完形 + 認知緩衝場**
- 捕捉「數位排泄物」：打字暫停、刪除重打，把焦慮承接住，把選擇還給人

### 3. 核心架構
- `core/` - Intent Gestalt 引擎
- `api/` - Protocol 層，可接 LINE / Slack / Notion
- `examples/typing_demo.py` - 初代驗證 Demo（已驗證）
- `tests/` - 對齊測試

### 4. 快速開始
```bash
git clone https://github.com/Himeko-CodeGeass/Himeko-YanRuoWeiYan
cd Himeko-YanRuoWeiYan
python typing_demo.py
```

### 5. 授權
MIT License - 個人、開源免費，商用未來將採 Dual License

### 6. 路線圖
- ✅ v0.1.0 YanRuoWeiYan - 初代驗證完成 (2026-10-28)
- 🚧 v0.2.0 接上 Notion 五中樞 - Potential + Fixed + Ongoing
- 🔜 v1.0.0 協定授權開放 - Protocol Licensing

### 7. 💰 Commercial License - 聽默文創 Tingmo Creative

**Personal / Open-source: MIT License - Free**
個人專案、研究、開源專案免費使用。

**Commercial: 商業授權 NT$32,000 / ~$999 USD**
在你的閉源商業產品中使用 YanRuoWeiYan Protocol，無需開源你的程式碼。

包含：
- Commercial use of Intent Gestalt (5213ms hesitation capture) + Cognitive Buffer Field
- Includes anxiety_score, absorbing state, intent_gestalt engine
- Support for Notion 5 hubs integration
- Email support + 商業授權證書 LICENSE-COMMERCIAL.txt

👉 **Buy Commercial License:**
https://tingmocreative.lemonsqueezy.com/checkout/buy/5d845d7e-6c55-4b27-9481-d06c62c776ff

購買後自動收到授權檔 + Tingmo Creative 發票。
After purchase, you will receive LICENSE-COMMERCIAL.txt + invoice automatically.

Contact: jizheng.contact@proton.me
Store: https://tingmocreative.lemonsqueezy.com

*Powered by Respectful Ambiguity Protocol - The 5.2s standard - 由聽默文創 Tingmo Creative 營運*
