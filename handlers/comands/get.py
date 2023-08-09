from aiogram.dispatcher import FSMContext
from loader import types, dp, ram, bot, CHANEL_ID, ibuttons


@dp.message_handler(commands = 'get')
async def admin(message : types.Message):
    index = message.text.split(' ')[-1]
    # print(index)
    if index.isnumeric() and int(index) <= len(ram.movies):
        movi = ram.movies[int(index)]
        
        await bot.copy_message(chat_id = message.from_user.id,
                               message_id = movi['id'],
                               from_chat_id = CHANEL_ID,
                               reply_markup = ibuttons.movi_buttons(url = movi['coments']))
        