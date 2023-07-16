from aiogram import Bot, Dispatcher, types

from login import BOT_TOKEN
from data.base import Database
from data.access import RAM

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)
db = Database("./data/database.db")
ram = RAM(db)

# @dp.message_handler(commands = 'start')
# async def start2(message : types.Message):
#     await message.reply("salom2")