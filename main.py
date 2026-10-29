# main.py v0.1.2 - HONEST PILOT - On-device promise compatible
# Legacy cloud demo - should be moved to legacy_cloud_demo/
# Himeko-YanRuoWeiYan v0.1.1-pilot
# Fix P0: no log content, webhook secret check, rate limit

import os
import logging
import hashlib
import time
from flask import Flask, request, abort
from collections import defaultdict

app = Flask(__name__)

# Setup logger - NEVER log user_message content
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Env
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
WEBHOOK_SECRET = os.getenv("TELEGRAM_WEBHOOK_SECRET", "")  # P0 fix: must set in Render Env
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")

# Simple rate limit: 10 req / 60s per chat_id
rate_limit_store = defaultdict(list)

def is_rate_limited(chat_id: str) -> bool:
    now = time.time()
    window = rate_limit_store[chat_id]
    # clean old
    rate_limit_store[chat_id] = [t for t in window if now - t < 60]
    if len(rate_limit_store[chat_id]) >= 10:
        return True
    rate_limit_store[chat_id].append(now)
    return False

@app.route("/", methods=["GET"])
def health():
    return "Himeko-YanRuoWeiYan v0.1.1-pilot - Legacy Cloud Demo - Suspended Safe Mode", 200

@app.route("/webhook/telegram", methods=["POST"])
def telegram_webhook():
    # P0 fix 1: secret token verification
    secret_header = request.headers.get("X-Telegram-Bot-Api-Secret-Token", "")
    if WEBHOOK_SECRET and secret_header != WEBHOOK_SECRET:
        logger.warning(f"webhook secret mismatch, len={len(secret_header)}")
        abort(403)

    data = request.get_json(silent=True)
    if not data:
        abort(400)

    try:
        message = data.get("message", {})
        chat_id = str(message.get("chat", {}).get("id", "unknown"))
        user_message = message.get("text", "")

        # P0 fix 2: rate limit
        if is_rate_limited(chat_id):
            logger.warning(f"rate limited chat_id_hash={hashlib.sha256(chat_id.encode()).hexdigest()[:8]}")
            return "rate limited", 429

        # P0 fix 3: NEVER log content, only length and hash
        msg_len = len(user_message)
        msg_hash = hashlib.sha256(user_message.encode()).hexdigest()[:12]
        logger.info(f"recv msg_len={msg_len} hash={msg_hash} chat_hash={hashlib.sha256(chat_id.encode()).hexdigest()[:8]}")

        # TODO: Gemini call here - ensure no content logged
        # ...

        return "ok", 200
    except Exception as e:
        logger.error(f"webhook error: {type(e).__name__}")
        return "error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
