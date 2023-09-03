from aiogram import types
from aiogram.types import ContentType
from loader import db, dp, ram, main_states, dbuttons
import time
import asyncio


@dp.message_handler(content_types=ContentType.DOCUMENT, state = main_states.input_series_part)
async def handle_document(message: types.Message):
    if ram.input_series.get(message.from_user.id):
        message.message_id

        if ram.input_series[message.from_user.id]['last_part']:
            ram.input_series[message.from_user.id]['last_part'] += 1
            ram.series_set_part(part = ram.input_series[message.from_user.id]['last_part'], message_id = message.message_id,
                                user_id = message.from_user.id)
            
            await message.reply(f"{ram.input_series[message.from_user.id]['last_part']} - qisim qo'shiildi", 
                                reply_markup = dbuttons.seri_input_menu(save = True))
            
            
            # Sort mesages
            data = ram.input_series[message.from_user.id]
            parts_id = [id for id in data['parts_id'].values()]
            parts_id.sort()
        
            sorted_part = {}
            n = 0
            for id in parts_id:
                n += 1
                sorted_part[n] = id
        
            data['parts_id'] = sorted_part 
            # ram.input_series[message.from_user.id] = data
            
            
            # print(ram.input_series[message.from_user.id], "\n\n\n")

            
        else:
            ram.input_series[message.from_user.id]['last_part'] = 1
            ram.series_set_part(part = ram.input_series[message.from_user.id]['last_part'], message_id = message.message_id,
                                user_id = message.from_user.id)
            await message.reply(f"{ram.input_series[message.from_user.id]['last_part']} - qisim qo'shiildi", 
                                reply_markup = dbuttons.seri_input_menu(save = True))
