from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class Defolt_buttons:
    def __init__(self):
        pass

    def menu(self, admin = False):
        if not admin:
            buttons = [[KeyboardButton(text="🎛 Menu"), KeyboardButton(text = "⚙️ Sozlamalar")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        else:
            buttons =[[KeyboardButton(text = "🎛 Menu")],
                      [KeyboardButton(text = "📂 Media"), KeyboardButton(text = "✉️ Xabarlar")],
                      [KeyboardButton(text = "  ------  "), KeyboardButton(text = "⚙️ Sozlamalar")],
                      [KeyboardButton(text = "📈 Xisobot")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    
    def media(self):
        buttons = [[KeyboardButton(text = " ------------- ")],
                   [KeyboardButton(text = "⚡️ Primyeralar"), KeyboardButton(text = "🧮 Kodli kinolar")],
                   [KeyboardButton(text = "🎬 Kino qo'shish"), KeyboardButton(text = "📺 Serial qo'shish")],
                   [KeyboardButton(text = "⬅️ Orqaga")]]
        
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def onli_back(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "⬅️ Orqaga")]], resize_keyboard = True)

    def primyer(self):
        buttons = [[KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]] 
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def seri_input_menu(self, save : bool = False):
        if save:
            buttons = [[KeyboardButton(text = "🧩 Oldingi qism")],
                       [KeyboardButton(text = "💾♻️ Saqlash"), KeyboardButton(text = "🗑♻️ Tozalash")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]], resize_keyboard = True)

    def user_input_movi(self):
        buttons = [[KeyboardButton(text = "🚀 jo'natish")], [KeyboardButton(text = "⬅️ Orqaga")]]

        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def add_movi(self, mode = 'none'):
        if mode == 'none':
            buttons = [[KeyboardButton(text = "♻️ Avtomatik"), KeyboardButton(text = "👊 Qo'lda")],
                       [KeyboardButton(text = "💾♻️ Saqlash"), KeyboardButton(text = "🗑♻️ O'chrish")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True) 
        if mode == 'avto':
            buttons = [[KeyboardButton(text = '🔵 Avtomatik'), KeyboardButton(text = "👊 Qo'lda")],
                       [KeyboardButton(text = "💾♻️ Saqlash"), KeyboardButton(text = "🗑♻️ O'chrish")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        if mode == 'hend':
            buttons = [[KeyboardButton(text = "♻️ Avtomatik"), KeyboardButton(text = "👊 Qo'lda 🔵")],
                       [KeyboardButton(text = "💾♻️ Saqlash"), KeyboardButton(text = "🗑♻️ O'chrish")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        
    def chose_movi_input_type(self, admin : bool = True):
        if admin:
            buttons = [[KeyboardButton(text = '♻️ Avtomatik'), KeyboardButton(text = "👊 Qo'lda")],
                       [KeyboardButton(text = "⬅️ Orqaga")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        
    def chose_lang(self):
        buttons = [[KeyboardButton(text = "🇺🇿 O'zbekcha"), KeyboardButton(text = "🇷🇺 Ruscha"), KeyboardButton(text = "🇬🇧 Inglizcha")],
                   [KeyboardButton(text = "⬅️ Orqaga")]]
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def avto_input_movi_menu(self):
        buttons = [[KeyboardButton(text = "🛠 Ishlov berish")],
                   [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🪓 Bekor qilish")]]
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def input_video(self):
        buttons = [[KeyboardButton(text = "! yordam")],
                   [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🪓 Bekor qilish")]]
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def back(self, skip : bool = False):
        if skip:
            return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "O'tkazish ➡️")], [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🪓 Bekor qilish")]], resize_keyboard = True)
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🪓 Bekor qilish")]], resize_keyboard = True)
    
    def save_movi(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "🗃 Saqlash")], [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🪓 Bekor qilish")]], resize_keyboard = True)
    
    def quite_admin_login(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "⬅️ Orqaga")]], resize_keyboard = True)
    
    def admin_logout(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🚶 Chiqish")]], resize_keyboard = True)
    
    def settings(self, admin : bool = True, mute : bool = False):
        if admin:
            if mute:
                mute_button = "🔇 Bildrishnoma"
            
            else:
                mute_button = "🔉 Bildrishnoma"
            
            buttons = [[KeyboardButton(text = "🤖 Bot Info")],
                       [KeyboardButton(text = "📡 Kanallar"), KeyboardButton(text = "📓 Qo'lanma")],
                       [KeyboardButton(text = "🔐 Parol"), KeyboardButton(text = mute_button)],
                       [KeyboardButton(text = "⬅️ Orqaga")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        
        else:
            pass
    
    def manual_edit(self):
        buttons = [[KeyboardButton(text = "📝 Yozuvli qo'lanma"), KeyboardButton(text = "🎞 Video qo'lanma")],
                   [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)

    def input_menu(self):
        return ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]], resize_keyboard = True)
    
    def movies_code_menu(self):
        buttons = [[KeyboardButton(text = "🆕 qo'shish"), KeyboardButton(text = "🔄 tahrirlash")],
                   [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)