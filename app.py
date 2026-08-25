import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_CHAT_ID")

@app.route("/")
def home():
    return "✅ Bot is running", 200

@app.route("/signal", methods=["POST"])
def signal():
    try:
        data = request.get_json()
        if not data:
            return "No data", 400

        # Отправка сообщения в Telegram
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": ADMIN_ID,
            "text": f"📊 Сигнал:\n{data}"
        }
        response = requests.post(url, json=payload)

        # Логируем ответ Telegram
        print("Telegram response:", response.status_code, response.text)

        if response.status_code == 200:
            return "OK", 200
        else:
            return f"Telegram error: {response.text}", 500

    except Exception as e:
        print("Error:", e)
        return str(e), 500

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
