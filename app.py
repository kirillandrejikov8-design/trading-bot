import os
from flask import Flask, request
import telegram

TOKEN = os.environ.get("TELEGRAM_TOKEN")
ADMIN = os.environ.get("ADMIN_CHAT_ID")

app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)

@app.route("/")
def home():
    return "Bot is running", 200

@app.route("/signal", methods=["POST"])
def signal():
    data = request.get_json()
    if data:
        bot.send_message(chat_id=ADMIN, text=f"📊 Сигнал: {data}")
    return "OK", 200

if __name__ == "__main__":
     port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=10000)
    
