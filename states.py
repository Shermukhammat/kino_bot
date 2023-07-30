from aiogram.dispatcher.filters.state import StatesGroup, State



class My_States(StatesGroup):
    movi_add_with_hand = State()
    movi_add_avto = State()


class get_movi_from_hand(StatesGroup):
    get_video = State()
    get_title = State()
    get_caption = State()
    get_caption_photo = State()

