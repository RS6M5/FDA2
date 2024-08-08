import logging
from flask import Flask, request, jsonify
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, CallbackContext
app = Flask(__name__)

TELEGRAM_TOKEN = '7346026260:AAFkDie023ZDmarmPuSk6FsYpdy7Ef-cY4M'
CHAT_ID = '7346026260'  # ID чата или пользователя, куда будут отправляться сообщения
bot = Bot(token=TELEGRAM_TOKEN)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


@app.route('/start', methods=['GET'])
async def start():
    message = f'Welcome to Flower Delivery Bot!:\n'
    bot.send_message(chat_id=CHAT_ID, text=message)
    return jsonify({"status": "success", "message": "Welcome to Flower."})

#    async def order(update: Update, context: CallbackContext) -> None:
#        await update.message.reply_text('Please provide your order details.')

@app.route('/place-order', methods=['POST'])
async def place_order():
    data = request.json
    order_details = data.get('orderDetails', '')
    message = f'Вы оформили заказ:\n{order_details}'

    bot.send_message(chat_id=CHAT_ID, text=message)

    return jsonify({"status": "success", "message": "Order placed successfully."})
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    #main()
    app.run(debug=True)




