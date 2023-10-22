from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import db, dp, ram,bot, picsum, ibuttons, movi_add, CHANEL_ID, main_states, title_finder, info_cleaner, dbuttons, setting
import re
import asyncio

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    return "%d:%02d:%02d" % (hour, minutes, seconds)

@dp.message_handler(content_types = ContentTypes.VIDEO, state = movi_add.set_video)
async def get_movi_from_hand(message : types.Message, state : FSMContext):
    id = message.from_user.id
    if ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
    
        size = int((message.video.file_size / 1024) / 1024)
        file_id = message.video.file_id 
        caption = message.caption 
        caption = re.sub(r'.*\B@(?=\w{5,32}\b)[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)*.*', "", caption)
        caption = re.sub(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)", "", caption).strip() + "\n\n" + setting.data['bot_url']

        duration = convert(message.video.duration)
        message_id = message.message_id
        # creating thumb photo url
        media = await bot.download_file_by_id(message.video.thumb.file_id)
        with open("./data/pictures/photo.jpg", "wb") as file:
            file.write(media.getbuffer())
        thumb_url = picsum.save_photo('./data/pictures/photo.jpg')


        ram.update_movi_data(id, admin = True, message_id = message_id, duration = duration, thumb = thumb_url, size = size, info = caption)
        await state.set_state(movi_add.set_title)
        await bot.send_message(chat_id = id, text = "Kino nomni kiriting", reply_markup = dbuttons.back(), reply_to_message_id = message.message_id)
    
    # ram.save_movi(admin_id = admin_id, vide_id = video_file_id, duration = duration, size = video_size, phot_url = thumb_url)
    # await bot.delete_message(chat_id = admin_id, message_id = message.message_id)
        




@dp.message_handler(content_types = ContentTypes.VIDEO, state = main_states.input_avto_movi)
async def get_movi_from_hand(message : types.Message, state : FSMContext):
    id = message.from_user.id
    if ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
    
        size = int((message.video.file_size / 1024) / 1024)

        if size >= 300:
            # file_id = message.video.file_id 
            caption = message.caption
    
            
            title = title_finder(caption)
            if title:
                duration = convert(message.video.duration)
                message_id = message.message_id

                # creating thumb photo url
                media = await bot.download_file_by_id(message.video.thumb.file_id)
                with open("./data/pictures/photo.jpg", "wb") as file:
                    file.write(media.getbuffer())
                thumb_url = picsum.save_photo('./data/pictures/photo.jpg')
                info = info_cleaner(caption, bot = "@kino_qidiruvchi_robot")

                ram.admin_movies_add(admin_id = id, 
                                     movi_id = message_id, 
                                     caption = info, 
                                     duration = duration,
                                     size = size,
                                     thumbl_url = thumb_url)
                
                # print(ram.admin_movies)
                await message.reply("Kino savatga qo'shildi")
            else:
                await message.reply("ℹ️❌ kinoni nomi captiondan topilmadi")
        
        else:
            await message.reply("Film xajmi 300 Mb dan kam")




@dp.message_handler(content_types = ContentTypes.VIDEO, state = main_states.input_series_part)
async def get_part(message : types.Message, state : FSMContext):
    duration = convert(message.video.duration)
    message_id = message.message_id


    if ram.input_series.get(message.from_user.id):
        if ram.input_series[message.from_user.id]['last_part']:
            ram.input_series[message.from_user.id]['last_part'] += 1
            ram.series_set_part(part = ram.input_series[message.from_user.id]['last_part'], message_id = message.message_id,
                                user_id = message.from_user.id)
            
            await message.reply(f"{ram.input_series[message.from_user.id]['last_part']} - qisim qo'shiildi", 
                                reply_markup = dbuttons.seri_input_menu(save = True))
            
            # print(ram.input_series[message.from_user.id], "\n\n\n")
            
        else:
            ram.input_series[message.from_user.id]['last_part'] = 1
            ram.series_set_part(part = ram.input_series[message.from_user.id]['last_part'], message_id = message.message_id,
                                user_id = message.from_user.id)
            await message.reply(f"{ram.input_series[message.from_user.id]['last_part']} - qisim qo'shiildi", 
                                reply_markup = dbuttons.seri_input_menu(save = True))
            

@dp.message_handler(content_types = ContentTypes.VIDEO, state = main_states.input_video_manual)
async def get_part(message : types.Message, state : FSMContext):
    data = await bot.copy_message(from_chat_id = message.from_user.id, chat_id = CHANEL_ID, message_id = message.message_id)
    
    
    await bot.delete_message(chat_id = CHANEL_ID, message_id = setting.data['vide_manual'])
    
    setting.data['vide_manual'] = data.message_id
    setting.update()

    await state.finish()
    await bot.send_message(text = "qo'lanma menyusi", reply_markup = dbuttons.manual_edit(), chat_id = message.from_user.id)


@dp.message_handler(content_types = ContentTypes.VIDEO, state = main_states.input_user_movi)
async def cetch_movi_from_user(message : types.Message, state : FSMContext):
    message_id = message.message_id

    if ram.check_user(message.from_user.id):
        ram.users[message.from_user.id]['message'].append(message_id)

        message_data = await bot.send_sticker(chat_id = message.from_user.id, sticker = 'CAACAgIAAxkBAAI3sGU031I-nn2ofC9saOTUIoBxnJDOAALuFAAC41VQSThLiq0CE2G8MAQ')
        await asyncio.sleep(3)
        await bot.delete_message(chat_id = message.from_user.id, message_id = message_data.message_id)
    