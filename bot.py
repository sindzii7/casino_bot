import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8671858126:AAGtX_9zTSB6IJOVAcNdZAELTwAXZe6p7tc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопки
    keyboard = [
        [InlineKeyboardButton("🎮 Играть!", web_app=WebAppInfo(url="https://sindzii7.github.io/casino_bot/"))],
        [InlineKeyboardButton("📢 Канал", url="https://t.me/your_channel")],
        [InlineKeyboardButton("💬 Присоединиться к чату", url="https://t.me/your_chat")],
        [InlineKeyboardButton("🆘 Поддержка", url="https://t.me/klrpl")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Добро пожаловать в 🎉 Prototip!",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()