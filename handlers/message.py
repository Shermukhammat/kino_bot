from aiogram.dispatcher import FSMContext
from loader import types, dp, db, ram, bot, dbuttons, ibuttons, my_states, get_movi, movi_add, DISCUSS_CHANEL_ID, main_states
from aiogram.types import InputMediaPhoto


# @dp.message_handler(state = get_movi.get_title)
# async def get_title(message : types.Message, state : FSMContext):
    # id = message.from_user.id

    # ram.update_title(id, message.text)
    # movie = ram.get_movi(id)
    # # await state.set_state(get_movi.get_caption)
    # await bot.send_video(video = movie['video_id'], 
    #                      caption = f"| | o o\nkino nomi: `{message.text}`", 
    #                      chat_id = id,
    #                      reply_markup = ibuttons.change_state(next = 'next2', back = 'back2'))


# @dp.message_handler(state = get_movi.get_caption)
# async def get_caption(message : types.Message, state : FSMContext):
    # id = message.from_user.id

    # ram.update_caption(id, message.text)
    # movie = ram.get_movi(id)

    # await bot.send_video(video = movie['video_id'],
    #                      chat_id = id,
    #                      caption = f"Kino nomi: {movie['title']}\n{movie['caption']}",
    #                      reply_markup = ibuttons.change_state(next = 'next3', back = 'back3'))
    # await message.answer("Kinoga photo caption qo'shishishni xoxlaysizmi?", reply_markup = ibuttons.photo_caption())

    # print(ram.movies[id])    


