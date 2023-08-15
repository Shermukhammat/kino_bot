from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import db, dp, ram,bot, picsum, ibuttons, movi_add, CHANEL_ID, add_movi_avto, main_states
import csv

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
        duration = convert(message.video.duration)
        message_id = message.message_id
        
        # creating thumb photo url
        media = await bot.download_file_by_id(message.video.thumb.file_id)
        with open("./data/pictures/photo.jpg", "wb") as file:
            file.write(media.getbuffer())
        thumb_url = picsum.save_photo('./data/pictures/photo.jpg')


        ram.update_movi_data(id, admin = True, message_id = message_id, duration = duration, thumb = thumb_url, size = size)
        await state.set_state(movi_add.set_title)
        await bot.send_photo(chat_id = id,
                                 photo = open("./data/pictures/add_movi/input_title.jpg", 'rb'),
                                 caption = "Kino nomni kiriting",
                                 reply_markup = ibuttons.delet(back = 'back_set_video'))
    # ram.save_movi(admin_id = admin_id, vide_id = video_file_id, duration = duration, size = video_size, phot_url = thumb_url)
    # await bot.delete_message(chat_id = admin_id, message_id = message.message_id)
        




@dp.message_handler(content_types = ContentTypes.VIDEO, state = main_states.input_avto_movi)
async def get_movi_from_hand(message : types.Message, state : FSMContext):
    id = message.from_user.id
    if ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
    
        size = int((message.video.file_size / 1024) / 1024)

        if size >= 300:
            file_id = message.video.file_id 
            caption = message.caption
            duration = convert(message.video.duration)
            message_id = message.message_id 
        

            # creating thumb photo url
            media = await bot.download_file_by_id(message.video.thumb.file_id)
            with open("./data/pictures/photo.jpg", "wb") as file:
                file.write(media.getbuffer())
            thumb_url = picsum.save_photo('./data/pictures/photo.jpg')

            ram.admin_movies_add(admin_id = id)
        
        else:
            await message.answer("Film xajmi 300 Mb dan kam")



        