import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import start_buttons
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!", reply_markup=start_buttons)
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer("Добро пожаловать!")
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} добавлен в базу данных.\nВ базе данных {count} пользователей."
    await bot.send_message(chat_id=ADMINS[0], text=msg)


# @dp.message_handler(IsPrivate(), CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Здравствуйте, {message.from_user.full_name}!", reply_markup=start_buttons)
