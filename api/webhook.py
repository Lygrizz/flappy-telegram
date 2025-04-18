import json
import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from fastapi import FastAPI, Request
from telegram.ext import Updater, CommandHandler, Dispatcher

TOKEN = os.environ.get("BOT_TOKEN")

app = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="Играть 🕹", web_app=WebAppInfo(url="https://flappy-telegram.vercel.app"))]
    ]
    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Нажми на кнопку, чтобы начать игру:", reply_markup=markup)

app.add_handler(CommandHandler("start", start))

# Для Vercel нужно настроить FastAPI или другие серверные фреймворки
# Пример использования FastAPI
fastapi_app = FastAPI()

@fastapi_app.post("/webhook")
async def handle_webhook(request: Request):
    try:
        body = await request.body()
        update = json.loads(body)
        await app.process_update(Update.de_json(update, app.bot))
        return {"statusCode": 200, "body": "ok"}
    except Exception as e:
        return {"statusCode": 500, "body": f"error: {str(e)}"}

