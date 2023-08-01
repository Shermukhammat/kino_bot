from aiogram import types
from aiogram.types import InputMediaPhoto, InputMediaAnimation
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, bot, ibuttons, dbuttons, my_states, get_movi, movi_add



# @dp.callback_query_handler(state = get_movi.get_video)
# async def get_video_query(query : types.CallbackQuery, state : FSMContext):
#     id = query.from_user.id

#     if query.data == 'delet':
#         await bot.delete_message(chat_id = id, message_id = query.message.message_id)
    
#     elif query.data == 'next1':
#         await state.set_state(get_movi.get_title)
#         await bot.send_message(text = "Endi esa kino nomni kiriting", chat_id = id)
    
# @dp.callback_query_handler(state = get_movi.get_title)
# async def get_tile_quer(query : types.CallbackQuery, state : FSMContext):
#     id = query.from_user.id
#     if query.data == 'delet':
#         await bot.delete_message(chat_id = id, message_id = query.message.message_id)
    
#     elif query.data == 'next2':
#         await state.set_state(get_movi.get_caption)
#         await bot.edit_message_reply_markup(reply_markup = ibuttons.delet_button(), 
#                                             chat_id = id, 
#                                             message_id = query.message.message_id)
#         await bot.send_message(chat_id = id, text = "Ok endi kinoga caption kiriting")
    
#     elif query.data == 'back2':
#         await state.set_state(get_movi.get_video)
#         await bot.edit_message_reply_markup(reply_markup = ibuttons.delet_button(), 
#                                             chat_id = id, 
#                                             message_id = query.message.message_id)
#         await bot.send_message(chat_id = id, text = "Ok Kinoyingzni videyosni tashlang")
    
# @dp.callback_query_handler(state = get_movi.get_caption)
# async def get_caption_query(query : types.CallbackQuery, state : FSMContext):
#     id  = query.from_user.id
#     message_id = query.message.message_id

#     if query.data == 'delet':
#         await bot.delete_message(chat_id = id, message_id = query.message.message_id)

#     elif query.data == 'back3':
#         await state.set_state(get_movi.get_title)
#         await bot.send_message(chat_id = id, text = "Ok endi kinoga title kiriting")
    
#     elif query.data == 'next3':
#         await bot.send_message(chat_id = id,
#                                text = f"Kinonoga caption phot qo'shishni xoxlaysizmi?",
#                                reply_markup = ibuttons.photo_caption())
    
    
#     if query.data == 'yes':
#         await state.set_state(get_movi.get_caption_photo)
#         await bot.send_message(text = "OK, endi caption photoni tashlang", chat_id = id)

#     elif query.data == 'no':
#         await query.answer( "Ok, unda videoni caption photosidan foydalanaman!")
#         await bot.edit_message_reply_markup(chat_id = id, 
#                                             message_id = query.message.message_id, 
#                                             reply_markup = ibuttons.add_movi())

#     # elif text == 'delet':
#     #     await bot.delete_message(chat_id = id, message_id = message_id)
    
#     elif query.data == 'add':
#         await query.answer("Kino qo'shildi :)")

#     elif query.data == 'back5':
#         await bot.edit_message_reply_markup(chat_id = id, 
#                                             message_id = query.message.message_id,
#                                             reply_markup = ibuttons.photo_caption())
    
#     # elif text == 'back':
#     #     await state.set_state(get_movi.get_title)
#     #     movie = ram.get_movi(id)

#     #     await bot.send_video(video = movie['vide_id'],
#     #                      chat_id = id,
#     #                      caption = f"Kino nomi: {movie['title']}\n{movie['caption']}\nKinoga phot caption qo'shishni xolaysizmi?",
#     #                      reply_markup = ibuttons.photo_caption())



# @dp.callback_query_handler(state = get_movi.get_caption_photo)
# async def get_caption_phot_query(query : types.CallbackQuery, state : FSMContext):
#     if query.data == 'add':
#         await state.finish()
#         await bot.send_message(chat_id = query.from_user.id, text = "tugadi :) ...")
    
