from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from login import BOT_TOKEN, CHANEL_ID
from data.base import Database
from data.access import RAM
from buttons.defolt import Defolt_buttons
from buttons.inline import Inline_buttons
from states import My_States, get_movi_from_hand

storage = MemoryStorage()
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot, storage = storage)
db = Database("./data/database.db")
ram = RAM(db)
dbuttons = Defolt_buttons()
ibuttons = Inline_buttons()
my_states = My_States()

get_movi = get_movi_from_hand()
