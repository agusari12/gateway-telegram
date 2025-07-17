import os
import requests
from flask import Flask, request

app = Flask(__name__)

botToken = os.getenv("BOT_TOKEN")
chatId = os.getenv("CHAT_ID")

@app.route('/kirim', methods=['POST'])
def kirim_pesan():
    data = request.json
    message = data.get("message", "")
    url = f"https://api.telegram.org/bot{botToken}/sendMessage"
    payload = {
        "chat_id": chatId,
        "text": message
    }
    response = requests.post(url, json=payload)
    return {"status": "ok", "telegram_response": response.json()}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
