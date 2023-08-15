from datetime import datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class RAM:
    def __init__(self, database = None):
        self.db = database
        self.users = database.get_users()
        self.admins = database.get_admins()
        self.movies = database.get_movies()
        self.movies_title = [movi['title'] for movi in self.movies]
        self.admin_movi = {}
        self.admin_movies = {}
        self.user_movi = {}
        # self.admin_a_movi = {}
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
    
    
    def add_search_movi(self, message_id =  None, title = None, caption = None, size = None, duration = None, coments = None, thum_url = None, lang = 'uz'):
        data = {'id' : message_id, 
                'title' : title, 
                'caption' : caption, 
                'size' : size,
                'duration' : duration,
                'like' : 0,
                'dislike' : 0,
                'coments' : coments,
                'thum_url' : thum_url,
                'lang' : lang}
        
        self.movies.append(data)
        self.movies_title.append(title)
        
    def like_movi(self, index : int, incres : bool = True):
        if incres:
            self.movies[index]['like'] += 1
        else:
            self.movies[index]['like'] -= 1
    
    def dislike_movi(self, index : int, incres : bool = True):
        if incres:
            self.movies[index]['dislike'] += 1
        else:
            self.movies[index]['dislike'] -= 1
        
    
    def creat_movi(self, id, lang = 'uz', admin = False):
        if admin:
            self.admin_movi[id] = {'message_id' : None,
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
            
    def set_thum(self, id, url = None, admin = True):
        if admin and self.admin_movi.get(id) != None:
            self.admin_movi[id]['thumb'] = url
            

    def save_movi(self, id, admin = True, message_id = None, caption = None, thum_url = None):
        pass


    def admin_movies_set_lang(self, lang : str = 'uz', admin_id : int = None):
        if self.admin_movies.get(admin_id):
            self.admin_movies[admin_id]['lang'] = lang
        else:
            self.admin_movies[admin_id] = {'movies' : [], 'lang' : lang}
    
    def admin_movies_add(self, admin_id : int = None, movi_id : int = None, caption : str = None, duration : str = None, size : int = None, thumbl_url : str = None):
        if self.admin_movies.get(admin_id):
            data = {'message_id' : movi_id,
                    'caption' : caption,
                    'duration' : duration, 
                    'size' : size,
                    'thumb' : thumbl_url}
            self.admin_movies[admin_id]['lang']['movies'].append(data)
    # def update_title(self, id, title):
    #     self.admin_a_movi[id]['title'] = title

    # def update_caption(self, id, caption):
    #     self.admin_a_movi[id]['caption'] = caption

    # def update_phot_url(self, id, photo_url = None):
    #     self.admin_a_movi[id]['thumb'] = photo_url
    
    def get_movi(self, id, admin = True):
        if admin:
            if self.admin_movi.get(id):
                return self.admin_movi[id]
            return {}
        return {}
            
    


if __name__ == '__main__':
    print(now())