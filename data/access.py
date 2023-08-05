from datetime import datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class RAM:
    def __init__(self, database = None):
        self.db = database
        self.users = database.get_users()
        self.admins = database.get_admins()
        self.admin_movi = {}
        self.admin_a_movi = {}
        self.port = True

        self.block = {}
        
    def check_user(self, id):
        if self.users.get(id) != None:
            return True
        return False
    
    def check_admin(self, id):
        if self.admins.get(id) != None:
            return True
        return False
    
    def registr(self, id = None, name = None, lang = 'uz', admin = False):
        data = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : now()}
        # print(data)
        if False == admin:
            self.users[id] = data
            self.db.registir(id = id, name = name, registred = now(), lang = lang)
        else:
            del self.users[id]
            self.admins[id] = data
            self.db.registir(id = id, name = name, registred = now(), lang = lang, admin = True)
        
    
    def get_info(self, id, admin = False):
        if not admin:
            return self.users[id]
        else:
            return self.admins[id]

    def bloc_user(self, id):
        respons = self.block.get(id)
        if respons != None:
            self.block[id] += 1
            return respons + 1
        self.block[id] = 1
        return 1
    
    def user_block_count(self, id):
        respons = self.block.get(id)
        if respons != None:
            return respons
        self.block[id] = 0
        return 0

    def creat_movi(self, id, lang = 'uz', admin = False):
        if admin:
            self.admin_movi[id] = {'video_id' : None,
                                   'message_id' : None,
                              'caption' : None,
                              'title' : None,
                              'duration' : None, 
                              'size' : None,
                              'thumb' : None,
                              'lang' : lang}
        
        
    def delet_movi(self, id, admin = False):
        if admin and self.admin_movi.get(id) != None:
                del self.admin_movi[id]
        
    
    def update_movi_data(self, id, video_id = None, message_id = None, duration = None, size = None, thumb = None, admin = False):
        if admin and self.admin_movi.get(id) != None:
            self.admin_movi[id]['message_id'] = message_id
            self.admin_movi[id]['video_id'] = video_id
            self.admin_movi[id]['duration'] = duration
            self.admin_movi[id]['size'] =  size
            self.admin_movi[id]['thumb'] = thumb
    
    def set_title(self, id, title = None, admin = False):
        if admin and self.admin_movi.get(id) != None:
            # print(title)
            self.admin_movi[id]['title'] = title
    
    def set_info(self, id, caption = None, admin = False):
        if admin and self.admin_movi.get(id) != None:
            self.admin_movi[id]['caption'] = caption
        
    # def update_title(self, id, title):
    #     self.admin_a_movi[id]['title'] = title

    # def update_caption(self, id, caption):
    #     self.admin_a_movi[id]['caption'] = caption

    # def update_phot_url(self, id, photo_url = None):
    #     self.admin_a_movi[id]['thumb'] = photo_url
    
    def get_movi(self, id):
        return self.admin_a_movi[id]
    


if __name__ == '__main__':
    print(now())