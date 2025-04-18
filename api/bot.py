from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.ext.webhook import WebhookServer

import os
import json
from http.server import BaseHTTPRequestHandler

TOKEN = os.environ.get("8107277857:AAFQcwRAP01SjE9t2UGewMbsfjiNkwoMMKE")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="Играть 🕹", web_app=WebAppInfo(url="https://flappy-telegram.vercel.app"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Нажми на кнопку, чтобы начать игру:", reply_markup=reply_markup)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

async def handler(request):
    body = await request.body()
    update = json.loads(body)
    await app.process_update(Update.de_json(update, app.bot))
    return {
        "statusCode": 200,
        "body": "ok"
    }
