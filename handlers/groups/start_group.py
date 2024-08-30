from aiogram.types import Message
from loader import dp
from filters.group_filter import IsGroup


@dp.message_handler(IsGroup(), commands="start")
async def start_g(msg: Message):
    await msg.reply("""Если вы добавли бота в группу значит эта группа учеников и учителя. 
    С помощью этого бота учитель или его помошник может заблокировать или остановить чат для одного или несеольких учеников""")
