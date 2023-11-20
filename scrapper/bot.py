from aiogram import Dispatcher, Bot, types, executor
from config import API_TOKEN


bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def start(message: types.Message):
    if message.text == 'test':
        await bot.send_document(chat_id = message.from_user.id, document = 'http://uzmovi.com/download/e4y5z5x543r24484y2u2q254p204x2x2r223v2u213w2n4343676l4n4v4c4t284j4d4q3u5h4w4q534o4m3h5i5w4h4q5q3m4j464l384i5u2h4l4x2')
    else:
        await message.answer(message.text, reply_markup = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text="test")]], resize_keyboard=True))

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)