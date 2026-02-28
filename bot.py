import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "8671858126:AAGtX_9zTSB6IJOVAcNdZAELTwAXZe6p7tc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем меню как на фото
    keyboard = [
        [InlineKeyboardButton("🎮 Играть!", web_app=WebAppInfo(url="https://sindzii7.github.io/casino_bot/"))],
        [InlineKeyboardButton("📢 Канал", url="https://t.me/your_channel")],
        [InlineKeyboardButton("💬 Присоединиться к чату", url="https://t.me/kgfdkg3")],
        [InlineKeyboardButton("💰 Пополнить инвентарь", callback_data="deposit")],
        [InlineKeyboardButton("📊 Маркетинг", callback_data="marketing")],
        [InlineKeyboardButton("🆘 Обратиться в поддержку", url="https://t.me/klrpl")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🎉 Добро пожаловать в Prototip, {update.effective_user.first_name}!\n\n"
        f"🎡 Играй • 💬 Общайся • 🛠 Поддержка",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "deposit":
        await query.edit_message_text("💰 Пополнение появится скоро!")
    elif query.data == "marketing":
        await query.edit_message_text("📊 Маркетинг в разработке")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()