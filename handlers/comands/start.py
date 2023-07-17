from loader import types, dp, ram

@dp.message_handler(commands = 'start')
async def start(message : types.Message):
    id = message.from_user.id
    
    if ram.check_user(id):
        user = ram.get_info(id)
        await message.answer(f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}")
    else:
        name = message.from_user.first_name
        ram.registr(id = id, name = name)
        await message.answer(f"Siznikiruyxatdan utdi ")