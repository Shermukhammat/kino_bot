from loader import types, dp

@dp.message_handler(commands = 'start')
async def start(message : types.Message):
    await message.answer("salomlar")