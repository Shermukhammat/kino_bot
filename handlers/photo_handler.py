from aiogram  import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, get_movi, bot, picsum, ibuttons




@dp.message_handler(content_types = ['photo'], state = get_movi.get_caption_photo)

async def catch_phot_caption(message : types.Message, state : FSMContext):
    id = message.from_user.id
    
    photo = message.photo[-1]

    # Download photo file
    file_path = await bot.get_file(photo.file_id)
    await bot.download_file(file_path.file_path, destination='data/pictures/image.jpg')
    url = picsum.save_photo('data/pictures/image.jpg')

    ram.update_phot_url(id, photo_url = url)
    
    # await bot.send_photo(photo = open('data/pictures/image.jpg', 'rb'), chat_id = id, caption = "Ushlab oldim ...")
    await message.reply("Caption phot qo'shldi", reply_markup = ibuttons.add_movi())
