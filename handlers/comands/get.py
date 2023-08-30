from aiogram.dispatcher import FSMContext
from loader import types, dp, ram, bot, CHANEL_ID, ibuttons, db



@dp.message_handler(commands = 'get2')
async def admin(message : types.Message):
    await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
    
    index = message.text.split(' ')[-1]
    if index.isnumeric():
        index = int(index)
        if ram.check_admin(message.from_user.id):
            movi = db.get_movi(id = index)
            # print(movi)
            if movi:
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'],
                                                                            admin = True,
                                                                            first_state = True,  
                                                                            id = 1, 
                                                                            like = movi['like'], 
                                                                            dislike = movi['dislike']))
                
            
        if ram.check_user(message.from_user.id):
            movi = db.get_movi(id = index)
            if movi:   
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                            first_state = True,  
                                                                            id = 1, 
                                                                            like = movi['like'], 
                                                                            dislike = movi['dislike'],
                                                                            admin = False))


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
            movi = ram.get_movi(index = index)

            state = db.is_like(user_id = message.from_user.id, movie_id = movi['id'])
            saved = db.is_saved(user_id = message.from_user.id, movie_id = movi['id'])
            # print(saved)
            buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], state = state, saved = saved, admin = False, id = movi['id'])
        
            await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)
    # elif len(index) > 1 and index[0] == '#' and index[1:].isnumeric():
    #     index = int(index[1:])
        
    #     if ram.check_user(message.from_user.id) and index < len(ram.top):
    #         movi = ram.top[index]
        
    #         await bot.copy_message(chat_id = message.from_user.id,
    #                                    message_id = movi['id'],
    #                                    from_chat_id = CHANEL_ID,
    #                                    reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
    #                                                                         first_state = True,  
    #                                                                         id = index, 
    #                                                                         like = movi['like'], 
    #                                                                         dislike = movi['dislike'],
    #                                                                         admin = False))

    #     elif ram.check_admin(message.from_user.id):
    #         pass
                          
    