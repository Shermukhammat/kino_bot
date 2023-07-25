from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes
from loader import db, dp, ram, my_states

@dp.message_handler(content_types = ContentTypes.VIDEO, state = my_states.movi_add_with_hand)
async def get_movi_from_hand(message : types.Message, state : FSMContext):
    await message.reply("Ushladi")