from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот працює! ✅")

if __name__ == "__main__":
    app = ApplicationBuilder().token("ТУТ_ВСТАВ_СВІЙ_ТОКЕН").build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()7713368381:AAH-Hz4aZrpo5MvT8-9w8Zd_stBpILgsuUA
