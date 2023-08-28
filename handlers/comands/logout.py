from aiogram.dispatcher import FSMContext
from loader import types, dp, ram, main_states, dbuttons


@dp.message_handler(commands = 'logout')
async def logout(message : types.Message, state : FSMContext):
    if ram.check_admin(message.from_user.id):
        await state.set_state(main_states.log_out_admin)
        await message.answer("Xaiqatdan ham admin paneldan chiqshni hohlaysizmi?", reply_markup = dbuttons.admin_logout())