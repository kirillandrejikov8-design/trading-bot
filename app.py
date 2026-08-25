import os
from flask import Flask, request
import requests

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
        if data:
            msg = f"📊 Сигнал:\n{data}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            payload = {"chat_id": ADMIN_ID, "text": msg}
            requests.post(url, json=payload)
            return "OK", 200
        return "No data", 400
    except Exception as e:
        return str(e), 500

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
