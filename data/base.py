import sqlite3

class Database:
    def __init__(self, file_name, users_tabel = 'users', admins_table = 'admins', movies = 'movies'):
        self.file = file_name
        self.users = users_tabel
        self.admins = admins_table
        self.movies = movies
        
        conection = sqlite3.connect(file_name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('id' INTEGER , 'name', 'lang', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.admins} ('id' INTEGER , 'name', 'lang', 'registred');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('id' INTEGER PRIMARY KEY, 'file_id', 'title', 'caption', 'file_size' INTEGER, 'duration', 'like' INTEGER, 'dislike' INTEGER, 'coments');")
        
        print("database conected ...")
        
        conection.commit()
        conection.close()

    def add_user_movi(self, title = None, caption = None, thumb_url = None, file_id = None, duration = None, size = None, coment = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        try:
            caption = caption.replace("'", '"')
            title = title.replace("'", '"')
            match = f"INSERT INTO {self.movies} ('file_id', 'title', 'caption', 'file_size', 'duration', 'like', 'dislike', 'coments') VALUES ('{file_id}', '{title}', '{caption}', {size}, '{duration}', 0, 0, '{coment}');"
            # print(match)
            cursor.execute(match)
            print(f"New movi {title} added ...")
        except:
            print(f"Can't added {title} ...")
        
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
    
    def get_admins(self):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        admins_data = {}

        match = f"SELECT * FROM {self.admins};"
        for row in cursor.execute(match):
            id, name, lang, registred_time = row[0], row[1], row[2], row[3]
            admins_data[id] = {'name' : name, 'lang' : lang, 'where' : 'none', 'action' : 'none', 'registred' : registred_time}
            # print(row) 
        conection.commit()
        conection.close()

        return admins_data
    

    def registir(self, id = None, name = None, registred = None, lang = 'uz', admin = False):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        name = name.replace("'", '"')
        if False == admin:
            match = f"INSERT INTO {self.users} ('id', 'name', 'lang', 'registred') VALUES ({id}, '{name}', '{lang}', '{registred}');"
            cursor.execute(match)
            print(f'New user {name}')
        else:
            match = f"INSERT INTO {self.admins} ('id', 'name', 'lang', 'registred') VALUES ({id}, '{name}', '{lang}', '{registred}');"
            match2 = f"DELETE  FROM {self.users} WHERE id == {id};"

            cursor.execute(match)
            cursor.execute(match2)
            
            print(f'New uadminser {name}')

        conection.commit()
        conection.close()
    
    


if __name__ == '__main__':
    data_base = Database('database.db')
    # data = data_base.get_users()
    data_base.add_user_movi(title = "Blah", 
                            caption = "Yaxshi kino",
                            thumb_url = "thubl htpp/:bfmef d",
                            file_id = 'file id fjvvehf93hb2480ghi',
                            duration = '12:20 minut',
                            size = 100,
                            coment = "Comentsdmfebs")
    