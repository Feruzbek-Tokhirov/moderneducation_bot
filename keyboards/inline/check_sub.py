from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


chek_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="☑️ Проверить подписку", callback_data="check_subs")
        ]
    ]
)
