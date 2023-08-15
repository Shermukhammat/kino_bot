from aiogram  import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, get_movi, bot, picsum, ibuttons, movi_add




@dp.message_handler(content_types = ['photo'], state = movi_add.set_thum)
async def catch_phot_caption(message : types.Message, state : FSMContext):
    id = message.from_user.id
    
    photo = message.photo[-1]

    # Download photo file
    file_path = await bot.get_file(photo.file_id)
    await bot.download_file(file_path.file_path, destination='data/pictures/image.jpg')
    url = picsum.save_photo('data/pictures/image.jpg')

    ram.set_thum(id, url = url)
    
    # await bot.send_photo(photo = open('data/pictures/image.jpg', 'rb'), chat_id = id, caption = "Ushlab oldim ...")
    
    await state.set_state(movi_add.set_save)
    await bot.send_photo(chat_id = message.from_user.id,
                         photo = open("./data/pictures/add_movi/save_movi.jpg", 'rb'),
                         caption = f"Caption phot qo'shldi", 
                         reply_markup = ibuttons.save_movi(back = 'back_set_thum'))
    