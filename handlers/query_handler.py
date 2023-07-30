from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, bot, ibuttons, dbuttons, my_states, get_movi



@dp.callback_query_handler(state = get_movi.get_video)
async def get_video_query(query : types.CallbackQuery, state : FSMContext):
    id = query.from_user.id

    if query.data == 'delet':
        await bot.delete_message(chat_id = id, message_id = query.message.message_id)
    
    elif query.data == 'next':
        await state.set_state(get_movi.get_title)
        await bot.send_message(text = "Endi esa kino nomni kiriting", chat_id = id)
    


@dp.callback_query_handler(state = get_movi.get_title)
async def get_tile_quer(query : types.CallbackQuery, state : FSMContext):
    id = query.from_user.id
    if query.data == 'delet':
        await bot.delete_message(chat_id = id, message_id = query.message.message_id)
    
    elif query.data == 'next':
        await state.set_state(get_movi.get_caption)
        await bot.send_message(chat_id = id, text = "Ok endi kinoga caption kiriting")
    
    elif query.data == 'back':
        await state.set_state(get_movi.get_video)
        await bot.send_message(chat_id = id, text = "Ok Kinoyingzni videyosni tashlang")
    


@dp.callback_query_handler(state = get_movi.get_caption)

async def get_caption_query(query : types.CallbackQuery, state : FSMContext):
    text = query.data
    id  = query.from_user.id
    message_id = query.message.message_id

    # if text == 'yes':
    #     await state.set_state(get_movi.get_caption_photo)
    #     await bot.send_message(text = "OK, endi caption photoni tashlang", chat_id = id)

    # elif text == 'no':
    #     await query.answer( "Ok, unda videoni caption photosidan foydalanaman!")
    #     await bot.edit_message_reply_markup(chat_id = id, 
    #                                         message_id = query.message.message_id, 
    #                                         reply_markup = ibuttons.add_movi())

    # elif text == 'delet':
    #     await bot.delete_message(chat_id = id, message_id = message_id)
    
    # elif text == 'add':
    #     await query.answer("Kino qo'shildi :)")
    #     print("Ushladim")
    
    # elif text == 'back':
    #     await state.set_state(get_movi.get_title)
    #     movie = ram.get_movi(id)

    #     await bot.send_video(video = movie['vide_id'],
    #                      chat_id = id,
    #                      caption = f"Kino nomi: {movie['title']}\n{movie['caption']}\nKinoga phot caption qo'shishni xolaysizmi?",
    #                      reply_markup = ibuttons.photo_caption())
    

    
       


@dp.callback_query_handler()

async def query_handler(query : types.CallbackQuery, state : FSMContext):
    text = query.data
    id = query.from_user.id
    message_id = query.message.message_id

    if ram.check_user(id):
        if text == 'more':
            await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.more_menu())

        elif text == 'less':
            await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.menu())
    
    # elif ram.check_admin(id):
    #     if text == 'more':
    #         await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.more_menu(admin = True))

    #     elif text == 'less':
    #         await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.menu())
    
    
    elif ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
        name = admin['name']
        where = admin['where']

        if admin['where'] == 'none':
            admin['where'] = 'head_menu'
            # await query.answer(f"Bosh menu", reply_markup = dbuttons.menu(admin = True))
            await bot.send_message(text = "salom", chat_id = id, reply_markup = dbuttons.menu(admin = True))

        # elif admin['where'] == 'head_menu':
        #     pass

        elif admin['where'] == 'media':
            if text == 'delet':
                await bot.delete_message(chat_id = id, message_id = message_id)

            elif text == 'hand':
                await state.set_state(get_movi.get_video)
                await bot.send_message(text = "Ok, Kinoyingzni  tashlang!", chat_id = id)

    else:
        print(print("Sizniki  utmagan"))