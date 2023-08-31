from aiogram import types
from aiogram.types import InputMediaPhoto, InputMediaAnimation, InputMediaVideo
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, bot, ibuttons, dbuttons, movi_add, add_movi_avto, DISCUSS_CHANEL_ID, CHANEL_ID, setting, main_states
import time
import asyncio
from random import randint

cheet = {'uz' : "o'zbek", 'en' : "ingliz", 'ru' : "rus"}

    
            
@dp.callback_query_handler()
async def query_handler(query : types.CallbackQuery, state : FSMContext):
    text = query.data
    id = query.from_user.id
    message_id = query.message.message_id



    if ram.check_user(query.from_user.id):
        if text == 'more':
            await bot.edit_message_reply_markup(chat_id = query.from_user.id, 
                                                message_id = query.message.message_id, 
                                                reply_markup = ibuttons.more_menu())

        elif text == 'less':
            await bot.edit_message_reply_markup(chat_id = query.from_user.id, 
                                                message_id = query.message.message_id, 
                                                reply_markup = ibuttons.menu())

        elif text == 'manual':
            content = """I can help you create and manage Telegram bots. If you're new to the Bot API, please see the manual.

You can control me by sending these commands:

/newbot - create a new bot
/mybots - edit your bots

Edit Bots
/setname - change a bot's name
/setdescription - change bot description
/setabouttext - change bot about info
/setuserpic - change bot profile photo
/setcommands - change the list of commands
/deletebot - delete a bot

Bot Settings
/token - generate authorization token
/revoke - revoke bot access token
/setinline - toggle inline mode
/setinlinegeo - toggle inline location requests
/setinlinefeedback - change inline feedback settings
/setjoingroups - can your bot be added to groups?
/setprivacy - toggle privacy mode in groups

Web Apps
/myapps - edit your web apps
/newapp - create a new web app
/listapps - get a list of your web apps
/editapp - edit a web app
/deleteapp - delete an existing web app

Games
/mygames - edit your games
/newgame - create a new game
/listgames - get a list of your games
/editgame - edit a game
/deletegame - delete an existing game"""
            
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = content, 
                                        reply_markup = ibuttons.manual_menu(back = "back_more"))
        
        elif text == "statistics":
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = ram.get_bot_info(), 
                                        reply_markup = ibuttons.manual_menu(back = "back_more2"))

            
        elif text == 'back_more':
            user = ram.get_info(query.from_user.id, admin = False)
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}",
                                        reply_markup = ibuttons.menu())
        
        elif text == 'back_more2':
            user = ram.get_info(query.from_user.id, admin = False)
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}",
                                        reply_markup = ibuttons.more_menu())

        if text == "top_100":
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = f"Top Reyitngdagi kinolar menyusi\n",
                                        reply_markup = ibuttons.top_100())



        elif text == 'random':
            index = randint(0, len(ram.movies)-1)
            movi = ram.movies[index]

            await bot.copy_message(chat_id = query.from_user.id,
                                   from_chat_id = CHANEL_ID,
                                   message_id = movi['id'],
                                   reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                            first_state = True,  
                                                                            id = index, 
                                                                            like = movi['like'], 
                                                                            dislike = movi['dislike'],
                                                                            admin = False,
                                                                            randomly = True))
        
        elif text == 'random2':
            index = randint(0, len(ram.movies)-1)
            movi = ram.movies[index]

            await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                message_id = query.message.message_id,
                                                reply_markup = None)
            await bot.copy_message(chat_id = query.from_user.id,
                                   from_chat_id = CHANEL_ID,
                                   message_id = movi['id'],
                                   reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                                                                            first_state = True,  
                                                                            id = index, 
                                                                            like = movi['like'], 
                                                                            dislike = movi['dislike'],
                                                                            admin = False,
                                                                            randomly = True))
            
        elif text == 'check':
            await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
            await bot.send_message(chat_id = query.from_user.id, text = "Bosh menu", reply_markup = dbuttons.menu())




        # Like va Dislikega jovob beruvchi qisim
        text = text.split('.')
        if len(text) == 3:
            state, movi_id, action = text[-1], int(text[-2]), text[-3]
            # movi = ram.movies[index]
            print(state)
            if state == 'firs':
                if action == 'like':
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        # movi = db.get_movi(id = movi_id)

                        db.like_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'])
                        ram.movies_dict[movi_id]['like'] += 1
                        
                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}.lik")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}.lik")
                        await query.answer("Sizniki Like bosdi")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                        #                                                                      dislike_state = True,  
                        #                                                                      id = index, 
                        #                                                                      like = movi['like'], 
                        #                                                                      dislike = movi['dislike'],
                        #                                                                      admin = False))
                if action == 'dislike':
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.dislike_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'])
                        ram.movies_dict[movi_id]['dislike'] += 1
                        
                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}.dis")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}.dis")
                        await query.answer("Sizniki Dislike bosdi")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
            elif state == 'dis':
                if action == 'dislike':
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.dislike_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'], remove = True)
                        ram.movies_dict[movi_id]['dislike'] -= 1
                        
                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}.firs")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}.firs")
                        await query.answer("Sizniki Dislike bosgan")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                    
                #     ram.like_movi(index, incres = False)
                #     db.like_movi(id = movi['id'], like = movi['dislike'] - 1)

                #     db.dislike_movi(id = movi['id'], dislike = movi['dislike']+1)
                #     ram.dislike_movi(index)
                #     await query.answer("Sizniki DisLike bosdi")
                #     await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                #                                         message_id = query.message.message_id,
                #                                         reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
                #                                                                              like_state = True,  
                #                                                                              id = index, 
                #                                                                              like = movi['like'], 
                #                                                                              dislike = movi['dislike'],
                #                                                                              admin = False))
                # if action == 'like':
                #     await query.answer("Sizniki Like Bosgan")
            
            elif state == 'lik':
                # print(action)
                if action == 'like':
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.like_movi(user_id = query.from_user.id, movie_id = movi_id, like_count = movi['like'], remove = True)
                        ram.movies_dict[movi_id]['like'] -= 1
                        await query.answer("Siznik like bosgan")

                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}.firs")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}.firs")
                        await query.answer("Sizniki Like bosdi")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))

                    
            #         ram.dislike_movi(index, incres = False)
            #         db.dislike_movi(id = movi['id'], dislike = movi['dislike']-1)

            #         db.like_movi(id = movi['id'], like = movi['dislike']+1)
            #         ram.like_movi(index)
            #         await query.answer("Sizniki DisLike bosdi")
            #         await bot.edit_message_reply_markup(chat_id = query.from_user.id,
            #                                             message_id = query.message.message_id,
            #                                             reply_markup = ibuttons.movi_buttons(coments_url = movi['coments'], 
            #                                                                                  dislike_state = True,  
            #                                                                                  id = index, 
            #                                                                                  like = movi['like'], 
            #                                                                                  dislike = movi['dislike'],
            #                                                                                  admin = False))

                # if action == 'dislike':
                #     await query.answer("Sizniki dislike bosdi")

        elif len(text) == 2:
            command, value = text[0], text[1]

            if command == 'chremove':
                setting.data['forced_chanels']

            elif command == 'favorite':
                if db.get_saved_len(id = id) < 5:
                    buttons = query.message.reply_markup.inline_keyboard
                    buttons[0][2] = types.InlineKeyboardButton(text = "🌟", callback_data = f"fremov.{value}")

                    # mov_id = ram.get_movi(index = int(value))['id']
                    db.save_movi(user_id = id, movie_id = value)
                
                    await query.message.edit_reply_markup(types.InlineKeyboardMarkup(inline_keyboard = buttons))
                    await query.answer("Sveimlilarga saqlandi")
                else:
                    await query.answer("Saqlangan kinolaringiz soni 45 tadan oshib ketdi", show_alert = True)

            elif command == 'fremov':
                buttons = query.message.reply_markup.inline_keyboard
                buttons[0][2] = types.InlineKeyboardButton(text = "⭐", callback_data = f"favorite.{value}")
                
                # mov_id = ram.get_movi(index = int(value))['id']
                db.delet_saved(user_id = id, movie_id = value)

                await query.message.edit_reply_markup(types.InlineKeyboardMarkup(inline_keyboard = buttons))
                await query.answer("Sveimlilardan olib tashlandi")

    
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
            elif text == 'avto':
                await state.set_state(add_movi_avto.chose_lang)
                await  bot.edit_message_media(chat_id = id,
                                              message_id = query.message.message_id,
                                              media = InputMediaPhoto(media = open('./data/pictures/add_movi/choose_lang.jpg', 'rb'), caption = "Kinolarni qaysi tilda kiritmoqchisiz?"),
                                              reply_markup = ibuttons.chose_lang(back = 'back_media'))
        

        elif admin['where'] == 'settings':
            if text == 'chanel_add':
                await state.set_state(main_states.input_chanle)
                await bot.delete_message(chat_id = id, message_id = query.message.message_id)
                await bot.send_message(chat_id = id, text = "Iltimos birinchi botni kanalga qo'shinv va kanalni user nameini kiriting maslan @kanal", reply_markup = dbuttons.quite_admin_login())
            
        
            elif text == 'delet':
                await bot.delete_message(chat_id = id, message_id = query.message.message_id)
        
        elif text == 'delet':
             await bot.delete_message(chat_id = id, message_id = query.message.message_id)
        


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
                

        elif len(text) == 2:
            command, value = text[0], text[1]

            if command == 'chremove':
                del setting.data['forced_chanels'][value]
                setting.update()
                #ibuttons.chanels(setting.data['forced_chanels'].keys())
                await bot.edit_message_reply_markup(chat_id = id, message_id = query.message.message_id, reply_markup = ibuttons.chanels(setting.data['forced_chanels'].keys()))
       
        
    else:
        await query.answer("Sizniki ruyxatdan utmaga")