from aiogram.dispatcher import FSMContext
from loader import types, dp, ram, bot, CHANEL_ID, ibuttons, db, main_states, dbuttons



@dp.message_handler(commands = ['get', 'get2'], state = main_states.set_movi_code)
async def add_movi_code(message : types.Message, state : FSMContext):
    # await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
    admin = ram.get_info(message.from_user.id, admin = True)
    movi_id = message.text.split(' ')[-1]

    if movi_id.isnumeric() and type(admin['action']) == int:
        movi_id = int(movi_id)
        # print(movi_id)
        # print(ram.movies_code.values())
        if movi_id not in ram.movies_code.values():
            if admin['action'] in ram.movies_code.keys():
                ram.movies_code[admin['action']] = movi_id
                db.update_movi_code(movie_id = movi_id, code = admin['action'])

                admin['action'] = None
                await message.answer("Kino yangliandi", reply_markup = dbuttons.movies_code_menu())
            else:
                ram.movies_code[admin['action']] = movi_id
                db.add_movi_code(movie_id = movi_id, code = admin['action'])

                admin['action'] = None
                await message.answer("Kino qo'shildi", reply_markup = dbuttons.movies_code_menu())
        else:
            await message.answer("Bu kino aloqachon qo'shilgan")




@dp.message_handler(commands = 'get2')
async def get_2_handler(message : types.Message):
    await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
    
    seire_id = message.text.split(' ')[-1]
    if seire_id.isnumeric():
        seire_id = int(seire_id)

        if ram.check_user(message.from_user.id):
            seire = ram.movies_dict.get(seire_id)
            if seire:
                saved = db.is_saved(user_id = message.from_user.id, movie_id = seire['id'])
                buttons = ibuttons.movi_buttons(coments_url = seire['coments'], like = seire['like'], dislike = seire['dislike'], saved = saved, admin = False, id = seire_id, serie = True)
        
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = seire['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)
                
        elif ram.check_admin(message.from_user.id):
            seire = ram.movies_dict.get(seire_id)
            if seire:
                saved = db.is_saved(user_id = message.from_user.id, movie_id = seire['id'])
                buttons = ibuttons.movi_buttons(coments_url = seire['coments'], like = seire['like'], dislike = seire['dislike'], saved = saved, admin = True, id = seire_id, serie = True)
        
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = seire['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)


@dp.message_handler(commands = 'get')
async def admin(message : types.Message):
    await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
    
    movi_id = message.text.split(' ')[-1]
    if movi_id.isnumeric():
        movi_id = int(movi_id)
        if ram.check_admin(message.from_user.id):
            if ram.movies_dict.get(movi_id):
                movi = ram.movies_dict[movi_id]

                # state = db.is_like(user_id = message.from_user.id, movie_id = movi['id'])
                saved = db.is_saved(user_id = message.from_user.id, movie_id = movi['id'])
                buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = True, id = movi['id'])
        
                await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)

                
            
        if ram.check_user(message.from_user.id):
            if ram.movies_dict.get(movi_id):
                movi = ram.movies_dict[movi_id]
   

                # state = db.is_like(user_id = message.from_user.id, movie_id = movi['id'])
                saved = db.is_saved(user_id = message.from_user.id, movie_id = movi['id'])
                buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = movi['id'])
        
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
        
    