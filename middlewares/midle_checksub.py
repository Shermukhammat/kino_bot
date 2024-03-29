import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import setting, bot, check_sub, ibuttons, dbuttons, ram


class Bro(BaseMiddleware):
    async def on_pre_process_update(self, update : types.Update,  data: dict):        
        if update.message:
            id = update.message.from_user.id
            buttons = {}
            status = True
            n = 0

            for chanel, url in setting.data['forced_chanels'].items():
                n += 1

                if await check_sub(user_id = id, chanel = chanel):
                    buttons[f"✅ {n}-kanal"] = url 
                else:
                    status = False
                    buttons[f"{n}-kanal"] = url 
        
            # print(status)
            if not status:
                await update.message.answer("Iltimos quydagi kanallarga obuna bo'ling", disable_web_page_preview = True,reply_markup = ibuttons.subscribe_chanels(buttons))
                raise CancelHandler()

        elif update.callback_query:
            id = update.callback_query.from_user.id
            buttons = {}
            status = True
            n = 0

            for chanel, url in setting.data['forced_chanels'].items():
                n += 1
                if await check_sub(user_id = id, chanel = chanel):
                    buttons[f"✅ {n}-kanal"] = url 
                else:
                    status = False
                    buttons[f"{n}-kanal"] = url 

            # print(status)
            if update.callback_query.data == 'check':
                if status:
                    return
            
                else:
                    await update.callback_query.answer("Iltimos hamma kanallarga obuna bo'ling", show_alert = True)
                    raise CancelHandler()
            
            elif status:
                return
            
            else:
                await bot.delete_message(chat_id = id, message_id = update.callback_query.message.message_id)
                await bot.send_message(text = "Iltimos quydagi kanallarga obuna bo'ling", disable_web_page_preview = True, chat_id = id, reply_markup = ibuttons.subscribe_chanels(buttons))
                raise CancelHandler()
        

        

                
