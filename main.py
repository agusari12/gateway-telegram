from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Bisa juga lewat query

@app.route('/send', methods=['GET'])
def send_message():
    chat_id = request.args.get('chat_id', CHAT_ID)
    text = request.args.get('text')

    if not chat_id or not text:
        return "Missing chat_id or text", 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    r = requests.get(url, params=payload)
    return r.text

if __name__ == '__main__':
    app.run()
