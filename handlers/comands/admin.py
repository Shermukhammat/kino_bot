from aiogram.dispatcher import FSMContext
from loader import types, dp, ram, main_states, dbuttons

@dp.message_handler(commands = 'admin')
async def admin(message : types.Message, state : FSMContext):
    id = message.from_user.id
   
    if ram.check_user(id):
        if ram.admin_login(id) < 3:
            await state.set_state(main_states.admin_login)
            await message.answer("Admin panelga kirish uchun paro'lni kiriting", reply_markup = dbuttons.quite_admin_login())
        else:
            await message.answer("Iltimos keyinroq urinib ko'ring")
    
    elif ram.check_admin(id):
        await message.reply("Sizniki admin")
    else:
        # name = message.from_user.first_name
        # ram.registr(id = id, name = name)
        await message.answer(f"Sizniki ruyxatdan o'tmagan")



