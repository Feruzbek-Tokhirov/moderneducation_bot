from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


info_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Наш сайт", url="http://moderneducation.uz.tilda.ws/lessons_uz")
        ],
        [
            InlineKeyboardButton(text="Менеджер", url="https://t.me/feruztokhirov")
        ]
    ]
)
