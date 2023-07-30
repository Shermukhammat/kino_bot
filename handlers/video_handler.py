from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import db, dp, ram, my_states, get_movi, bot, picsum, ibuttons

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    return "%d:%02d:%02d" % (hour, minutes, seconds)

@dp.message_handler(content_types = ContentTypes.VIDEO, state = get_movi.get_video)
async def get_movi_from_hand(message : types.Message, state : FSMContext):
    admin_id = message.from_user.id
    admin = ram.get_info(admin_id, admin = True)
    
    video_size = int((message.video.file_size / 1024) / 1024)
    video_file_id = message.video.file_id
    caption = message.caption 

    media = await bot.download_file_by_id(message.video.thumb.file_id)
    duration = convert(message.video.duration)
    with open("photo.jpg", "wb") as file:
        file.write(media.getbuffer())
        thumb_url = picsum.save_photo('photo.jpg')
        # print(thumb_url)

    ram.save_movi(admin_id = admin_id, vide_id = video_file_id, duration = duration, size = video_size, phot_url = thumb_url)

    # await bot.delete_message(chat_id = admin_id, message_id = message.message_id)
    await bot.send_video(video = video_file_id, caption = "| o o o", chat_id = admin_id, reply_markup = ibuttons.change_state(head = True, next = 'next1'))

