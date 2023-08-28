from datetime import datetime
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputMediaVideo
import aiohttp

API_TOKEN = '6646323098:AAG9l0z4nIzEFN8LD2Ec7t_P4GREKDSBw0s'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['video'])
async def send_welcome(message: types.Message):
    await message.reply("Kino yuborish boshlandi")
    
    start = datetime.now()

    # url = f"http://fayllar1.ru/20/kinolar/Quvnoq%20chexra%201957%20480p%20O'zbek%20tilida%20(asilmedia.net).mp4"
    url = 'https://samplelib.com/lib/preview/mp4/sample-30s.mp4'

    # url = 'https://filetransfer.io/data-package/8VomrZd9/download'
    await bot.send_video(chat_id = message.from_user.id, video = open('video.mp4', 'rb'))
    
    await message.reply(f"run time : {datetime.now() - start}")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text, supports_streaming = True)


executor.start_polling(dp, skip_updates=True)