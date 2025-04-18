from fastapi import FastAPI, Request
import json
from telegram import Update
from telegram.ext import Application
import os

TOKEN = os.environ.get("BOT_TOKEN")
print(f"TOKEN: {TOKEN}")
app = Application.builder().token(TOKEN).build()



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
