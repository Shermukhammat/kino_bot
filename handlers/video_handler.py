from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import db, dp, ram, my_states, get_movi

@dp.message_handler(content_types = ContentTypes.VIDEO, state = get_movi.get_video)
async def get_movi_from_hand(message : types.Message, state : FSMContext):
    admin_id = message.from_user.id
    admin = ram.get_info(id, admin = True)

    print(message.video)
    
    video_size = int((message.video.file_size / 1024) / 1024)
    video_file_id = message.video.file_id
    caption = message.caption 

    ram.save_movi()

    await state.set_state(get_movi.next)
    await message.reply(f"{admin['name']} endi kinoning nomni kiriting.")

