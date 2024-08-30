from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ℹ️ Информация про Modern Education")
        ],
        [
            KeyboardButton(text="📋 Что у нас преподаётся"),
            KeyboardButton(text="🎓 Зарегестрироватся в боте как ученик")
        ]
    ],
    resize_keyboard=True
)