@dp.message_handler(state = movi_add.set_title)
async def get_title(message : types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text not in ["Ishchi so'zla"]:
            ram.set_title(message.from_user.id, title = message.text, admin = True)

            await state.set_state(movi_add.set_info)
            await bot.send_photo(chat_id = message.from_user.id,
                                 photo = open("./data/pictures/add_movi/ask_input_info.jpg", 'rb'),
                                 caption = "Kino haqida malumot kiritasizmi?",
                                 reply_markup = ibuttons.ask_button(back = 'back_title', admin = True, yes = 'yes_info', skip = 'skip_info'))


@dp.message_handler(state = movi_add.set_info)
async def set_info_message_handler(message: types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text not in ["Ishchi suz"]:
            ram.set_info(id, caption = message.text, admin = True)
            await state.set_state(movi_add.set_thum)
            await bot.send_photo(chat_id = message.from_user.id,
                                 photo = open('./data/pictures/add_movi/ask_thum.jpg', 'rb'), 
                                 caption = "Kinoga caption rasim kirtasizmi?",
                                 reply_markup = ibuttons.ask_button(back = 'back_set_info', admin = True, yes = 'yes_thum', skip = 'skip_thum'))
        

@dp.message_handler(state = main_states.input_avto_movi)
async def input_avto_movi_message_handler(message: types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        admin = ram.get_info(message.from_user.id, admin = True)
        if message.text == "⬅️ Orqaga":
            await state.finish()
            admin['where'] = 'chose_alang'
            await bot.send_photo(chat_id = message.from_user.id,
                                 photo = open('./data/pictures/add_movi/choose_lang.jpg', 'rb'), 
                                 caption = "Kinolarni qaysi tilda kiritmoqchisiz?",
                                 reply_markup = dbuttons.chose_lang())
        
        elif message.text == "🪓 Bekor qilish":
            await state.finish()
            admin['where'] = 'media'
            await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
            


@dp.message_handler()
async def core_message_handler(message : types.Message, state : FSMContext):
    id = message.from_user.id
    
    # chat = await bot.get_chat("@kino_bot_discuss")
    # print(chat.id)

    
    # data = await bot.send_photo(chat_id = DISCUSS_CHANEL_ID,
    #                      photo="https://picsum.photos/200",
    #                      caption = "Yaxshi kino 1")
    
    # print(data.url)
    # await bot.send_video(chat_id = message.from_user.id, video = "http://88.99.56.141/Kinolar/Meg%202%20X%20480p%20O'zbek%20tilida%20(asilmedia.net).mp4")

    if ram.check_user(id):
        # {'name': 'SHermukhammad', 'lang': 'uz', 'where': 'none', 'action': 'none', 'registred': '17.07.2023 13:47'}
        user = ram.get_info(id)
        name = user['name']
        where = user['where']

        if user['where'] == 'none':
            user['where'] = 'head_menu'
            await message.answer(f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = dbuttons.menu())



        elif user['where'] == 'head_menu':
            if message.text == '🎛 Menu':
                await message.answer(f"📓 Bosh menu:\n\nFoydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = ibuttons.menu())


            if user['action'] == 'sign_admin':
                count = ram.bloc_user(id)
                if count <= 2:
                    if message.text == '1234':
                        user['action'] = 'none'
                        ram.registr(id = id, name = user['name'], admin = True)
                        await message.reply("Admin aka ush kelibsiz")
                    else:
                        await message.reply(f"Xato sizda {3 - count} urunish qoldi")
                elif count == 3:
                    if message.text == '1234':
                        user['action'] = 'none'
                        ram.registr(id = id, name = user['name'], admin = True)
                        await message.reply("Admin aka ush kelibsiz ")
                    else:
                        user['action'] = 'none'
                        await message.reply("Ko'd xato bloklanding")
                    
            
    elif ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
        name = admin['name']
        where = admin['where']

        if admin['where'] == 'none':
            admin['where'] = 'head_menu'
            await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = dbuttons.menu(admin = True))



        elif admin['where'] == 'head_menu':
            if message.text == '🎛 Menu':
                await message.answer(f"📓 Bosh menu:\n\nAdmin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = ibuttons.menu())   

            elif message.text == "📂 Media":
                admin['where'] = 'media'
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
        
        elif admin['where'] == 'media':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'head_menu'
                await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = dbuttons.menu(admin = True))
            
            elif message.text == "🎬 Kino qo'shish":
                admin['where'] = 'chose_mtype'
                await bot.send_photo(photo = open('./data/pictures/add_movi/select_input_type.jpg', 'rb'),
                                    chat_id = id,
                                    caption = "Qanday usul bilan kino kiritmoqchisiz?",
                                    reply_markup = dbuttons.chose_movi_input_type())
        
        elif admin['where'] == 'chose_mtype':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'media'
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())

            elif message.text == '♻️ Avtomatik':
                admin['where'] = 'chose_alang'
                await bot.send_photo(chat_id = message.from_user.id,
                                         photo = open('./data/pictures/add_movi/choose_lang.jpg', 'rb'), 
                                         caption = "Kinolarni qaysi tilda kiritmoqchisiz?",
                                         reply_markup = dbuttons.chose_lang())
        
        elif admin['where'] == 'chose_alang':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'chose_mtype'
                await bot.send_photo(photo = open('./data/pictures/add_movi/select_input_type.jpg', 'rb'),
                                    chat_id = id,
                                    caption = "Qanday usul bilan kino kiritmoqchisiz?",
                                    reply_markup = dbuttons.chose_movi_input_type())
            
            elif message.text == "🪓 Bekor qilish":
                admin['where'] = 'media'
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
            
            elif message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Ruscha", "🇬🇧 Inglizcha"]:
                cheet = {"🇺🇿 O'zbekcha" : 'uz', "🇷🇺 Ruscha" : 'ru', "🇬🇧 Inglizcha" : 'en'}
                ram.admin_movies_set_lang(lang = cheet[message.text], admin_id = message.from_user.id)

                await state.set_state(main_states.input_avto_movi)
                await bot.send_photo(chat_id = message.from_user.id,
                                     photo = open('./data/pictures/add_movi/send_movi.jpg', 'rb'), 
                                     caption = "Kinolaringzni tashlang",
                                     reply_markup = dbuttons.avto_input_movi_menu())

    else:
        pass


# @dp.message_handler(state = [])
