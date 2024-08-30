from aiogram.types import Message
from loader import dp
from keyboards.inline.info_keyboard import info_btn
from keyboards.inline.register_keyboard import register_btn


@dp.message_handler(text="ℹ️ Информация про Modern Education")
async def info(msg: Message):
    img = open("static/images/modern_edu.jpg", "rb")
    await msg.answer_photo(photo=img, caption="""1. 📍 Modern Education был открыт недавно, но мы уже имеем много разных филиалов в Ташкенте и в Бухаре

2. 🏢 У каждого человека есть возможность учится у нас, ведь в наших филиалах комнаты бывают просторными и могу вмещать в себя от 30 до 45 человек

3. 👨🏻‍🏫 Репетиторы у нас с большим опытом и стараются преподавать уроки чтобы вся группа могла осилить задания""", reply_markup=info_btn)


@dp.message_handler(text="📋 Что у нас преподаётся")
async def info(msg: Message):
    img = open("static/images/lessons.jpg", "rb")
    await msg.answer_photo(photo=img, caption="""Наши репетиторы преподают множество уроков. Вот некторые из них:
    
1. 🌐 Frontend, Backend
2. 🖥 Строение компьютеров и смартфонов
3. ⚛️ Обществознание (Физика ,Химия, Биология и т.д.)
4. 🤖 Робототехника
5. 🇺🇸 Лингвистика (Английский, Немецкий, Японский и другие)
6. ➕➖ Алгебра и высшая математика""")


@dp.message_handler(text="🎓 Зарегестрироватся в боте как ученик")
async def registration(msg: Message):
    await msg.answer("Через какой тип связи вам удобно общатся ?", reply_markup=register_btn)
