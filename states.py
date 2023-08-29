from aiogram.dispatcher.filters.state import StatesGroup, State



class My_States(StatesGroup):
    movi_add_with_hand = State()
    movi_add_avto = State()


class get_movi_from_hand(StatesGroup):
    get_video = State()
    get_title = State()
    get_caption = State()
    get_caption_photo = State()



class add_movi(StatesGroup):
    chose_lang = State()
    set_video = State()
    set_title = State()
    set_info = State()
    set_thum = State()
    set_save = State()

class Add_Movi_Avto(StatesGroup):
    chose_lang = State()
    input_movies = State()


class Main_States(StatesGroup):
    input_avto_movi = State()
    admin_login = State()
    log_out_admin = State()
    input_chanle = State()