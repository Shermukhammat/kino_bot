from aiogram import types
from aiogram.types import InputMediaPhoto, InputMediaAnimation
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, bot, ibuttons, dbuttons, my_states, get_movi, movi_add






@dp.callback_query_handler(state = movi_add.chose_lang)
async def chose_lang_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data in ['uz', 'en', 'ru']:
            ram.creat_movi(query.from_user.id, lang = query.data, admin = True) # Creating movi in ram

            cheet = {'uz' : "o'zbek", 'en' : "ingliz", 'ru' : "rus"}
            await query.answer(f"Siz {cheet[query.data]} tilni tanladingiz")
            await state.set_state(movi_add.set_video)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(open('./data/pictures/add_movi/1.jpg', 'rb'), caption = "Kinonoyingzni tashlang"),
                                         reply_markup = ibuttons.delet(back = 'back2'))
        elif query.data == 'back1':
            await state.finish()
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(open('./data/pictures/add_movi/select_input_type.jpg', 'rb'), caption = "Qanday usul bilan kino kiritmoqchisiz?"),
                                         reply_markup = ibuttons.ask_movi_input())
        elif query.data == 'delet':
            await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)


@dp.callback_query_handler(state = movi_add.set_video)
async def movi_video_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'back2':
            await state.set_state(movi_add.chose_lang)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/1.jpg', 'rb'), caption = "Kinoyingzni tilni tanlang"),
                                         reply_markup = ibuttons.chose_lang(back = 'back1'))

        elif query.data == 'delet':
                await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
        

@dp.callback_query_handler(state = movi_add.set_info)
async def set_info_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'yes_info':
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/input_caption_text.jpg', 'rb'), caption = "Kino haqida malumot kiriting"),
                                         reply_markup = ibuttons.delet(back = 'back6'))
        
        elif query.data == 'skip_info':
            await state.set_state(movi_add.set_thum)
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/5.jpg', 'rb'), caption = "Kinoga caption rasim kirtasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back_set_info', admin = True, yes = 'yes_thum', skip = 'skip_thum'))
        
        elif query.data == 'back4':
            await state.set_state(movi_add.set_title)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open("./data/pictures/add_movi/3.jpg", 'rb'), caption = "Kino nomni kiriting"),
                                         reply_markup = ibuttons.delet(back = 'back3'))


        elif query.data == 'back6':
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/4.jpg', 'rb'), caption = "Kino haqida malumot kirtasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back4', admin = True))
        
        elif query.data == 'delet':
                await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)



@dp.callback_query_handler(state = movi_add.set_thum)
async def set_movi_thum_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'yes_thum':
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/send_caption_photo.jpg', 'rb'), caption = "Kinoga haqida rasim kiriting"),
                                         reply_markup = ibuttons.delet(back = 'back8'))
        elif query.data == 'skip_thum':
            await query.answer("Ok,Unda Kinoni caption rasmidan foydalanaman")
            await state.set_state(movi_add.set_save)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open("./data/pictures/add_movi/save_movi.jpg"), caption = "Kinon saqlash"),
                                         reply_markup = ibuttons.save_movi(admin = True))
            
        elif query.data == 'back_info':
            await state.set_state(movi_add.set_info)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open("./data/pictures/add_movi/4.jpg", 'rb'), caption = "Kino haqida malumot kiritasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back4', admin = True, yes = 'yes_info', skip = 'skip_info'))
            

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
                await state.set_state(movi_add.chose_lang)
                await  bot.edit_message_media(chat_id = id,
                                              message_id = query.message.message_id,
                                              media = InputMediaPhoto(media = open('./data/pictures/add_movi/2.jpg', 'rb'), caption = "Kinoyingzni tilni tanlang"),
                                              reply_markup = ibuttons.chose_lang(back = 'back1'))


    else:
        print("Sizniki  utmagan")