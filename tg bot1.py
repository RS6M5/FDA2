import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставьте ваш токен
TELEGRAM_TOKEN = '7346026260:AAFkDie023ZDmarmPuSk6FsYpdy7Ef-cY4M'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome to Flower Delivery Bot!')

async def order(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Please provide your order details.')

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("order", order))

    application.run_polling()

if __name__ == '__main__':
    main()