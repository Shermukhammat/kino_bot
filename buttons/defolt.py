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
                      [KeyboardButton(text = "📂 Media"), KeyboardButton(text = "📦 Review")],
                      [KeyboardButton(text = "✉️ Xabarlar"), KeyboardButton(text = "⚙️ Sozlamalar")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    
    def media(self):
        buttons = [[KeyboardButton(text = "🎬 Kino qo'shish"), KeyboardButton(text = "📺 Serial qo'shish")],
                   [KeyboardButton(text = "🔥 Primyeralarni taxrirlash"), KeyboardButton(text = "⬅️ Orqaga")]]
        
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