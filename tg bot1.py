import logging
from flask import Flask, request, jsonify
from telegram import Bot

app = Flask(__name__)

TELEGRAM_TOKEN = '7346026260:AAFkDie023ZDmarmPuSk6FsYpdy7Ef-cY4M'
CHAT_ID = '7346026260'  # ID чата или пользователя, куда будут отправляться сообщения
bot = Bot(token=TELEGRAM_TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

@app.route('/place-order', methods=['POST'])
def place_order():
    data = request.json
    order_details = data.get('orderDetails', '')
    message = f'Вы оформили заказ:\n{order_details}'

    bot.send_message(chat_id=CHAT_ID, text=message)

    return jsonify({"status": "success", "message": "Order placed successfully."})

if __name__ == '__main__':
    app.run(debug=True)