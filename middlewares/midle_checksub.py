import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import setting, bot, check_sub


class Bro(BaseMiddleware):
    async def on_pre_process_update(self, update : types.Update):
        if update.message:
            id = update.message.from_user.id

        elif update.callback_query:
            id =  update.callback_query.from_user.id
        
        else:
            return
        
        logging.info(id)

        nosub_chanels = []
        status = 0
        for chanel in setting.data['forced_chanels']:
            if await check_sub(user_id = id, chanel = chanel):
                status += 1
            else:
                nosub_chanels.append(chanel)

        
        await update.message.answer("Iltimos hamma kanalarga obuna bo'ling", disable_web_page_preview = True)
        raise CancelHandler()

                