#     elif query.data == 'back5':
#         await state.set_state(get_movi.get_caption)
#         await bot.edit_message_reply_markup(reply_markup = ibuttons.delet_button(), 
#                                             chat_id = query.from_user.id, 
#                                             message_id = query.message.message_id)
#         await bot.send_message(chat_id = query.from_user.id, text = "kinoga phot caption qo'shishnini xoxlaysizmi?",
#                                reply_markup = ibuttons.photo_caption())



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
                                         media = InputMediaAnimation(open('./data/pictures/add_movi/send_movi.mp4', 'rb'), caption = "Kinonoyingzni tashlang"),
                                         reply_markup = ibuttons.delet(back = 'back2'))
        elif query.data == 'back1':
            await state.finish()
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaAnimation(open('./data/pictures/add_movi/chose_input_type.mp4', 'rb'), caption = "Qanday usul bilan kino kiritmoqchisiz?"),
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
                                         media = InputMediaAnimation(media = open('./data/pictures/add_movi/chose_lang.mp4', 'rb'), caption = "Kinoyingzni tilni tanlang"),
                                         reply_markup = ibuttons.chose_lang(back = 'back1'))
        # elif query.data == 'back2':
        #     await state.set_state(movi_add.chose_lang)
        #     await  bot.edit_message_media(chat_id = query.from_user.id,
        #                                       message_id = query.message.message_id,
        #                                       media = InputMediaAnimation(media = open('./data/pictures/add_movi/chose_lang.mp4', 'rb'), caption = "Kinoyingzni tilni tanlang"),
        #                                       reply_markup = ibuttons.chose_lang())
        elif query.data == 'delet':
                await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
        


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
                await state.set_state(movi_add.chose_lang)
                await  bot.edit_message_media(chat_id = id,
                                              message_id = query.message.message_id,
                                              media = InputMediaAnimation(media = open('./data/pictures/add_movi/chose_lang.mp4', 'rb'), caption = "Kinoyingzni tilni tanlang"),
                                              reply_markup = ibuttons.chose_lang(back = 'back1'))


            # elif text == 'back':
            #     await  bot.edit_message_media(chat_id = id,
            #                                   message_id = query.message.message_id,
            #                                   media = InputMediaPhoto(media = open('./data/pictures/4.jpg', 'rb'), caption = f"{admin['name']} qanday usul bilan kino kiritmoqchisiz?"),
            #                                   reply_markup = ibuttons.ask_movi_input())
            
            # elif text in ['set_uz', 'set_ru', 'set_en']:
            #     lang = text[-2:]
            #     ram.creat_movi(id, lang = lang)
            #     cheet = {'uz' : "o'zbek", 'ru' : "rus", 'en' : "ingliz"}
        
            #     await query.answer(text = f"Siz {cheet[lang]} tilni tanladingiz")
            #     await bot.edit_message_media(chat_id = id,
            #                                 message_id = query.message.message_id,
            #                                 media = InputMediaAnimation(media = open('./data/pictures/add_movi/send_movi.mp4', 'rb'), caption = "Kin"))
            #     # await  bot.edit_message_media(chat_id = id,
            #     #                               message_id = query.message.message_id,
            #     #                               media = InputMediaPhoto(media = open('./data/pictures/2.jpg', 'rb'), caption = f"||ooo"),
            #     #                               reply_markup = ibuttons.change_state(back = 'back2', next = 'next2'))
        
            # elif text == 'back2':
            #     await  bot.edit_message_media(chat_id = id,
            #                                   message_id = query.message.message_id,
            #                                   media = InputMediaPhoto(media = open('./data/pictures/4.jpg', 'rb'), caption = "|oooo\nKinoyingzni tilni tanlang"),
            #                                   reply_markup = ibuttons.chose_lang())
            
            # elif text == 'next2':
            #     await state.set_state(get_movi.get_video)
            #     await bot.send_message(text = "Endi es, Kinoyingzni videosni tashlang!", chat_id = id)

    else:
        print("Sizniki  utmagan")