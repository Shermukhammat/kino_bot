from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import db, dp, ram,bot, picsum, ibuttons, movi_add, CHANEL_ID, main_states, title_finder, info_cleaner, dbuttons, setting
import re

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



        