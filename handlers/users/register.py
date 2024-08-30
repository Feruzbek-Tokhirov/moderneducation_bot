# from aiogram import types
# from aiogram.dispatcher import FSMContext
# # from aiogram.dispatcher.filters import Command
# from keyboards.inline.register_keyboard import register_btn
#
# from loader import dp
# from states.personal_data import PersonalData
#
#
# # /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
# @dp.message_handler(text="🎓 Зарегестрироватся в боте как ученик", state=None)
# async def enter_test(message: types.Message):
#     await message.answer("Введите Ф.И.О")
#     await PersonalData.fullName.set()
#
#
# @dp.message_handler(state=PersonalData.fullName)
# async def answer_fullname(message: types.Message, state: FSMContext):
#     fullname = message.text
#
#     await state.update_data(
#         {"name": fullname}
#     )
#
#     await message.answer("Введите свой email")
#
#     # await PersonalData.email.set()
#     await PersonalData.next()
#
#
# @dp.message_handler(state=PersonalData.email)
# async def answer_email(message: types.Message, state: FSMContext):
#     email = message.text
#
#     await state.update_data(
#         {"email": email}
#     )
#
#     await message.answer("Введите номер телефона")
#
#     await PersonalData.next()
#
#
# @dp.message_handler(state=PersonalData.phoneNum)
# async def answer_phone(message: types.Message, state: FSMContext):
#     phone = message.text
#
#     await state.update_data(
#         {"phone": phone}
#     )
#
#     # Ma`lumotlarni qayta o'qiymiz
#     data = await state.get_data()
#     name = data.get("name")
#     email = data.get("email")
#     phone = data.get("phone")
#
#     msg = "Приняты следующие данные:\n"
#     msg += f"Ф.И.О - {name}\n"
#     msg += f"Email - {email}\n"
#     msg += f"Номер телефона: - {phone}\n"
#     await message.answer(msg, reply_markup=register_btn)
#
#     # State dan chiqaramiz
#     # 1-variant
#     await state.finish()
#
#     # 2-variant
#     # await state.reset_state()
#
#     # 3-variant. Ma`lumotlarni saqlab qolgan holda
#     # await state.reset_state(with_data=False)
