from flask import Flask, request, send_from_directory
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

import os

app = Flask(__name__, static_folder="static")

TOKEN = "8107277857:AAFQcwRAP01SjE9t2UGewMbsfjiNkwoMMKE"  # 🔴 ЗАМЕНИ на свой токен
bot = Bot(TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None)

# Команда /start
def start(update, context):
    update.message.reply_text("Привет! Нажми на кнопку ниже, чтобы поиграть!")
    update.message.reply_game("flappy")  # <-- это название игры в @BotFather /setgame

dispatcher.add_handler(CommandHandler("start", start))

# Telegram Webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

# Главная страница (твоя игра)
@app.route("/")
def serve_game():
    return send_from_directory("static", "index.html")

# Остальные файлы (css, js, картинки)
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)
