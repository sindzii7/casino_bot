import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8671858126:AAGtX_9zTSB6IJOVAcNdZAELTwAXZe6p7tc"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопка для открытия красивого интерфейса
    keyboard = [
        [InlineKeyboardButton("🎮 Открыть Rolls", web_app=WebAppInfo(url="https://your-domain.com"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎰 **Нажми кнопку чтобы открыть игру**",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()