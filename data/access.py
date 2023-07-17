from datetime import datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class RAM:
    def __init__(self, database = None):
        self.db = database
        self.users = database.get_users()
        
    def check_user(self, id):
        if self.users.get(id) != None:
            return True
        return False
    
    def registr(self, id = None, name = None, lang = 'uz', admin = False):
        data = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : now()}
        if not admin:
            self.users[id] = data
            self.db.registir(id = id, name = name, registred = now(), lang = lang)
        else:
            pass
    
    def get_info(self, id, admin = False):
        if not admin:
            return self.users[id]
        else:
            pass



if __name__ == '__main__':
    print(now())