from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего бота
TOKEN = "6870674489:AAEZcT-C23VY8AK6o-ktWmwhbQZ1pv6J8fo"
google_drive_link_lesson_1 = "https://drive.google.com/file/d/159ubwZNXIyjldfR7SxEnr2z1MABYf02j/view?usp=drive_link"

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
        reply_markup = InlineKeyboardMarkup(content_keyboard)
        await query.edit_message_text("Содержание:", reply_markup=reply_markup)
    
    elif query.data == "lessons_1_5":
        lessons_keyboard = [
            [InlineKeyboardButton("Урок 1", callback_data="lesson_1")],
            [InlineKeyboardButton("Урок 2", callback_data="lesson_2")],
            [InlineKeyboardButton("Урок 3", callback_data="lesson_3")],
            [InlineKeyboardButton("Урок 4", callback_data="lesson_4")],
            [InlineKeyboardButton("Урок 5", callback_data="lesson_5")],
            [InlineKeyboardButton("Назад", callback_data="content")]
        ]
        reply_markup = InlineKeyboardMarkup(lessons_keyboard)
        await query.edit_message_text("Уроки 1-5:", reply_markup=reply_markup)

    elif query.data == "lesson_1":
        lesson_1_messages = [
            "Урок №1\n\nПервые на очереди у нас сонорные согласные. Они все низкого класса.",
            "[n]  น ณ\nЗвук [n] в начале слога обозначается двумя буквами низкого класса: น [nͻͻ] หนู [nǔu] (мышка) и ณ [nͻͻ] เณร [neen] (буддийский послушник). Таким же образом эти буквы будут читаться и на конце слога. Позже мы увидим, какие согласные будут менять своё чтение и подстраиваться под звук [n].\n\nТайский звук [n] чуть мягче русского, близок к английскому. При произнесении тайского звука кончик языка не должен касаться верхних зубов, но должен упираться в твёрдое нёбо за ними. Примеры тайских слов: นอน [nɔɔn] (спать), หนาว [nǎao] (холодный). Попробуй послушать их в гугле или на Forvo. ",
            "[[m]  ม\nЗвук [m] в начале и конце слога обозначается буквой низкого класса — ม [mͻͻ] ม้า [máa] (лошадь). Этот звук мы встретим в таких тайских словах ไม่ [mâi] (не), มี [mii] (иметь), มา [maa] (приходить). Он аналогичен русской «м».",
            "[l]  ล ฬ\nЗвук [л] в начале слога в тайском языке обозначается двумя буквами: ล [lͻͻ] ลิง [ling] (обезьяна) и ฬ [lͻͻ] จุฬา [jù laa] (воздушный змей). Тайский звук «л» чуть мягче, чем русский. При его произношении язык не должен касаться верхних зубов, он должен упираться в нёбо за ними. В тайском языке его можно услышать в словах เล็ก [lék] (маленький) или ลืม [lʉʉm] (забывать).\n\nНа конце слога ล и ฬ меняют своё чтение! Когда ล и ฬ закрывают слог, то произносится звук [n]. ",
            "[r]  ร\n Звук [r] обозначается буквой ร [rͻͻ] เรือ [rʉa] (лодка). Подобный звук мы встретим в словах โรงแรม [roong rɛɛm] (гостиница) и รู้ [rúu] (знать). \n\nНа конце слога буква ร [rͻͻ] เรือ [rʉa] меняет своё чтение! Когда ร закрывает слог, она произносится как [n].",
            "Теперь возьмём пару гласных, чтобы скучно не было. Начнём с долгих. Их надо старательно тянуть.\n\nЗвук [aa] обозначается в тайском языке с помощью буквы สระอา [sà rà aa ] — -า. Эта гласная ставится справа от согласной, после которой читается.\nНапример: มา [maa ] или นา [naa]\n\nЗвук [ii] обозначается с помощью буквы สระอี [sà rà ii] —ี, которая ставится над согласной, после которой читается.\nНапример: มี [mii ] или ลี [lii]",
        ]
        for message in lesson_1_messages:
            await query.message.reply_text(message)

        practice_keyboard = [[InlineKeyboardButton("Вперёд!", callback_data="practice_1")]]
        reply_markup = InlineKeyboardMarkup(practice_keyboard)
        await query.message.reply_text("Переходим к практике:", reply_markup=reply_markup)
    
    elif query.data == "practice_1":
        practice_messages = [
            "✍️ Прописи прописываем. Можешь распечатать себе, можешь просто в тетради аккуратно всё прописать."
        ]
        for message in practice_messages:
            await query.message.reply_text(message)
        
        # Отправка ссылки на файл
        await query.message.reply_text(
            f"Cкачай файл с прописями c Google Drive: [Скачать файл]({google_drive_link_lesson_1})",
            parse_mode="Markdown"
        )
        
        await query.message.reply_text("🧑‍💻 Тест проходим")
        
        quiz_keyboard = [[InlineKeyboardButton("Начали!", url="t.me/QuizBot?start=UQSwXVxU")]]
        await query.message.reply_text("Пройди тест:", reply_markup=InlineKeyboardMarkup(quiz_keyboard))

        nav_keyboard = [
            [InlineKeyboardButton("Содержание", callback_data="content"), InlineKeyboardButton("Урок 2", callback_data="lesson_2")]
        ]
        await query.message.reply_text("К следующему уроку:", reply_markup=InlineKeyboardMarkup(nav_keyboard))

    # Добавим ветки для других кнопок
# Главная функция для запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()