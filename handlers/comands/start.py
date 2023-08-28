from loader import types, dp, ram, bot
# from aiogram import Bot


@dp.message_handler(commands = 'start')
async def start(message : types.Message):
    id = message.from_user.id
    
    # bot = Bot.get_current()
    # bot.get_current()
    # bot.get


    if ram.check_user(id):
        user = ram.get_info(id, admin = False)
        await message.answer(f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}")
    
    elif ram.check_admin(id):
        pass
    
    else:
        name = message.from_user.first_name
        ram.registr(id = id, name = name)
        await message.answer(f"Siznikiruyxatdan utdi ")