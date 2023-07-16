from loader import types, dp, ram

@dp.message_handler(commands = 'start')
async def start(message : types.Message):
    print(message.from_user.first_name)
    id = message.from_user.id
    
    if ram.check_user(id):
        await message.answer("Siz ruyxatdan utgan")
    else:
        await message.answer("Sizniki ro'yxatdan o'tmagan")