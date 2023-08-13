from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from login import BOT_TOKEN, CHANEL_ID, TELEGRAPH_API_KEY, DISCUSS_CHANEL_ID
from data.base import Database
from data.access import RAM
from data.picsum import Picsum
from buttons.defolt import Defolt_buttons
from buttons.inline import Inline_buttons
from states import My_States, get_movi_from_hand, add_movi, Add_Movi_Avto
from data.searcher import Google

storage = MemoryStorage()
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot, storage = storage)
db = Database("./data/database.db")
ram = RAM(db)
google = Google(ram = ram)
dbuttons = Defolt_buttons()
ibuttons = Inline_buttons()
my_states = My_States()
movi_add = add_movi()
add_movi_avto = Add_Movi_Avto()

get_movi = get_movi_from_hand()
picsum = Picsum(token = TELEGRAPH_API_KEY)