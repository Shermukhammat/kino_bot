from aiogram.dispatcher import FSMContext
from loader import types, dp, db, ram, bot, dbuttons, ibuttons, movi_add, DISCUSS_CHANEL_ID, main_states, CHANEL_ID, info_cleaner, title_finder, setting, check_sub
from aiogram.types import InputMediaPhoto
import asyncio
from random import randint 
from aiogram  import Bot
import re
import time
import asyncio


@dp.message_handler(content_types=types.ContentType.STICKER)
async def catch_sticer(message : types.Message):
    print(message.sticker.file_id)
    await bot.send_sticker(chat_id = message.from_user.id, sticker = message.sticker.file_id)

@dp.message_handler(state = main_states.input_video_manual)
async def input_manual_video_message(message : types.Message, state : FSMContext):

    if message.text == "⬅️ Orqaga":
        await state.finish()

        admin = ram.get_info(message.from_user.id, admin = True)
        admin['where'] = 'manual_m'
        await message.answer("qo'lanma menyusi", reply_markup = dbuttons.manual_edit())

    elif message.text == "🏠 Bosh sahifa":
        await state.finish()

        admin = ram.get_info(message.from_user.id, admin = True)
        admin['where'] = 'head_menu'
        await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", 
                                    reply_markup = dbuttons.menu(admin = True))


