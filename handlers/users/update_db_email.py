from aiogram import types
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.builtin import Command
from loader import dp, db
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text="from_email")
async def bot_start(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свою электронную почту")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    db.update_user_email(email=email, id=message.from_user.id)
    user = db.select_user(id=message.from_user.id)
    await message.answer(f"Ваша электронная почта получена. Ожидайте ответа в своём email! (Если вы ввели неправильную почту то просто нажмите кнопку ещё раз и тогда ваша почта обновится)")
    await state.finish()
