from loader import types, dp



@dp.message_handler()
async def core_message_handler(message : types.Message):
    await message.answer("slaom")