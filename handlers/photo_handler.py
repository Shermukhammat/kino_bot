from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, get_movi



@dp.message_handler(content_types = ['photo'])

async def catch_phot_caption(photo : Message, state : FSMContext):
    print(photo)