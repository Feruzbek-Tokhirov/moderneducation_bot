import time

from aiogram import types

from data.config import ADMINS

from loader import dp, db, bot
from aiogram.utils import exceptions as aiogram_exceptions


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def all_users(message: types.Message):
    text = ""
    users = db.select_all_users()
    for user in users:
        text += f"Имя: {user[1]}, ID: {user[0]}, email: {user[2]}, язык: {user[3]}\n"
    # print(users[0][0])
    await message.answer(text)


@dp.message_handler(text='/reklama', user_id=ADMINS)
async def reklama(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        print(user_id)
        try:
            await bot.send_message(chat_id=user_id, text="Тяжелая тренировка выжала из тебя все соки? Не беда! Snickers – твой надежный компаньон в достижении спортивных целей. Быстрые углеводы, белки и жиры помогут восстановить силы и подготовиться к новым свершениям. Скушай Snickers, сни, и стань сильнее!")
        except aiogram_exceptions.BotBlocked:
            pass

        # 1 sekund dam olib yuboradi
        # time.sleep(1)


@dp.message_handler(text="/cleardb", user_id=ADMINS)
async def cleardb(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")
