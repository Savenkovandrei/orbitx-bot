import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌌 Привет! Я Orbit Lab — ваш цифровой спутник.\n"
        "Напишите что-нибудь, и я повторю. Или воспользуйтесь командами."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧪 Доступные команды:\n"
        "/start — начать\n"
        "/help — справка\n\n"
        "Просто отправьте текст — я отвечу!"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔁 Вы написали:\n{update.message.text}")

def main():
    # 🔑 Токен от @BotFather
    TOKEN = "8114259362:AAG7I3I3_nResUvgc7cNTXklnnZLJRJ3tZM"
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("🚀 Orbit Lab запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
