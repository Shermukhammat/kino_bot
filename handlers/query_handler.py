from aiogram import types
from loader import dp, db, ram, bot, ibuttons



@dp.callback_query_handler()

async def query_handler(query : types.CallbackQuery):
    text = query.data
    id = query.from_user.id
    message_id = query.message.message_id

    if ram.check_user(id):
        if text == 'more':
            await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.more_menu())

        elif text == 'less':
            await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.menu())

    else:
        print(print("Sizniki  utmagan"))