from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
TOKEN = "6870674489:AAEZcT-C23VY8AK6o-ktWmwhbQZ1pv6J8fo"
google_drive_link_lesson_1 = "https://drive.google.com/file/d/1EJVzhJoRClq3ZfJh2jdLcriErgSx_vHF/view?usp=sharing"
google_drive_link_practice_2 = "https://drive.google.com/file/d/159ubwZNXIyjldfR7SxEnr2z1MABYf02j/view?usp=drive_link"

# Функция стартового сообщения
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Приветственное сообщение (часть 1 и часть 2)
    welcome_message_1 = (
        "Ват-ди в нашей дружной семье упоротых любителей Таиланда. Здесь мы будем учиться читать по-тайски.\n\n"
        "Следующие 50 уроков мы будем учить тайский алфавит и правила чтения, базовые грамматические конструкции. "
        "Это нам поможет ориентироваться в бесконечных тайских закорючках и познать тайский дзен."
    )
    welcome_message_2 = (
        "Каждый урок состоит из теории и практики. Читаем сообщения, выполняем задания, проверяем себя в тесте. "
        "Это всё для вашей самостоятельной свободной работы в том темпе и объёмах, которые нужны именно вам."
    )
    
    # Отправка первой части приветственного сообщения
    await update.message.reply_text(welcome_message_1)
    # Отправка второй части приветственного сообщения
    await update.message.reply_text(welcome_message_2)
    
    # Клавиатура с одной кнопкой "Содержание"
    keyboard = [
        [InlineKeyboardButton("Содержание", callback_data="content")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправка клавиатуры пользователю
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

# Функция для обработки нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "content":
        content_keyboard = [
            [InlineKeyboardButton("Вводное слово", callback_data="intro")],
            [InlineKeyboardButton("Уроки 1-5", callback_data="lessons_1_5")],
            [InlineKeyboardButton("Уроки 6-10", callback_data="lessons_6_10")],
            [InlineKeyboardButton("Уроки 11-15", callback_data="lessons_11_15")],
            [InlineKeyboardButton("Уроки 16-20", callback_data="lessons_16_20")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("Выберите раздел:", reply_markup=reply_markup)

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()