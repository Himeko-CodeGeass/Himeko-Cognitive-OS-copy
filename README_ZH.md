# 姬子引擎 - Himeko Cognitive OS

> **人機共築輝煌的第一步，不是看穿彼此，而是學會尊重的留白。**
> *The first step of Human-AI Alignment is not total transparency, but respectful ambiguity.*

**YanRuoWeiYan 言若微言 - 開源認知作業系統協定**

## 1. 為什麼需要姬子？

現在的 AI 都在犯同一個錯：
- **全透明會衝突**：逼你交出所有隱私、情緒，結果你只會更防備
- **全隱藏會孤立**：AI 假裝同理，結果是虛偽的和諧

姬子提出第三條路：**非侵入式意圖完形 + 認知緩衝場**
我們不逼你掏心掏肺，捕捉你的「數位排泄物」：打字暫停、刪除重打的痕跡。把焦慮承接住，但把最終判斷還給你。

## 2. 初代驗證 Demo

`examples/typing_demo.py` 已經驗證：
- 捕捉 >800ms 的猶豫
- 捕捉刪除重打
- 生成 Cognitive Buffer 焦慮分數

這就是 Himeko 的輸入。

## 3. 快速開始

```bash
git clone https://github.com/Himeko-CodeGeass/Himeko-Cognitive-OS
pip install -r requirements.txt
python examples/typing_demo.py
