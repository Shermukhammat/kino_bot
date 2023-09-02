from datetime import datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class RAM:
    def __init__(self, database = None):
        self.db = database
        self.users = database.get_users()
        self.users_count = len(self.users)
        self.admins = database.get_admins()
        self.movies = database.get_movies()
        self.movies_dict = {movi['id'] : movi for movi in self.movies}
        self.movies_count = len(self.movies)
        self.movies_title = [movi['title'] for movi in self.movies]
        self.admin_movi = {}
        self.admins_input_movi_lang = {}
        self.admin_movies = {}
        self.user_movi = {}
        self.input_series = {}
        self.port = True
        self.block = {}

    def get_top_movies_index(self, limit : int = 10):
        likes =  [movi['like'] for movi in self.movies]
        indexs = []
        for n in range(limit):
            index = likes.index(max(likes))
            likes[index] = 0
            indexs.append(index)
        
        return indexs

        

    def get_bot_info(self):
        return f"Bot Foydalanuvchilar soni : {self.users_count}\nJami kinolar soni {self.movies_count}\nJami Seryallar soni : coming son ...\n\n@kino_qidiruvchi_robot"



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
            self.users_count += 1
            self.db.registir(id = id, name = name, registred = now(), lang = lang)
        else:
            del self.users[id]
            self.admins[id] = data
            self.db.registir(id = id, name = name, registred = now(), lang = lang, admin = True)
        
    
    def logout(self, id : int, name : str = None, lang : str = 'uz',  admin : bool = False):
        data = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : now()}
        if admin:
            del self.admins[id]
            self.users[id] = data
            
            self.db.delet_admin(id)
            self.db.registir(id = id, name = name, registred = now(), lang = lang)
        
    
    def get_info(self, id, admin = True):
        if not admin:
            return self.users[id]
        else:
            return self.admins[id]
    
    def get_user(self, id : int = None):
        return self.users[id]

    #del
    def bloc_user(self, id):
        respons = self.block.get(id)
        if respons != None:
            self.block[id] += 1
            return respons + 1
        self.block[id] = 1
        return 1
    
    #del
    def user_block_count(self, id):
        respons = self.block.get(id)
        if respons != None:
            return respons
        self.block[id] = 0
        return 0
    
    def admin_login(self, id : int, block : bool = False):
        if block:
            if self.block.get(id):
                self.block[id] += 1
            else:
                self.block[id] = 1

            return self.block[id]
        
        elif self.block.get(id):
            return self.block[id]
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
        self.movies_count += 1
        
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
        

    def update_movi_data(self, id, video_id = None, message_id = None, duration = None, size = None, thumb = None, admin = False, info = None):
        if admin and self.admin_movi.get(id) != None:
            self.admin_movi[id]['message_id'] = message_id
            self.admin_movi[id]['video_id'] = video_id
            self.admin_movi[id]['duration'] = duration
            self.admin_movi[id]['size'] =  size
            self.admin_movi[id]['thumb'] = thumb
            self.admin_movi[id]['caption'] = info
            

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
        self.admins_input_movi_lang[admin_id] = lang

    
    def admin_movies_add(self, admin_id : int = None, movi_id : int = None, caption : str = None, duration : str = None, size : int = None, thumbl_url : str = None):
        if self.admins_input_movi_lang.get(admin_id):
            data = {'message_id' : movi_id,
                    'caption' : caption,
                    'duration' : duration, 
                    'size' : size,
                    'thumb' : thumbl_url,
                    'lang' : self.admins_input_movi_lang[admin_id]}
            
            if self.admin_movies.get(admin_id):
                self.admin_movies[admin_id].append(data)
            else:
               self.admin_movies[admin_id] = [data]
    
    def get_admin_movies(self, id : int):
        if self.admin_movies.get(id):
            return self.admin_movies[id]
        else:
            return []

    def clean_admin_movies(self, id : int):
        if self.admin_movies.get(id):
            self.admin_movies[id] = []
            
    
    def get_movi(self, index : int):
        if self.movies_count > index:
            return self.movies[index]

    
    def creat_serie(self, lang : str = 'uz', id : int = None):
        data = {'id' : None,
                'lang' : lang,
                'title' : None,
                'parts_id' :{},
                'last_part' : None,
                'thumb' : None}
        self.input_series[id] = data 
    
    def series_set_title(self, title : str = None, id : int = None):
        if self.input_series.get(id):
            self.input_series[id]['title'] = title
    
    def series_set_info(self, message_id : int = None, user_id : int = None, thumbl : str = None):
        if self.input_series.get(user_id):
            self.input_series[user_id]['id'] = message_id
            self.input_series[user_id]['thumb'] = thumbl
    
    def series_set_part(self, part : int = None, message_id : int = None, user_id : int = None):
        if self.input_series.get(user_id):
            self.input_series[user_id]['parts_id'][part] = message_id
    
        
            
    


if __name__ == '__main__':
    print(now())