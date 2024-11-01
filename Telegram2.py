from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import asyncio

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='button1')],
        [InlineKeyboardButton("Кнопка 2", callback_data='button2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите кнопку:", reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Подтверждаем нажатие кнопки
    if query.data == 'button1':
        await query.message.reply_text("Вы нажали кнопку 1")
    elif query.data == 'button2':
        await query.message.reply_text("Вы нажали кнопку 2")

async def main():
    application = ApplicationBuilder().token("6870674489:AAEZcT-C23VY8AK6o-ktWmwhbQZ1pv6J8fo").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))  # Добавляем обработчик для нажатия кнопок
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
