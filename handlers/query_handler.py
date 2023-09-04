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

    # print(text)

    if ram.check_user(query.from_user.id):
        if text == 'more':
            await bot.edit_message_reply_markup(chat_id = query.from_user.id, 
                                                message_id = query.message.message_id, 
                                                reply_markup = ibuttons.more_menu())
        
        if text == 'delet':
            await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
        
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
            index = randint(0, len(ram.movies_id)-1)
            movi_id = ram.movies_id[index]
            movi = ram.movies_dict[movi_id]
            
            if movi['type'] == 'movi':
                saved = db.is_saved(user_id = query.from_user.id, movie_id = movi['id'])
                buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = movi['id'])
        

                await bot.copy_message(chat_id = query.from_user.id,
                                   from_chat_id = CHANEL_ID,
                                   message_id = movi['id'],
                                   reply_markup = buttons)
            
            elif movi['type'] == 'seri':
                saved = db.is_saved(user_id = query.from_user.id, movie_id = movi['id'])
                buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = movi['id'], serie = True)
        
                await bot.copy_message(chat_id = query.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)

        
        elif text == 'random2':
            index = randint(0, len(ram.movies_id)-1)
            movi_id = ram.movies_id[index]
            movi = ram.movies_dict[movi_id]
            
            if movi['type'] == 'movi':
                saved = db.is_saved(user_id = query.from_user.id, movie_id = movi['id'])
                buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = movi['id'])
            
                await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                message_id = query.message.message_id,
                                                reply_markup = None)
                await bot.copy_message(chat_id = query.from_user.id,
                                   from_chat_id = CHANEL_ID,
                                   message_id = movi['id'],
                                   reply_markup = buttons)
            
            
            elif movi['type'] == 'seri':
                saved = db.is_saved(user_id = query.from_user.id, movie_id = movi['id'])
                buttons = ibuttons.movi_buttons(coments_url = movi['coments'], like = movi['like'], dislike = movi['dislike'], saved = saved, admin = False, id = movi['id'], serie = True)
        
                await bot.copy_message(chat_id = query.from_user.id,
                                       message_id = movi['id'],
                                       from_chat_id = CHANEL_ID,
                                       reply_markup = buttons)
            
        elif text == 'check':
            await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
            await bot.send_message(chat_id = query.from_user.id, text = "Bosh menu", reply_markup = dbuttons.menu())




        

        # Comandalar qismi
        text = text.split('.')
        if len(text) == 2:
            command, value = text[0], text[1]
            
            if command == 'parts':
                value = int(value)
                serie = ram.movies_dict[value]

                await bot.edit_message_reply_markup(chat_id = query.from_user.id, 
                                                    message_id = query.message.message_id,
                                                    reply_markup = ibuttons.serie_parts(serie_id = value, parts = serie['parts_id']))

            elif command == 'favorite':
                if db.get_saved_len(id = id) < 45:
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

            elif command == 'back_ser':
                value = int(value)
                seire = ram.movies_dict.get(value)
                # if movi
                # movi = db.get_movi(id = index)
                if seire:
                    # state = db.is_like(user_id = query.from_user.id, movie_id = seire['id'])
                    saved = db.is_saved(user_id = query.from_user.id, movie_id = seire['id'])
                    # db.get_
                    buttons = ibuttons.movi_buttons(coments_url = seire['coments'], like = seire['like'], dislike = seire['dislike'], saved = saved, admin = False, id = value, serie = True)
        
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id, message_id = query.message.message_id, reply_markup = buttons)


            elif  command == 'gpart':
                part_id = int(value)
                await bot.copy_message(chat_id = query.from_user.id, from_chat_id = CHANEL_ID, message_id = part_id)
            
            elif command == 'pnex':
                serie_id = int(value)
                serie = ram.movies_dict[serie_id]

                buttons = query.message.reply_markup.inline_keyboard            
                last = int(buttons[0][-1].text)

                new_buttons = []
                n = 0
                for num, idd in serie['parts_id'].items():
                    if num > last and n < 5:
                        n+=1
                        new_buttons.append(types.InlineKeyboardButton(text = f' {num} ', callback_data = f"gpart.{idd}"))

                if len(new_buttons) > 0:
                    buttons[0] = new_buttons

                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                else:
                    await query.answer("Boshqa qismlar mavjud emas")
            
            elif command == 'pback':
                serie_id = int(value)
                serie = ram.movies_dict[serie_id]

                buttons = query.message.reply_markup.inline_keyboard            
                head = int(buttons[0][0].text)
                start = head - 5
                # print(head)

                new_buttons = []
                for num, idd in serie['parts_id'].items():
                    if num >= start and num < head:
                        new_buttons.append(types.InlineKeyboardButton(text = f' {num} ', callback_data = f"gpart.{idd}"))

                if len(new_buttons) > 0:
                    buttons[0] = new_buttons

                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                else:
                    await query.answer("Boshqa qismlar mavjud emas")


            elif command == 'like':
                movi_id = int(value)
                state = db.is_like(user_id = query.from_user.id, movie_id = movi_id)
                # print(state)

                if state == 'like':
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.like_movi(user_id = query.from_user.id, movie_id = movi_id, like_count = movi['like'], remove = True)
                        ram.movies_dict[movi_id]['like'] -= 1

                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")
                        await query.answer("Like olib tashlandi")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                    
                
                elif state == None:
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.like_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'])
                        ram.movies_dict[movi_id]['like'] += 1
                    
                        buttons = query.message.reply_markup.inline_keyboard
                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")

                        await query.answer("Siz Like bosdingiz")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                
                else:
                    await query.answer("Siz DisLike bosgansiz")
            
            if command == 'dislike':
                movi_id = int(value)
                state = db.is_like(user_id = query.from_user.id, movie_id = movi_id)

                if state == None:
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.dislike_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'])
                        ram.movies_dict[movi_id]['dislike'] += 1
                        
                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")
                        await query.answer("Siz Dislike bosdingiz")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                
                elif state == 'dislike':
                    movi_id = int(value)
                    movi = ram.movies_dict.get(movi_id)

                    if movi:
                            db.dislike_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'], remove = True)
                            ram.movies_dict[movi_id]['dislike'] -= 1
                        
                            buttons = query.message.reply_markup.inline_keyboard

                            buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                            buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")
                            await query.answer("Dislike olib tashlandi")
                            await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                    
                else:
                    await query.answer("Siz Like bosgansiz")


                
            

    elif ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
        name = admin['name']
        where = admin['where']

        

        if text == 'more':
            await bot.edit_message_text(text = f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", 
                                        reply_markup = ibuttons.more_menu(admin = True),
                                        chat_id = query.from_user.id,
                                        message_id = query.message.message_id)
            
        
        elif text == 'less':
            await bot.edit_message_text(text = f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}\n Bugun nima qilamiz admin aka?", 
                                        reply_markup = ibuttons.menu(admin = True),
                                        chat_id = query.from_user.id,
                                        message_id = query.message.message_id)
        
        elif text == 'statistics':
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = ram.get_bot_info(), 
                                        reply_markup = ibuttons.manual_menu(back = "back_more"))
        
        elif text == 'back_more':
            admin = ram.get_info(query.from_user.id, admin = True)
            await bot.edit_message_text(chat_id = query.from_user.id, 
                                        message_id = query.message.message_id,
                                        text = f"Foydalanuvchi : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}",
                                        reply_markup = ibuttons.more_menu(admin = True))
        
        elif text == "⚡️ Primyeralar":
            pass
            # await state.set_state(main_states)


        if admin['where'] == 'settings':
            if text == 'chanel_add':
                await state.set_state(main_states.input_chanle)
                await bot.delete_message(chat_id = id, message_id = query.message.message_id)
                await bot.send_message(chat_id = id, text = "Iltimos birinchi botni kanalga qo'shinv va kanalni user nameini kiriting maslan @kanal", reply_markup = dbuttons.quite_admin_login())
            
        
            elif text == 'delet':
                await bot.delete_message(chat_id = id, message_id = query.message.message_id)
        
        elif text == 'delet':
             await bot.delete_message(chat_id = id, message_id = query.message.message_id)
        


        # Like va Dislikega jovob beruvchi qisim
        text = text.split('.')
        if len(text) == 2:
            command, value = text[0], text[1]

            if command == 'chremove':
                del setting.data['forced_chanels'][value]
                setting.update()
                #ibuttons.chanels(setting.data['forced_chanels'].keys())
                await bot.edit_message_reply_markup(chat_id = id, message_id = query.message.message_id, reply_markup = ibuttons.chanels(setting.data['forced_chanels'].keys()))

            
            elif command == 'parts':
                value = int(value)
                serie = ram.movies_dict[value]

                await bot.edit_message_reply_markup(chat_id = query.from_user.id, 
                                                    message_id = query.message.message_id,
                                                    reply_markup = ibuttons.serie_parts(serie_id = value, parts = serie['parts_id']))

            elif command == 'favorite':
                if db.get_saved_len(id = id) < 45:
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

            elif command == 'back_ser':
                value = int(value)
                seire = ram.movies_dict.get(value)
                if seire and seire['type'] == 'seri':
                    saved = db.is_saved(user_id = query.from_user.id, movie_id = seire['id'])
                    buttons = ibuttons.movi_buttons(coments_url = seire['coments'], like = seire['like'], dislike = seire['dislike'], saved = saved, admin = True, id = value, serie = True)
        
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id, message_id = query.message.message_id, reply_markup = buttons)
                
                elif seire and seire['type'] == 'movi':
                    saved = db.is_saved(user_id = query.from_user.id, movie_id = seire['id'])
                    buttons = ibuttons.movi_buttons(coments_url = seire['coments'], like = seire['like'], dislike = seire['dislike'], saved = saved, admin = True, id = value)
        
                    await bot.edit_message_reply_markup(chat_id = query.from_user.id, message_id = query.message.message_id, reply_markup = buttons)



            elif  command == 'gpart':
                part_id = int(value)
                await bot.copy_message(chat_id = query.from_user.id, from_chat_id = CHANEL_ID, message_id = part_id)
            
            elif command == 'pnex':
                serie_id = int(value)
                serie = ram.movies_dict[serie_id]

                buttons = query.message.reply_markup.inline_keyboard            
                last = int(buttons[0][-1].text)

                new_buttons = []
                n = 0
                for num, idd in serie['parts_id'].items():
                    if num > last and n < 5:
                        n+=1
                        new_buttons.append(types.InlineKeyboardButton(text = f' {num} ', callback_data = f"gpart.{idd}"))

                if len(new_buttons) > 0:
                    buttons[0] = new_buttons

                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                else:
                    await query.answer("Boshqa qismlar mavjud emas")
            
            elif command == 'pback':
                serie_id = int(value)
                serie = ram.movies_dict[serie_id]

                buttons = query.message.reply_markup.inline_keyboard            
                head = int(buttons[0][0].text)
                start = head - 5
                # print(head)

                new_buttons = []
                for num, idd in serie['parts_id'].items():
                    if num >= start and num < head:
                        new_buttons.append(types.InlineKeyboardButton(text = f' {num} ', callback_data = f"gpart.{idd}"))

                if len(new_buttons) > 0:
                    buttons[0] = new_buttons

                    await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                else:
                    await query.answer("Boshqa qismlar mavjud emas")


            elif command == 'like':
                movi_id = int(value)
                state = db.is_like(user_id = query.from_user.id, movie_id = movi_id)
                # print(state)

                if state == 'like':
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.like_movi(user_id = query.from_user.id, movie_id = movi_id, like_count = movi['like'], remove = True)
                        ram.movies_dict[movi_id]['like'] -= 1

                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")
                        await query.answer("Like olib tashlandi")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                    
                
                elif state == None:
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.like_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'])
                        ram.movies_dict[movi_id]['like'] += 1
                    
                        buttons = query.message.reply_markup.inline_keyboard
                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")

                        await query.answer("Siz Like bosdingiz")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                
                else:
                    await query.answer("Siz DisLike bosgansiz")
            
            elif command == 'dislike':
                movi_id = int(value)
                state = db.is_like(user_id = query.from_user.id, movie_id = movi_id)

                if state == None:
                    movi = ram.movies_dict.get(movi_id)
                    if movi:
                        db.dislike_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'])
                        ram.movies_dict[movi_id]['dislike'] += 1
                        
                        buttons = query.message.reply_markup.inline_keyboard

                        buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                        buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")
                        await query.answer("Siz Dislike bosdingiz")
                        await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                
                elif state == 'dislike':
                    movi_id = int(value)
                    movi = ram.movies_dict.get(movi_id)

                    if movi:
                            db.dislike_movi(user_id = query.from_user.id, movie_id = movi['id'], like_count = movi['like'], remove = True)
                            ram.movies_dict[movi_id]['dislike'] -= 1
                        
                            buttons = query.message.reply_markup.inline_keyboard

                            buttons[0][0] = types.InlineKeyboardButton(text = f"👍 {movi['like']}", callback_data = f"like.{movi_id}")
                            buttons[0][1] = types.InlineKeyboardButton(text = f"👎 {movi['dislike']}", callback_data = f"dislike.{movi_id}")
                            await query.answer("Dislike olib tashlandi")
                            await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                        message_id = query.message.message_id,
                                                        reply_markup = types.InlineKeyboardMarkup(inline_keyboard = buttons))
                    
                else:
                    await query.answer("Siz Like bosgansiz")


            elif command == 'delets':
                await query.answer("Xaqiqatdan xam kinoni o'chrmoqchimisiz?", show_alert = True)
                await bot.edit_message_reply_markup(chat_id = query.from_user.id,
                                                    message_id = query.message.message_id,
                                                    reply_markup = ibuttons.suure_delet(id = value))


            #back_ser
            elif command == 'delets2':

                movi_id = int(value)
                movi = ram.movies_dict.get(movi_id)
                if movi and movi['type'] == 'seri':

                    # Delet comment
                    if movi['coments'].split('/')[-1].isnumeric:
                        try:
                            await bot.delete_message(chat_id = '@kino_bot_discuss', message_id = int(movi['coments'].split('/')[-1]))
                        except:
                            await query.answer("Comment message topilmadi")

                    try:
                        for part_num, part_id in movi['parts_id'].items():
                            await bot.delete_message(chat_id = CHANEL_ID, message_id = part_id)
                        await query.answer("Hamma seriyal qismlari o'chrib tashlandi")
                    except:
                        await query.answer("Seriyal qismlari topilmadi")
                    
                    await bot.delete_message(chat_id = CHANEL_ID, message_id = movi_id)

                    
                    db.delet_serie(movi_id)
                    del ram.movies_dict[movi_id]

                    await query.answer("Seriyal o'chrldi")
                    await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)
            
                elif movi and movi['type'] == 'movi':
                    movi =  ram.movies_dict[movi_id]

                    # Delet comment
                    if movi['coments'].split('/')[-1].isnumeric:
                        try:
                            await bot.delete_message(chat_id = '@kino_bot_discuss', message_id = int(movi['coments'].split('/')[-1]))
                        except:
                            await query.answer("Comment message topilmadi")
                    
                        db.delet_movi(movi_id)
                        del ram.movies_dict[movi_id]

                        await query.answer("Kino o'chrldi")
                        await bot.delete_message(chat_id = query.from_user.id, message_id = query.message.message_id)





        
    else:
        await query.answer("Sizniki ruyxatdan utmaga")