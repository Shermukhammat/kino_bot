from aiogram.dispatcher import FSMContext
from loader import types, dp, ram, bot, CHANEL_ID, ibuttons


@dp.message_handler(commands = 'get')
async def admin(message : types.Message):
    await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
    
    index = message.text.split(' ')[-1]
    if index.isnumeric():
        index = int(index)
        if ram.check_admin(message.from_user.id):
            if index <= len(ram.movies):
                movi = ram.movies[index]
        
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'],
                                                                            admin = True,
                                                                            first_state = True,  
                                                                            id = index, 
                                                                            like = movi['like'], 
                                                                            dislike = movi['dislike']))
                
            
        if ram.check_user(message.from_user.id):
            if index <= len(ram.movies):
                movi = ram.movies[index]
        
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                            first_state = True,  
                                                                            id = index, 
                                                                            like = movi['like'], 
                                                                            dislike = movi['dislike'],
                                                                            admin = False))
        