from aiogram  import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, get_movi, bot, picsum, ibuttons, movi_add, dbuttons, main_states




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
    await message.reply("Caption phot qo'shldi, oxirgi qadam kinoni saqlaymizmi?", reply_markup = dbuttons.save_movi())


@dp.message_handler(content_types = ['photo'], state = main_states.input_serie_info)
async def catch_series_info_phot(message : types.Message, state : FSMContext):
    id = message.from_user.id
    
    photo = message.photo[-1]
    info = message.caption

    # Download photo file
    file_path = await bot.get_file(photo.file_id)
    await bot.download_file(file_path.file_path, destination='data/pictures/image.jpg')
    url = picsum.save_photo('data/pictures/image.jpg')

    ram.series_set_info(message_id = message.message_id, user_id = message.from_user.id,
                        thumbl = url)
    
    await state.set_state(main_states.input_series_part)
    await message.answer("Endi esa 1-qism videosni tashlang", reply_markup = dbuttons.seri_input_menu())



    # await bot.send_photo(chat_id = message.from_user.id,
    #                      photo = open("./data/pictures/add_movi/save_movi.jpg", 'rb'),
    #                      caption = f"Caption phot qo'shldi", 
    #                      reply_markup = ibuttons.save_movi(back = 'back_set_thum'))
    