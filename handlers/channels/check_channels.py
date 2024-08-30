from loader import dp, bot
from aiogram import types
from data.config import CHANNELS
from utils.misc import subscription


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> Вы попдписались на канал, теперь можете пользоватся ботом!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> Вы не подписаны на канал. "
                       f"<a href='{invite_link}'>Подпишитесь</a>\n\n")

    await call.message.answer(result, disable_web_page_preview=True)
