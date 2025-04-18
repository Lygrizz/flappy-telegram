from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8107277857:AAFQcwRAP01SjE9t2UGewMbsfjiNkwoMMKE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="Запустить игру 🕹", web_app=WebAppInfo(url="https://flappy-telegram.vercel.app"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Нажми на кнопку, чтобы начать играть:", reply_markup=reply_markup)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_webhook(
        listen="0.0.0.0",
        port=8000,
        webhook_url=f"https://flappy-telegram.vercel.app/{TOKEN}"
    )
