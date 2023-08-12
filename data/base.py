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
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('id' INTEGER PRIMARY KEY, 'title', 'caption', 'file_size' INTEGER, 'duration', 'like' INTEGER, 'dislike' INTEGER, 'coments', 'thum_url', 'lang');")
        
        print("database conected ...", end = '\r')
        
        conection.commit()
        conection.close()

    def add_movi(self, title = None, caption = None, message_id = None, duration = None, size = None, coment_url = None, thum_url = None, lang = 'uz'):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        try:
            caption = caption.replace("'", '"')
            title = title.replace("'", '"')
            match = f"INSERT INTO {self.movies} ('id', 'title', 'caption', 'file_size', 'duration', 'like', 'dislike', 'coments', 'thum_url', 'lang') VALUES ({message_id}, '{title}', '{caption}', {size}, '{duration}', 0, 0, '{coment_url}', '{thum_url}', '{lang}');"
            # print(match)
            cursor.execute(match)
            print(f"New movi {title} added ...")
        except:
            print(f"Can't added {title} ...")
        
        conection.commit()
        conection.close()

    
    def get_movies(self):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        movies = []

        match = f"SELECT * FROM {self.movies};"
        for row in cursor.execute(match):
            # print(row)
            id, title, caption, file_size, duration, like, dislike, coments, thum_url, lang = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
            movi =  {'id' : id, 
                          'title' : title, 
                          'caption' : caption, 
                          'size' : file_size,
                          'duration' : duration,
                          'like' : like,
                          'dislike' : dislike,
                          'coments' : coments,
                          'thum_url' : thum_url,
                          'lang' : lang}
            movies.append(movi)
            

        conection.commit()
        conection.close()
        
        return movies
    
    def like_movi(self, id : int = 0, like : int = 0, incres : bool = True):
        #UPDATE movies SET 'like' = 10 WHERE id == 2766;
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        cursor.execute(f"UPDATE {self.movies} SET like = {like} WHERE id == {id};")
            
        conection.commit()
        conection.close()
    
    def dislike_movi(self, id : int = 0, dislike : int = 0):
        #UPDATE movies SET 'like' = 10 WHERE id == 2766;
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        cursor.execute(f"UPDATE {self.movies} SET dislike = {dislike} WHERE id == {id};")
        
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
    # data_base.add_movi(title = "y'axs'hi \"kino3",
    #                    caption = "Yaxshi title2",
    #                    message_id = 18,
    #                    duration = '20:00',
    #                    size = 100,
    #                    coment_url = "htpp/telegram/17",
    #                    thum_url = "htpp:/telegraph.org/1345")
    print(data_base.get_movies())
    