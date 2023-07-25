from aiogram.dispatcher import FSMContext
from loader import types, dp, ram

@dp.message_handler(commands = 'admin')
async def admin(message : types.Message):
    id = message.from_user.id
   
    if ram.check_user(id):
        user = ram.get_info(id)

        count = ram.user_block_count(id)

        if count == 0:
            user['action'] = 'sign_admin'
            await message.answer(f"Ukam admin bo'lishni xoxlisanmi 😏? Ko'dni kirit unda")
        
        elif count <= 3:
            user['action'] = 'sign_admin'
            await message.answer(f"Ukam ko'dni kirit") 

        else:
            await message.answer("Ukam bloklanding ...")
    
    elif ram.check_admin(id):
        await message.reply("Sizniki admin")
    else:
        name = message.from_user.first_name
        ram.registr(id = id, name = name)
        await message.answer(f"Sizniki ruyxatdan utdi ")



