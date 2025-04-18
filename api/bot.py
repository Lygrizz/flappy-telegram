import json
import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("8107277857:AAFQcwRAP01SjE9t2UGewMbsfjiNkwoMMKE")

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="Играть 🕹", web_app=WebAppInfo(url="https://flappy-telegram.vercel.app"))]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Нажми на кнопку, чтобы начать игру:", reply_markup=markup)

app.add_handler(CommandHandler("start", start))

# Vercel вызывает эту функцию
async def handler(request):
    try:
        body = await request.body()
        update = json.loads(body)
        await app.process_update(Update.de_json(update, app.bot))
        return {
            "statusCode": 200,
            "body": "ok"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"error: {str(e)}"
        }
