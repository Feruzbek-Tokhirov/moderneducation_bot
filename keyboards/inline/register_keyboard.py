from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

register_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Через Электронную почту", callback_data="from_email")
        ]
    ]
)
