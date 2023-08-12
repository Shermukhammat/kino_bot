from aiogram import types
from aiogram.types import InputMediaPhoto, InputMediaAnimation
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, bot, ibuttons, dbuttons, my_states, get_movi, movi_add, DISCUSS_CHANEL_ID, CHANEL_ID
import time
import asyncio





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
                                         media = InputMediaPhoto(open('./data/pictures/add_movi/send_movi.jpg', 'rb'), caption = "Kinonoyingzni tashlang"),
                                         reply_markup = ibuttons.delet(back = 'back_chose_lang'))
        elif query.data == 'back_media':
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
        if query.data == 'back_chose_lang':
            await state.set_state(movi_add.chose_lang)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/choose_lang.jpg', 'rb'), caption = "Kinoyingzni tilni tanlang"),
                                         reply_markup = ibuttons.chose_lang(back = 'back_media'))

        elif query.data == 'delet':
                await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
        

@dp.callback_query_handler(state = movi_add.set_title)
async def set_title_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'back_set_video':
            await state.set_state(movi_add.set_video)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(open('./data/pictures/add_movi/send_movi.jpg', 'rb'), caption = "Kinonoyingzni tashlang"),
                                         reply_markup = ibuttons.delet(back = 'back_chose_lang'))
        elif query.data == 'delet':
                await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)


@dp.callback_query_handler(state = movi_add.set_info)
async def set_info_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'yes_info':
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/input_caption_text.jpg', 'rb'), caption = "Kino haqida malumot kiriting"),
                                         reply_markup = ibuttons.delet(back = 'back_def'))
        
        elif query.data == 'skip_info':
            await state.set_state(movi_add.set_thum)
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/ask_thum.jpg', 'rb'), caption = "Kinoga caption rasim kirtasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back_set_info', admin = True, yes = 'yes_thum', skip = 'skip_thum'))
        
        elif query.data == 'back_title':
            await state.set_state(movi_add.set_title)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open("./data/pictures/add_movi/input_title.jpg", 'rb'), caption = "Kino nomni kiriting"),
                                         reply_markup = ibuttons.delet(back = 'back_set_video'))


        elif query.data == 'back_def':
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/ask_input_info.jpg', 'rb'), caption = "Kino haqida malumot kirtasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back_title', admin = True, yes = 'yes_info', skip = 'skip_info'))
        
        elif query.data == 'delet':
                await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)



@dp.callback_query_handler(state = movi_add.set_thum)
async def set_movi_thum_query(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'yes_thum':
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/send_caption_photo.jpg', 'rb'), caption = "Kinoga rasim kiriting"),
                                         reply_markup = ibuttons.delet(back = 'back_thum'))
        elif query.data == 'skip_thum':
            await query.answer("Ok,Unda Kinoni caption rasmidan foydalanaman")
            await state.set_state(movi_add.set_save)
            await bot.edit_message_media(chat_id = query.from_user.id,
                                         message_id = query.message.message_id,
                                         media = InputMediaPhoto(media = open("./data/pictures/add_movi/save_movi.jpg", 'rb'), caption = "Kinon saqlash"),
                                         reply_markup = ibuttons.save_movi(admin = True, back = 'back_set_thum'))
            
        elif query.data == 'back_set_info':
            await state.set_state(movi_add.set_info)
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media = InputMediaPhoto(media = open('./data/pictures/add_movi/ask_input_info.jpg', 'rb'), caption = "Kino haqida malumot kirtasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back_title', admin = True, yes = 'yes_info', skip = 'skip_info'))
            
        elif query.data == 'back_thum':
            await bot.edit_message_media(message_id  = query.message.message_id,
                                        chat_id = query.from_user.id,
                                        media = InputMediaPhoto(media = open('./data/pictures/add_movi/ask_thum.jpg', 'rb'), caption = "Kinoga caption rasim kirtasizmi?"),
                                        reply_markup = ibuttons.ask_button(back = 'back_set_info', admin = True, yes = 'yes_thum', skip = 'skip_thum'))
        
        elif query.data == 'delet':
            await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)


