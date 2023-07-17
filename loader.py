from aiogram import Bot, Dispatcher, types

from login import BOT_TOKEN
from data.base import Database
from data.access import RAM
from buttons.defolt import Defolt_buttons
from buttons.inline import Inline_buttons

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)
db = Database("./data/database.db")
ram = RAM(db)
dbuttons = Defolt_buttons()
ibuttons = Inline_buttons()