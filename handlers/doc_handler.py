from aiogram import types
from aiogram.types import ContentType
from loader import db, dp, ram, main_states, dbuttons



@dp.message_handler(content_types=ContentType.DOCUMENT, state = main_states.input_series_part)
async def handle_document(message: types.Message):
    if ram.input_series.get(message.from_user.id):
        if ram.input_series[message.from_user.id]['last_part']:
            ram.input_series[message.from_user.id]['last_part'] += 1
            ram.series_set_part(part = ram.input_series[message.from_user.id]['last_part'], message_id = message.message_id,
                                user_id = message.from_user.id)
            
            await message.reply(f"{ram.input_series[message.from_user.id]['last_part']} - qisim qo'shiildi", 
                                reply_markup = dbuttons.seri_input_menu(save = True))
            
            # print(ram.input_series[message.from_user.id], "\n\n\n")
            
        else:
            ram.input_series[message.from_user.id]['last_part'] = 1
            ram.series_set_part(part = ram.input_series[message.from_user.id]['last_part'], message_id = message.message_id,
                                user_id = message.from_user.id)
            await message.reply(f"{ram.input_series[message.from_user.id]['last_part']} - qisim qo'shiildi", 
                                reply_markup = dbuttons.seri_input_menu(save = True))
