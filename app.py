import os
import logging
from flask import Flask, request
import telegram

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN не задан. Установите в Render Environment.")
if not ADMIN_CHAT_ID:
    raise RuntimeError("ADMIN_CHAT_ID не задан. Установите в Render Environment.")

app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)

@app.route("/")
def home():
    return "Bot is running!", 200

@app.route("/signal", methods=["POST"])
def signal():
    try:
        data = request.get_json()
        if data:
            logger.info(f"Получен сигнал: {data}")
            bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"📊 Сигнал:\n{data}")
            return "OK", 200
        return "No data", 400
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return "Error", 500

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
