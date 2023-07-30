from aiogram.dispatcher import FSMContext
from loader import types, dp, db, ram, bot, dbuttons, ibuttons, my_states, get_movi



@dp.message_handler(state = get_movi.get_title)
async def get_title(message : types.Message, state : FSMContext):
    id = message.from_user.id

    ram.update_title(id, message.text)
    movie = ram.get_movi(id)
    # await state.set_state(get_movi.get_caption)
    await bot.send_video(video = movie['vide_id'], 
                         caption = f"| | o o\nkino nomi: `{message.text}`", 
                         chat_id = id,
                         reply_markup = ibuttons.change_state())


@dp.message_handler(state = get_movi.get_caption)
async def get_caption(message : types.Message, state : FSMContext):
    id = message.from_user.id

    ram.update_caption(id, message.text)
    movie = ram.get_movi(id)

    await bot.send_video(video = movie['vide_id'],
                         chat_id = id,
                         caption = f"Kino nomi: {movie['title']}\n{movie['caption']}\nKinoga phot caption qo'shishni xolaysizmi?",
                         reply_markup = ibuttons.photo_caption())
    # await message.answer("Kinoga photo caption qo'shishishni xoxlaysizmi?", reply_markup = ibuttons.photo_caption())

    # print(ram.movies[id])    




@dp.message_handler()
async def core_message_handler(message : types.Message):
    id = message.from_user.id

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
                # await message.answer(f"{admin['name']} qanday usul bilan kino kiritmoqchisiz?", reply_markup = ibuttons.input_movi())

                await bot.send_photo(chat_id = id, photo = open('./data/pictures/2.jpg', 'rb'), caption = f"{admin['name']} qanday usul bilan kino kiritmoqchisiz?", reply_markup = ibuttons.ask_movi_input())

            

    else:
        pass
    