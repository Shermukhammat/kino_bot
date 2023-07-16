

class RAM:
    def __init__(self, database = None):
        self.db = database
        self.users = database.get_users()
        
    def check_user(self, id):
        if self.users.get(id) != None:
            return True
        return False
        