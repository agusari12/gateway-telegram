from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/send", methods=["POST"])
def send_to_telegram():
    try:
        data = request.get_json()

        chat_id = data.get("chat_id")
        text = data.get("text")

        if not chat_id or not text:
            return jsonify({"status": "error", "message": "chat_id dan text wajib"}), 400

        payload = {
            "chat_id": chat_id,
            "text": text
        }

        response = requests.post(TELEGRAM_API_URL, json=payload)
        return jsonify({"status": "success", "telegram_response": response.json()})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
