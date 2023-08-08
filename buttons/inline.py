from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class Inline_buttons:
    def __init__(self):
        pass

    def menu(self, admin = False):
        if not admin:
            buttons = [[InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬇️ Ko'proq", callback_data = "more")],
                        [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]]
        
            return InlineKeyboardMarkup(inline_keyboard = buttons)
        
        else:
            pass

    def more_menu(self, admin = False):
        if not admin:
            buttons = [[InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬆️ Kamroq", callback_data = "less")],
                       [InlineKeyboardButton(text = "📲 Aloqa", callback_data = "contact"), InlineKeyboardButton(text = "📈 Statistika", callback_data = "statistics")],
                       [InlineKeyboardButton(text = "🧪 Kino qo'shish", callback_data = "add_movi")],
                    
                       [InlineKeyboardButton(text = "🏆 Top 100", callback_data = "top"), InlineKeyboardButton(text = "⚡️ Primyeralar", callback_data = "premier")],
                       [InlineKeyboardButton(text = "⭐️ Saqlanganlar", callback_data = "saved"), InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random")],
                    #    [InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random")],
                    #    [[InlineKeyboardButton(text = "🧩 Filtir", callback_data = "filtir")]],
                       [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]
                    
                    ]





                # [InlineKeyboardButton(text = "⭐️ Saqlanganlar", callback_data = "saved"), InlineKeyboardButton(text = "⚡️ Primyeralar", callback_data = "premier")],
                #        [InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random"), InlineKeyboardButton(text = "🏆 Top 100", callback_data = "top")],
                #        [InlineKeyboardButton(text = "🧪 Kino qo'shish", callback_data = "add_movi"), InlineKeyboardButton(text = "📲 Aloqa", callback_data = "contact")],
                #        [InlineKeyboardButton(text = "📈 Statistika", callback_data = "statistics")]


            return InlineKeyboardMarkup(inline_keyboard = buttons)

        else:
            buttons = [[InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬆️ Kamroq", callback_data = "less")],
                       [ InlineKeyboardButton(text = "📈 Statistika", callback_data = "statistics")],
                       [InlineKeyboardButton(text = "🏆 Top 100", callback_data = "top"), InlineKeyboardButton(text = "⚡️ Primyeralar", callback_data = "premier")],
                       [InlineKeyboardButton(text = "⭐️ Saqlanganlar", callback_data = "saved"), InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random")],
                    #    [InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random")],
                    #    [[InlineKeyboardButton(text = "🧩 Filtir", callback_data = "filtir")]],
                       [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]
                    
                    ]
            
            return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def chose_lang(self, back = 'back'): #⬅️
        buttons = [[InlineKeyboardButton(text = 'O\'zbekcha', callback_data = 'uz'), InlineKeyboardButton(text = 'Ruscha', callback_data = 'ru'), InlineKeyboardButton(text = 'Inglizcha', callback_data = 'en')],
                   [InlineKeyboardButton(text = '⬅️ orqaga', callback_data = back)],
                   [InlineKeyboardButton(text = '❌', callback_data = 'delet')]]
        return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def ask_movi_input(self):
        buttons = [[InlineKeyboardButton(text = "🙏 Qo'lda", callback_data = "hand" ), InlineKeyboardButton(text = "♻️ Avtomatik", callback_data = "avto")],
                   [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
        
        return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def ask_button(self, admin = True, back = None, yes = 'yes', skip = 'skip'):
        if admin:
            buttons = [[InlineKeyboardButton(text = "Kiritish 🔤", callback_data = yes), InlineKeyboardButton(text = "O'tkazish ➡️", callback_data = skip)],
                       [InlineKeyboardButton(text = "⬅️ orqaga", callback_data = back)],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
            return InlineKeyboardMarkup(inline_keyboard = buttons)

    def delet(self, back = 'back'):
        return InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "⬅️ orqaga", callback_data = back)], [InlineKeyboardButton(text = "❌", callback_data = 'delet')]])

    
    def save_movi(self, admin = True, back = None):
        if admin:
            buttons = [[InlineKeyboardButton(text = "📥 Saqlash", callback_data = "save"), InlineKeyboardButton(text = "🗑 O'chrish", callback_data = 'delet_movi')],
                       [InlineKeyboardButton(text = "⬅️ orqaga", callback_data = back)],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
            return InlineKeyboardMarkup(inline_keyboard = buttons)









    def photo_caption(self):
        buttons = [[InlineKeyboardButton(text = "xa", callback_data = "yes"), InlineKeyboardButton(text = "yo'q", callback_data = "no")],
                   [InlineKeyboardButton(text = "Bekor qilish ❌", callback_data = 'delet')]]
  
        return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def change_state(self, head = False, last = False, back = 'back', next = 'next'):
        if last:
            buttons = [[InlineKeyboardButton(text = "<- Oldingi", callback_data = back)],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
        
            return InlineKeyboardMarkup(inline_keyboard = buttons)
        
        if head:
            buttons = [[InlineKeyboardButton(text = "Keyingi ->", callback_data = next)],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
        
            return InlineKeyboardMarkup(inline_keyboard = buttons)
        
        buttons = [[InlineKeyboardButton(text = "<- Oldingi", callback_data = back), InlineKeyboardButton(text = "Keyingi ->", callback_data = next)],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
        
        return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def add_movi(self, back = False):
        if back:
            buttons = [[InlineKeyboardButton(text = "Kinoni qo'shish", callback_data = 'add')],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
            return InlineKeyboardMarkup(inline_keyboard = buttons)
        buttons = [[InlineKeyboardButton(text = "<- orqaga", callback_data = 'back5'), InlineKeyboardButton(text = "Kinoni qo'shish", callback_data = 'add')],
                       [InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
        return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def delet_button(self):
        buttons = [[InlineKeyboardButton(text = "❌", callback_data = 'delet')]]
        return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    
    def next(self):
        buttons = [[InlineKeyboardButton(text = "<- orqaga", callback_data = 'back2'), InlineKeyboardButton(text = "Keyingsi ->", callback_data = 'next2')],
                    [InlineKeyboardButton(text = " x ", callback_data = 'delet')]]
        return InlineKeyboardMarkup(inline_keyboard = buttons)