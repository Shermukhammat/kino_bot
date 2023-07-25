from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, ram, bot, ibuttons, dbuttons, my_states, get_movi




@dp.callback_query_handler()

async def query_handler(query : types.CallbackQuery, state : FSMContext):
    text = query.data
    id = query.from_user.id
    message_id = query.message.message_id

    if ram.check_user(id):
        if text == 'more':
            await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.more_menu())

        elif text == 'less':
            await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.menu())
    
    # elif ram.check_admin(id):
    #     if text == 'more':
    #         await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.more_menu(admin = True))

    #     elif text == 'less':
    #         await bot.edit_message_reply_markup(chat_id = id, message_id = message_id, reply_markup = ibuttons.menu())
    
    
    elif ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
        name = admin['name']
        where = admin['where']

        if admin['where'] == 'none':
            admin['where'] = 'head_menu'
            # await query.answer(f"Bosh menu", reply_markup = dbuttons.menu(admin = True))
            await bot.send_message(text = "salom", chat_id = id, reply_markup = dbuttons.menu(admin = True))

        # elif admin['where'] == 'head_menu':
        #     pass

        elif admin['where'] == 'media':
            if text == 'delet':
                await bot.delete_message(chat_id = id, message_id = message_id)

            elif text == 'hand':
                await state.set_state(get_movi.get_video)
                await bot.send_message(text = "Ok, Kinoyingzni tashlang!", chat_id = id)

    else:
        print(print("Sizniki  utmagan"))