@dp.callback_query_handler(state = movi_add.set_save)
async def set_save_query_handler(query : types.CallbackQuery, state : FSMContext):
    if ram.check_admin(query.from_user.id):
        if query.data == 'back_set_thum':
            await state.set_state(movi_add.set_thum)
            await bot.edit_message_media(message_id = query.message.message_id,
                                         chat_id = query.from_user.id,
                                         media =InputMediaPhoto(media = open('./data/pictures/add_movi/ask_thum.jpg', 'rb'), caption = "Kinoga caption rasim kirtasizmi?"),
                                         reply_markup = ibuttons.ask_button(back = 'back_set_info', admin = True, yes = 'yes_thum', skip = 'skip_thum'))
        
        elif query.data == 'delet_movi':
            await state.finish()
            ram.delet_movi(id, admin = True)
            await bot.send_message(chat_id = query.from_user.id, text = "Kino o'chrib tashlandi")
        
        elif query.data == 'delet':
            await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
        
        elif query.data == 'save':
            await state.finish()
            await bot.send_message(chat_id = query.from_user.id, text = "Kino yuklanmoqda")
            
            movi = ram.get_movi(query.from_user.id)
            if len(movi) != 0:
                n = 0
                while True:
                    n+=1
                    if ram.port:
                        movi_data = ram.get_movi(query.from_user.id)
                        
                        # Creating comment url and Checking caption
                        
                        if movi_data['caption'] == None:
                            movi_data['caption'] = movi_data['title'] + "\n@kino_qidruvchi_robot"

                        data = await bot.send_photo(chat_id = DISCUSS_CHANEL_ID,
                                                    photo = movi_data['thumb'],
                                                    caption = movi_data['caption'])
                        commens_url = data.url
                        
            
                        
                        data = await bot.copy_message(message_id = movi_data['message_id'],
                                                      chat_id = CHANEL_ID,
                                                      from_chat_id = query.from_user.id,
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
                                            lang = movi_data['lang'])
                        

                        
                        #  {'video_id' : None,
                        #            'message_id' : None,
                        #       'caption' : None,
                        #       'title' : None,
                        #       'duration' : None, 
                        #       'size' : None,
                        #       'thumb' : None,
                        #       'lang' : lang}



                        await bot.send_message(chat_id = query.from_user.id, text = "Kino muvafqiyali yuklandi")
                        break
                    else:
                        await asyncio.sleep(20)
                    if n == 10:
                        await bot.send_message(chat_id = query.from_user.id, text = f"Afsus kino yuklanmadi. Port 200 sekun ichida ochilmadi")
                        break
                
    

          
            
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
    
        
        # Like va Dislikega jovob beruvchi qisim
        text = text.split('.')
        if len(text) == 3:
            state, index, action = text[-1], int(text[-2]), text[-3]
            movi = ram.movies[index]
            if state == 'firs':
                if action == 'like':
                    db.like_movi(id = movi['id'], like = movi['like'] + 1)
                    ram.like_movi(index)
                    await query.answer("Sizniki Like bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             dislike_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike'],
                                                                                             admin = False))
                if action == 'dislike':
                    db.dislike_movi(id = movi['id'], dislike = movi['dislike']+1)
                    ram.dislike_movi(index)
                    await query.answer("Sizniki DisLike bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             like_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike'],
                                                                                             admin = False))
            elif state == 'dis':
                if action == 'dislike':
                    ram.like_movi(index, incres = False)
                    db.like_movi(id = movi['id'], like = movi['dislike'] - 1)

                    db.dislike_movi(id = movi['id'], dislike = movi['dislike']+1)
                    ram.dislike_movi(index)
                    await query.answer("Sizniki DisLike bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             like_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike'],
                                                                                             admin = False))
                if action == 'like':
                    await query.answer("Sizniki Like Bosgan")
            
            elif state == 'lik':
                # print(action)
                if action == 'like':
                    ram.dislike_movi(index, incres = False)
                    db.dislike_movi(id = movi['id'], dislike = movi['dislike']-1)

                    db.like_movi(id = movi['id'], like = movi['dislike']+1)
                    ram.like_movi(index)
                    await query.answer("Sizniki DisLike bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             dislike_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike'],
                                                                                             admin = False))

                if action == 'dislike':
                    await query.answer("Sizniki Dislike Bosgan")


    
    elif ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
        name = admin['name']
        where = admin['where']

        if admin['where'] == 'none':
            admin['where'] = 'head_menu'
            # await query.answer(f"Bosh menu", reply_markup = dbuttons.menu(admin = True))
            await bot.send_message(text = "Bosh menu", chat_id = id, reply_markup = dbuttons.menu(admin = True))

        # elif admin['where'] == 'head_menu':
        #     pass

        elif admin['where'] == 'media':
            if text == 'delet':
                await bot.delete_message(chat_id = id, message_id = message_id)

            elif text == 'hand':
                await state.set_state(movi_add.chose_lang)
                await  bot.edit_message_media(chat_id = id,
                                              message_id = query.message.message_id,
                                              media = InputMediaPhoto(media = open('./data/pictures/add_movi/choose_lang.jpg', 'rb'), caption = "Kinoyingzni tilni tanlang"),
                                              reply_markup = ibuttons.chose_lang(back = 'back_media'))
        
        text = text.split('.')
        # print(text)
        if len(text) == 3:
            state, index, action = text[-1], int(text[-2]), text[-3]
            movi = ram.movies[index]
            if state == 'firs':
                if action == 'like':
                    db.like_movi(id = movi['id'], like = movi['like'] + 1)
                    ram.like_movi(index)
                    await query.answer("Sizniki Like bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             dislike_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike']))
                if action == 'dislike':
                    db.dislike_movi(id = movi['id'], dislike = movi['dislike']+1)
                    ram.dislike_movi(index)
                    await query.answer("Sizniki DisLike bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             like_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike']))
            elif state == 'dis':
                if action == 'dislike':
                    ram.like_movi(index, incres = False)
                    db.like_movi(id = movi['id'], like = movi['dislike'] - 1)

                    db.dislike_movi(id = movi['id'], dislike = movi['dislike']+1)
                    ram.dislike_movi(index)
                    await query.answer("Sizniki DisLike bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             like_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike']))
                if action == 'like':
                    await query.answer("Sizniki Like Bosgan")
            
            elif state == 'lik':
                # print(action)
                if action == 'like':
                    ram.dislike_movi(index, incres = False)
                    db.dislike_movi(id = movi['id'], dislike = movi['dislike']-1)

                    db.like_movi(id = movi['id'], like = movi['dislike']+1)
                    ram.like_movi(index)
                    await query.answer("Sizniki DisLike bosdi")
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                                             dislike_state = True,  
                                                                                             id = index, 
                                                                                             like = movi['like'], 
                                                                                             dislike = movi['dislike']))

                if action == 'dislike':
                    await query.answer("Sizniki Dislike Bosgan")
                


            # if text[0] == 'like':
            #     index = int(text[1])
            #     movi = ram.movies[index]

            #     db.like_movi(id = movi['id'], like = movi['like'] + 1)
            #     await query.answer("Sizniki Like bosdi")
            #     await bot.edit_message_reply_markup(chat_id = query.from_user.id,
            #                                         message_id = query.message.message_id,
            #                                         reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
            #                                                                             dislike_state = True,  
            #                                                                             id = index, 
            #                                                                             like = movi['like']+1, 
            #                                                                             dislike = movi['dislike']))
 
            # elif text[0] == 'dislike':
            #     index = int(text[1])
            #     movi = ram.movies[index]

            #     db.dislike_movi(id = movi['id'], dislike = movi['dislike'] + 1)
                
  
            #     await query.answer("Sizniki Dislike bosdi")
            #     await bot.edit_message_reply_markup(chat_id = query.from_user.id,
            #                                         message_id = query.message.message_id,
            #                                         reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
            #                                                                             dislike_state = True,  
            #                                                                             id = index, 
            #                                                                             like = movi['like'], 
            #                                                                             dislike = movi['dislike']+1))
        
       
        
    else:
        await query.answer("Sizniki ruyxatdan utmaga")