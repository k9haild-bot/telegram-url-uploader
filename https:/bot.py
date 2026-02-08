from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests
import os

# نجيب التوكن من المتغيرات
TOKEN = os.getenv("BOT8393582046:AAEoeptCCS750RvzyTpbmeqM57IY6Xy5ylI")

async def start(update: Update, context):
    await update.message.reply_text(
        "👋 أهلاً!\nأرسل رابط مباشر وسأحمل الملف لك."
    )

async def download(update: Update, context):
    url = update.message.text
    try:
        response = requests.get(url)
        filename = url.split("/")[-1]

        with open(filename, "wb") as file:
            file.write(response.content)

        await update.message.reply_document(document=open(filename, "rb"))
        os.remove(filename)

    except:
        await update.message.reply_text("❌ حصل خطأ في التحميل")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))

    app.run_polling()

if name == "main":
    main()
