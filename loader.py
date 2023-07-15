from aiogram import Bot, Dispatcher, types

from login import BOT_TOKEN


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler(commands = 'start')
# async def start2(message : types.Message):
#     await message.reply("salom2")