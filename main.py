from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8033826325:AAG9vBAOphBkpuoFOjm25fuNtZ7D5sY38Lo"

@app.route('/')
def index():
    return "Gateway Telegram aktif!"

@app.route('/send', methods=['GET', 'POST'])
def send():
    chat_id = request.args.get('chat_id') or request.json.get('chat_id')
    text = request.args.get('text') or request.json.get('text')

    if not chat_id or not text:
        return {"status": "error", "message": "Missing chat_id or text"}, 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, json=payload)
    return {"status": "ok", "telegram_response": r.json()}
