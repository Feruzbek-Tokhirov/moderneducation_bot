import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.misc import subscription
from loader import bot
from keyboards.inline.check_sub import chek_inline


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs":
                return
        else:
            return

        result = "Чтобы полноценно пользоватся нашим ботом нужно подписатся на наш канал\n"
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"👉 <a href='{invite_link}'>{channel.title}</a>\n")

        if not final_status:
            await update.message.answer(result, reply_markup=chek_inline, disable_web_page_preview=True)
            raise CancelHandler()
