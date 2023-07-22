from datetime import datetime

def now():
    now = datetime.now()
    return str(now.strftime("%d.%m.%Y %H:%M"))

class RAM:
    def __init__(self, database = None):
        self.db = database
        self.users = database.get_users()
        self.admins = database.get_admins()

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



if __name__ == '__main__':
    print(now())