@dp.message_handler(state = main_states.input_series_part)
async def input_series_part_mesage(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(main_states.input_serie_info)
        await message.answer("Endi esa kino haqida caption photo bilan kino haqida malumot kiriting!", reply_markup = dbuttons.back())

    elif message.text == "🧩 Oldingi qism":
        if ram.input_series.get(message.from_user.id):
            last = ram.input_series[message.from_user.id]['last_part']
            if last <= 1:
                ram.input_series[message.from_user.id]['last_part'] = None
                await message.answer("Iltimos 1-qismni kiriting")
            else:
                ram.input_series[message.from_user.id]['last_part'] -= 1
                await message.answer(f"Iltimos {ram.input_series[message.from_user.id]['last_part'] + 1}-qismni  kiriting")
    
    elif message.text == "🗑♻️ Tozalash":
        if ram.input_series.get(message.from_user.id):
            ram.input_series[message.from_user.id]['last_part'] = None
            ram.input_series[message.from_user.id]['parts_id'] = {}

            await message.answer("Xamma qismlar o'chrildi! 1-qismni tashlang")
    
    elif message.text ==  "🏠 Bosh sahifa":
        await state.finish()
        admin = ram.get_info(message.from_user.id, admin = True)
        admin['where'] = 'head_menu'

        await message.answer(f"Bosh menu", reply_markup = dbuttons.menu(admin = True))

    elif message.text == "💾♻️ Saqlash":
        await state.finish()
        user_id = message.from_user.id
        data = ram.input_series[user_id] #['title']


        # Sort parts
        parts_id = [id for id in data['parts_id'].values()]
        parts_id.sort()
        
        sorted_part = {}
        n = 0
        for id in parts_id:
            n += 1
            sorted_part[n] = id
        
        data['parts_id'] = sorted_part 

        if data['caption'] == None:
            data['caption'] = data['title']

        # print(data)
        await message.answer("Seriyal yuklanishi boshland")

        #Back media menu
        admin = ram.get_info(message.from_user.id, admin = True)
        admin['where'] = 'media'
        await message.answer("Media menyusi", reply_markup = dbuttons.media())
        

        
        

        # Make coments
        coment = await bot.send_photo(chat_id = DISCUSS_CHANEL_ID, 
                                      photo = data['thumb'], 
                                      caption = data['caption'] + "\n\n" + setting.data['bot_url'])

        coment_url = coment.url


        # Send movi info to data CHANEL
        mes_data = await bot.send_photo(chat_id = CHANEL_ID, 
                                      photo = data['thumb'], 
                                      caption = data['caption'] + "\n\n" + setting.data['bot_url'])
        
        
        # Copy parts to data CHANEL print
        part = {'uz' : ' - qisim', 'ru' : 'часть', 'en' : 'episode'}
        parts_id = {}

        n = 0
        for part_num, part_id in data['parts_id'].items():
            n += 1
            if n > 18:
                await message.answer("Qismlar soni 18 tadan oshib ketdi 1 daqialik uyqu rejimi yoqildi")
                await asyncio.sleep(60) 
                await message.answer("Yuklash boshlandi")
                n = 0
            
            part_data = await bot.copy_message(chat_id = CHANEL_ID, 
                                               from_chat_id = user_id,
                                               message_id = part_id, 
                                               caption = f"{data['title']} {part_num} {part.get(data['lang'])}")
            
            parts_id[part_num] = part_data.message_id

        
        # Save data to database
        db.add_seri(title = data['title'], 
                    message_id = mes_data.message_id,
                    coment_url = coment_url,
                    thumb = data['thumb'],
                    lang = data['lang'],
                    parts_id = parts_id)
        
        # Add serie to ram
        seri =  {'id' : mes_data.message_id,
                     'title' : data['title'], 
                     'like' : 0,
                     'dislike' : 0,
                     'coments' : coment_url,
                     'thum_url' : data['thumb'],
                     'parts_id' : parts_id,
                     'lang' : data['lang'],
                     'type' : 'seri'}
        ram.movies_dict[id] = seri
        
        


@dp.message_handler(state = main_states.input_serie_info)
async def input_seroie_info(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.set_state(main_states.input_serie_title)
        await message.answer("Seriyal nomini kiriting", reply_markup = dbuttons.back())
    
    elif message.text ==  "🏠 Bosh sahifa":
        await state.finish()
        admin = ram.get_info(message.from_user.id, admin = True)
        admin['where'] = 'head_menu'

        await message.answer(f"Bosh menu", reply_markup = dbuttons.menu(admin = True))
    


@dp.message_handler(state = main_states.input_serie_title)
async def get_series_title(message : types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text == "⬅️ Orqaga":
            await state.set_state(main_states.input_serie_lang)
            await message.answer("Seriyal tilni tanlang", reply_markup = dbuttons.chose_lang())

        else:
            ram.series_set_title(id = message.from_user.id, title = message.text)
            await state.set_state(main_states.input_serie_info)
            await message.answer("Endi esa kino haqida caption photo bilan kino haqida malumot kiriting!", reply_markup = dbuttons.back())


@dp.message_handler(state = main_states.input_serie_lang)
async def get_serie_lang(message : types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Ruscha", "🇬🇧 Inglizcha"]:
            lang = {"🇺🇿 O'zbekcha" : 'uz', "🇷🇺 Ruscha" : 'ru', "🇬🇧 Inglizcha" : 'en'}[message.text]
            ram.creat_serie(lang = lang, id = message.from_user.id)

            await state.set_state(main_states.input_serie_title)
            await message.answer("Ok endi seriyal nomini kiriting", reply_markup = dbuttons.back())
            
        elif message.text == "⬅️ Orqaga":
                admin = ram.get_info(message.from_user.id, admin = True)
                admin['where'] = 'media'
                await state.finish()
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())


        
        


@dp.message_handler(state = main_states.input_chanle)
async def inpt_chanel_message_handler(message : types.Message, state : FSMContext):
    if message.text ==  "⬅️ Orqaga":
        await state.finish()
        await message.answer("Sozlamalar", reply_markup = dbuttons.settings(admin = True))
    
    elif re.search(r"^@", message.text):
        try: 
            admins = await bot.get_chat_administrators(chat_id = message.text.strip())
            for admin in admins:
                if admin.user.id == 6331798502:
                    setting.data['forced_chanels'][message.text.strip()] = "https://t.me/" + message.text.strip()[1:]
                    setting.update()

                    await state.finish()
                    await message.answer("Kanal muvafaqiyatli qo'shildi", reply_markup = dbuttons.settings(admin = True))
                    return
            
            await message.answer("Ilimos botni birinchi admin qiling")
        except:
            await message.answer("ERROR")
    else:
        await message.answer("Ilitmos kanal user nameni to'gri kiriting")


@dp.message_handler(state = main_states.log_out_admin)
async def admin_logout_mesage_handler(message : types.Message, state : FSMContext):
    if message.text ==  "⬅️ Orqaga":
        await state.finish()
        await message.answer("Admin panel", reply_markup = dbuttons.menu(admin = True))
    
    elif message.text == "🚶 Chiqish":
        await state.finish()
        ram.logout(message.from_user.id, name = message.from_user.first_name, admin = True)
        await message.answer("Bosh menu", reply_markup = dbuttons.menu())



@dp.message_handler(state = main_states.admin_login)
async def admin_login_mesage_handler(message : types.Message, state : FSMContext):
    if message.text == "⬅️ Orqaga":
        await state.finish()
        await message.answer('Bosh menu', reply_markup = dbuttons.menu())
    
    elif ram.admin_login(message.from_user.id) < 3:
        if message.text == setting.data['pasword']:
            ram.registr(id =  message.from_user.id, name = message.from_user.first_name, admin = True)

            await state.finish()
            await bot.delete_message(chat_id = message.from_user.id, message_id = message.message_id)
            message_data = await bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAI6tWU1NXTI6ZhBHGkyBqEPXPtdO-M-AAJJAgACVp29CiqXDJ0IUyEOMAQ')
            
            await asyncio.sleep(3)
            await bot.delete_message(chat_id = message.from_user.id, message_id = message_data.message_id) 

            await message.answer("Admin panel", reply_markup = dbuttons.menu(admin = True))
        else:
            if ram.admin_login(message.from_user.id, block = True) == 3:
                await state.finish()
                await message.answer("ko'd xat Siz blocklandingiz", reply_markup = dbuttons.menu())

            else:
                await message.reply(f"Ko'd xato sizda {3 - ram.block[message.from_user.id]} ta urinish qoldi", reply_markup = dbuttons.quite_admin_login())
    
    else:
        await state.finish()
        await message.answer("Iltimos keyinroq urinib ko'ring", dbuttons.menu())
            


@dp.message_handler(state = movi_add.set_video)
async def set_video_mesage_handler(message : types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        admin = ram.get_info(message.from_user.id, admin = True)
        if message.text == "⬅️ Orqaga":
            await state.finish()
            admin['where'] = 'chose_hlang'
            await message.answer("Kinoyingzni tilni tanlang", reply_markup = dbuttons.chose_lang())
        
        elif message.text == "🪓 Bekor qilish":
                await state.finish()
                admin['where'] = 'media'
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())

@dp.message_handler(state = movi_add.set_title)
async def get_title(message : types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text == "⬅️ Orqaga":
            await state.set_state(movi_add.set_video)
            await message.answer("Kinoyingzni tashlang", reply_markup = dbuttons.input_video())
            
        elif message.text == "🪓 Bekor qilish":
                admin = ram.get_info(message.from_user.id, admin = True)
                admin['where'] = 'media'
                await state.finish()
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
        
        else:
            ram.set_title(message.from_user.id, title = message.text, admin = True)
            await state.set_state(movi_add.set_info)
            await message.answer("Kino haqida malumot kiritasizmi?", reply_markup = dbuttons.back(skip = True))


@dp.message_handler(state = movi_add.set_info)
async def set_info_message_handler(message: types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text == "⬅️ Orqaga":
            await state.set_state(movi_add.set_title)
            await message.answer("titleni qaytadan kiriting", reply_markup = dbuttons.back())
            
        elif message.text == "🪓 Bekor qilish":
                admin = ram.get_info(message.from_user.id, admin = True)
                admin['where'] = 'media'
                await state.finish()
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
        
        elif message.text == "O'tkazish ➡️":
            await state.set_state(movi_add.set_thum)
            await message.answer("Ok, kinoga Caption phot qo'shasizmi", reply_markup = dbuttons.back(skip = True))

        else:
            await state.set_state(movi_add.set_thum)
            await message.answer("Ok, kinoga Caption phot qo'shasizmi", reply_markup = dbuttons.back(skip = True))
            ram.set_info(id = message.from_user.id, admin = True, caption = message.text)
    

@dp.message_handler(state = movi_add.set_thum)
async def set_thum_message_handler(message: types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text == "⬅️ Orqaga":
            await state.set_state(movi_add.set_info)
            await message.answer("Kino haqida malumot kiritasizmi?", reply_markup = dbuttons.back(skip = True))
            
        elif message.text == "🪓 Bekor qilish":
                admin = ram.get_info(message.from_user.id, admin = True)
                admin['where'] = 'media'
                await state.finish()
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
        
        elif message.text == "O'tkazish ➡️":
            await state.set_state(movi_add.set_save)
            await message.answer("Oxirgi qadam", reply_markup = dbuttons.save_movi()) #"🗃 Saqlash"

        # else:
        #     await state.set_state(movi_add.set_thum)
        #     await message.answer("Ok, kinoga Caption phot qo'shasizmi")
        #     ram.set_info(id = message.from_user.id, admin = True, caption = message.text)



@dp.message_handler(state = movi_add.set_save)
async def set_thum_message_handler(message: types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        if message.text == "⬅️ Orqaga":
            await state.set_state(movi_add.set_thum)
            await message.answer("Kinoga caption photoni qaytadan kiriting", reply_markup = dbuttons.back(skip = True))
            
        elif message.text == "🪓 Bekor qilish":
                admin = ram.get_info(message.from_user.id, admin = True)
                admin['where'] = 'media'
                await state.finish()
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
        
        elif message.text == "🗃 Saqlash":
            movi_data = ram.admin_movi.get(message.from_user.id) 
            if movi_data:   
            
                # Creating comment url and Checking caption  

                if movi_data['caption'] == None:
                    movi_data['caption'] = movi_data['title'] + "\n@kino_qidiruvchi_robot"

                data2 = await bot.send_photo(chat_id = DISCUSS_CHANEL_ID,
                                            photo = movi_data['thumb'],
                                            caption = movi_data['caption'])
                commens_url = data2.url
                        
            
                        
                data = await bot.copy_message(message_id = movi_data['message_id'],
                                             chat_id = CHANEL_ID,
                                             from_chat_id = message.from_user.id,
                                             caption = movi_data['caption'])          
                        
                db.add_movi(title = movi_data['title'],
                            caption = movi_data['caption'],
                            message_id = data.message_id,
                            duration = movi_data['duration'],
                            size = movi_data['size'],
                            lang = movi_data['lang'],
                            thum_url = movi_data['thumb'],
                            coment_url = commens_url)
                        
                ram.add_search_movi(message_id = data.message_id, 
                                    title = movi_data['title'],
                                    caption = movi_data['caption'],
                                    size = movi_data['size'],
                                    duration = movi_data['duration'],
                                    coments = commens_url,
                                    thum_url = movi_data['thumb'],
                                    lang = movi_data['lang'] )#movi

                admin = ram.get_info(message.from_user.id, admin = True)
                admin['where'] = 'media'
                await state.finish()
                await message.answer("Kino muvvafaqiyatli databasega saqlandi", reply_markup = dbuttons.media())
        

n = 0
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
        
        elif message.text == "🛠 Ishlov berish":
            movies = ram.get_admin_movies(message.from_user.id)

            if len(movies) != 0:
                ram.clean_admin_movies(message.from_user.id)
                await state.finish()
                admin['where'] = 'media'
                await message.answer(f"Kinolarga ishlov berish boshlandi. Kinolar soni {len(movies)} ta\n📂 Media menyusi", reply_markup = dbuttons.media())

                # Starting movi add to dataset
                
                
                global n
                for movi in movies:
                    if n >= 20:
                        # sleep_time = randint()
                        await message.answer("Kinolar soni 20 taga yetdi! 30 sonyadan keyin proses davom etadi")
                        await asyncio.sleep(30)
                        n = 0
                    n+=1

                    # FIND DATA AND CLEN INFO
                    title = title_finder(movi['caption'])
                    caption = info_cleaner(movi['caption'], bot = "@kino_qidiruvchi_robot")

                    # COPY THE MOVI
                    data = await bot.copy_message(message_id = movi['message_id'],
                                                      chat_id = CHANEL_ID,
                                                      from_chat_id = message.from_user.id,
                                                      caption = caption)
                    
                    data2 = await bot.send_photo(chat_id = DISCUSS_CHANEL_ID,
                                                    photo = movi['thumb'],
                                                    caption = caption)
                    
                    db.add_movi(title = title,
                                caption = caption,
                                message_id = data.message_id,
                                duration = movi['duration'],
                                size = movi['size'],
                                coment_url = data2.url,
                                thum_url = movi['thumb'],
                                lang = movi['lang'],
                                mode = 'avto')
                    
                    ram.add_search_movi(message_id = data.message_id,
                                        title = title,
                                        caption = caption,
                                        size = movi['size'],
                                        duration = movi['duration'],
                                        coments = data2.url,
                                        thum_url = movi['thumb'])
                
                await message.answer("Ishlov berish tugadi")



            else:
                await message.reply("Iltimos avval kino tashlang")
            

@dp.message_handler(state = main_states.set_movi_code)
async def set_movi_code_message_handler(message: types.Message, state : FSMContext):
    admin = ram.get_info(message.from_user.id, admin = True)
    if message.text == "⬅️ Orqaga":
        admin['where'] = 'media'
        admin['action'] = None
        await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
        await state.finish()
    
    elif message.text == "🆕 qo'shish":
        if len(ram.movies_code) != 0:
            code = max(ram.movies_code.keys()) + 1
        else:
            code = 1
        
        admin['action'] = code
        await message.answer(f"kino kodi : {code}, kinoni tanlang", reply_markup = ibuttons.chose_movi())
    
    elif message.text == "🔄 tahrirlash":
        await state.set_state(main_states.input_movi_number)
        await message.answer("Mavjud kino ko'dini kiriting", reply_markup = dbuttons.onli_back())


@dp.message_handler(state = main_states.input_movi_number)
async def input_number(message: types.Message, state : FSMContext):
    admin = ram.get_info(message.from_user.id, admin = True)
    if message.text == "⬅️ Orqaga":
        admin['action'] = None
        await state.set_state(main_states.set_movi_code)
        await message.answer("Kodli kinolar menyusi", reply_markup = dbuttons.movies_code_menu())

    elif message.text.isnumeric():
        code = int(message.text)

        if code in ram.movies_code.keys():
            admin['action'] = code
            await state.set_state(main_states.set_movi_code)
            await message.answer("Kodli kinolar menyusi", reply_markup = dbuttons.movies_code_menu())
            await message.reply(f"{code} kodi uchun yangi kino tanlang", reply_markup = ibuttons.chose_movi())
        else:
            await message.reply("Bunday kod bilan birorta ham kino saqlanmagan", reply_markup = dbuttons.onli_back())
    else: 
        await message.reply("Kod raqam emasa", reply_markup = dbuttons.onli_back())



@dp.message_handler(state = main_states.input_user_movi)
async def input_user_message(message: types.Message, state : FSMContext):
    user = ram.get_info(message.from_user.id, admin = False)
    if message.text == "⬅️ Orqaga":
        await state.finish()

        message_data = await bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAI4FmU06SmntgY8Ccfnlc1iTwJ2lN8RAALoGAACgJoYSUfokcsDkNm5MAQ')
        await asyncio.sleep(3)
        await bot.delete_message(chat_id = message.from_user.id, message_id = message_data.message_id)
        
        await message.answer("menu", reply_markup = dbuttons.menu())
        await message.answer(f"Foydalanuvchi : {user['name']} \nRo'yxatdan o'tdi : {user['registred']}", reply_markup = ibuttons.more_menu())

    
    elif message.text == "🚀 jo'natish":
        if len(user['message']) > 0:
            for id in user['message']:
                await bot.copy_message(chat_id = setting.data['ram'], message_id = id, from_chat_id = message.from_user.id)

            user['message'] = []
            await state.finish()

            message_data = await bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAI38mU05aGaRAI16hxdbFcS_XPMOdfdAAICFQACOsFQSbdMkgm_6KgTMAQ')
            await asyncio.sleep(3)
            await bot.delete_message(chat_id = message.from_user.id, message_id = message_data.message_id)
            await message.answer("Kino jo'natidi adminlarimiz kinoyingzni tez orda ko'rib chiqshadi", reply_markup = dbuttons.menu())
            

        else:
            message_data = await bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAI302U045uxJZXGFm3fUVo8KKQ7cpoPAALLFAAC3bBRSUxgbDQypB1hMAQ')
            await asyncio.sleep(2)
            await bot.delete_message(chat_id = message.from_user.id, message_id = message_data.message_id)
            await message.answer("Iltimos birinchi kino yoki seriyal jo'nating", reply_markup = dbuttons.user_input_movi())


@dp.message_handler()
async def core_message_handler(message : types.Message, state : FSMContext):
    id = message.from_user.id 
    print(id)
    
    
    if ram.check_user(id):
        # {'name': 'SHermukhammad', 'lang': 'uz', 'where': 'none', 'action': 'none', 'registred': '17.07.2023 13:47'}
        user = ram.get_info(id, admin = False)
        name = user['name']
        where = user['where']

        if message.text == '🎛 Menu':
            user['where'] = 'head_menu'
            await message.answer(f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = ibuttons.menu())

        elif user['where'] == 'none':
            user['where'] = 'head_menu'
            # mes = await message.answer(f"menu", reply_markup = dbuttons.menu())
            # await bot.delete_message(message_id = mes.message_id, chat_id = id)
            await message.answer(f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = dbuttons.menu())



        elif user['where'] == 'head_menu':
            if message.text == '🎛 Menu':
                await message.answer(f"📓 Bosh menu:\n\nFoydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = ibuttons.menu())

            elif message.text.isnumeric():
                code = int(message.text)
                if ram.movies_code.get(code):
                    movi = ram.movies_dict[ram.movies_code[code]]
                    
                    if movi['type'] == 'seri':
                        saved = db.is_saved(user_id = message.from_user.id, movie_id = movi['id'])
                        buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = ram.movies_code[code], serie = True)
        
                        await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)
                    
                    else:
                        saved = db.is_saved(user_id = message.from_user.id, movie_id = movi['id'])
                        buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = movi['id'])
        
                        await bot.copy_message(chat_id = message.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)
            
                else:
                    await message.reply("Bunday kod mavjud emas")
                return

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
            await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", reply_markup = dbuttons.menu(admin = True))



        elif admin['where'] == 'head_menu':
            if message.text == "🎛 Menu":
                await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", reply_markup = ibuttons.menu(admin = True))

            elif message.text == "📂 Media":
                admin['where'] = 'media'
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
            
            elif message.text == "⚙️ Sozlamalar":
                admin['where'] = 'settings'
                await message.answer("Sozlamalar", reply_markup = dbuttons.settings())
        
        elif admin['where'] == 'settings':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'head_menu'
                await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = dbuttons.menu(admin = True))

            elif message.text == "📡 Kanallar":
                await message.answer("Hozirda majvjud jami kanallar ", reply_markup = ibuttons.chanels(setting.data['forced_chanels'].keys()))
            
            elif message.text == "📓 Qo'lanma":
                admin['where'] = 'manual_m'
                await message.answer("Qaysi qo'lanmani tahrirlaymiz?", reply_markup = dbuttons.manual_edit())
        
        elif  admin['where'] == 'manual_m':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'settings'
                await message.answer("Sozlamalar", reply_markup = dbuttons.settings())
            
            elif message.text == "🏠 Bosh sahifa":
                admin['where'] = 'head_menu'
                await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", 
                                     reply_markup = dbuttons.menu(admin = True))
            
            elif message.text == "📝 Yozuvli qo'lanma":
                admin['where'] = 'input_tman'
                await message.answer("Ok, text qo'lanmani kiriting!", reply_markup = dbuttons.input_menu())
            
            elif message.text == "🎞 Video qo'lanma":
                await state.set_state(main_states.input_video_manual)
                await message.answer("Ok, Yangi video qo'lanmani tashlang", reply_markup = dbuttons.input_menu())
        
        elif admin['where'] == 'input_tman':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'manual_m'
                await message.answer("qo'lanma menyusi", reply_markup = dbuttons.manual_edit())

            elif message.text == "🏠 Bosh sahifa":
                admin['where'] = 'head_menu'
                await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", 
                                     reply_markup = dbuttons.menu(admin = True))
            

            else:
                setting.data['user_manual'] = message.text
                setting.update()

                admin['where'] = 'manual_m'
                await message.answer("qo'lanma menyusi", reply_markup = dbuttons.manual_edit())
        

        

        elif admin['where'] == 'media':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'head_menu'
                await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = dbuttons.menu(admin = True))
            
            elif message.text == "🎬 Kino qo'shish":
                admin['where'] = 'chose_hlang'
                await message.answer("Ok, Endi kinoyingzni tilni tanlang", reply_markup = dbuttons.chose_lang())
            
            elif message.text == "📺 Serial qo'shish":
                await state.set_state(main_states.input_serie_lang)
                await message.answer("Seriyal tilni tanlang", reply_markup = dbuttons.chose_lang()) 
            
            elif message.text == '🧮 Kodli kinolar':
                pass
                await message.answer("Kodli kinolar menyus", reply_markup = dbuttons.movies_code_menu())
                await state.set_state(main_states.set_movi_code)

        elif admin['where'] == 'chose_hlang':
            if message.text == "⬅️ Orqaga":
                admin['where'] = 'media'
                await message.answer(f"📂 Media menyusi", reply_markup = dbuttons.media())
            
            elif message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Ruscha", "🇬🇧 Inglizcha"]:
                cheet = {"🇺🇿 O'zbekcha" : 'uz', "🇷🇺 Ruscha" : 'ru', "🇬🇧 Inglizcha" : 'en'}
                ram.creat_movi(id = message.from_user.id, lang = cheet[message.text], admin = True)

                await state.set_state(movi_add.set_video)
                await message.answer("Endi kinoyingzni tashlang", reply_markup = dbuttons.input_video())
        
        
    else:
        await message.answer(f"Assalomu alaykum {message.from_user.first_name}, Xush kelibsiz", reply_markup = dbuttons.menu())
        ram.registr(id = message.from_user.id, name = message.from_user.first_name)

