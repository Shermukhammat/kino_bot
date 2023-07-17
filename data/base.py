import sqlite3

class Database:
    def __init__(self, file_name, users_tabel = 'users', admins_table = 'admins'):
        self.file = file_name
        self.users = users_tabel
        self.admins = admins_table
        
        conection = sqlite3.connect(file_name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('id' INTEGER , 'name', 'lang', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.admins} ('id' INTEGER , 'name', 'lang', 'registred');")
        
        print("database conected ...")
        
        conection.commit()
        conection.close()
    
    def get_users(self):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        users_data = {}

        match = f"SELECT * FROM {self.users};"
        for row in cursor.execute(match):
            id, name, lang, registred_time = row[0], row[1], row[2], row[3]
            users_data[id] = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : registred_time}
            # print(row) 
        conection.commit()
        conection.close()
        return users_data
    

    def registir(self, id = None, name = None, registred = None, lang = 'uz', admin = False):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        name = name.replace("'", '"')
        if not admin:
            match = f"INSERT INTO {self.users} ('id', 'name', 'lang', 'registred') VALUES ({id}, '{name}', '{lang}', '{registred}');"
            cursor.execute(match)
            print(f'New user {name}')
        else:
            pass

        conection.commit()
        conection.close()
    
    


if __name__ == '__main__':
    data_base = Database('database.db')
    data = data_base.get_users()
    print(data)