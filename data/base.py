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
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('id' INTEGER PRIMARY KEY, 'title', 'caption', 'file_size' INTEGER, 'duration', 'like' INTEGER, 'dislike' INTEGER, 'coments', 'thum_url', 'lang', 'mode');")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS series ('id' INTEGER PRIMARY KEY, 'title', 'like' INTEGER, 'dislike' INTEGER, 'coments', 'thum_url', 'lang');")
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS saved (user_id, movie_id);")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS parts (serie_id, part_id, part_num);")

        cursor.execute(f"CREATE TABLE IF NOT EXISTS liked (user_id, movie_id);")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS disliked (user_id, movie_id);")

        # print("database conected ...", end = '\r')
        
        conection.commit()
        conection.close()

    def save_movi(self, user_id : int = None, movie_id : int = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        try:
            match = f"INSERT INTO saved ('user_id', 'movie_id') VALUES ({user_id}, {movie_id});"
            # print(match)
            cursor.execute(match)
        except:
            print(f"Can't save movie, id : {movie_id} ...")
        
        conection.commit()
        conection.close()

    def delet_saved(self, user_id : int = None, movie_id : int = None):
        #DELETE  FROM {self.users} WHERE id == {id};
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        try:
            match = f"DELETE FROM saved WHERE user_id == {user_id} AND movie_id == {movie_id};"
            # print(match)
            cursor.execute(match)
        except:
            print(f"Can't deleted movie, id : {movie_id} user id : {user_id} ...")
        
        conection.commit()
        conection.close()


    def get_saved_len(self, id : int):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        n = 0
        match = f"SELECT movie_id FROM saved WHERE user_id == {id};"
        for row in cursor.execute(match):
            n+=1
        conection.commit()
        conection.close()
        return n


    def get_saved(self, id : int):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        ids = []
        match = f"SELECT movie_id FROM saved WHERE user_id == {id};"
        for row in cursor.execute(match):
            ids.append(row[0])


        conection.commit()
        conection.close()

        return ids

    def get_movi(self, id : int):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        match = f"SELECT * FROM {self.movies} WHERE id == {id};"
        for row in cursor.execute(match):
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
                return movi
        
        conection.commit()
        conection.close()



    def add_movi(self, title = None, caption = None, message_id = None, duration = None, size = None, coment_url = None, thum_url = None, lang = 'uz', mode : str = 'hand'):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        try:
            caption = caption.replace("'", '"')
            title = title.replace("'", '"')
            match = f"INSERT INTO {self.movies} ('id', 'title', 'caption', 'file_size', 'duration', 'like', 'dislike', 'coments', 'thum_url', 'lang', 'mode') VALUES ({message_id}, '{title}', '{caption}', {size}, '{duration}', 0, 0, '{coment_url}', '{thum_url}', '{lang}', '{mode}');"
            # print(match)
            cursor.execute(match)
            print(f"New movi {title} added ...")
        except:
            print(f"Can't added {title} ...")
        
        conection.commit()
        conection.close()

    def add_seri(self, title = None, message_id : int = None, coment_url : str = None, thumb : str = None, lang : str = 'uz', parts_id : dict = {}, like = 0, dislike = 0):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        try:
            for part, id in parts_id.items():
                cursor.execute(f"INSERT INTO parts ('serie_id', 'part_id', 'part_num') VALUES ({message_id}, {id}, {part});")
            title = title.replace("'", '"')
            match = f"INSERT INTO series ('id', 'title', 'like' , 'dislike', 'coments', 'thum_url', 'lang') VALUES ({message_id}, '{title}', {like}, {dislike}, '{coment_url}', '{thumb}', '{lang}');"
            # print(match)
            cursor.execute(match)
            print(f"New serire {title} added ...")
        except:
            print(f"Can't added serie {title} ...")
        
        conection.commit()
        conection.close()
    
    def get_series(self):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        series = []

        match = f"SELECT * FROM series;"
        rows = cursor.execute(match)
        for row in rows.fetchall():
            id, title, like, dislike, coments, thum_url, lang = row[0], row[1], row[2], row[3], row[4], row[5], row[6]
            parts_id = {}
            for row2 in cursor.execute(f"SELECT part_id, part_num FROM parts WHERE serie_id == {id};"):
                part_id, part_num = row2[0], row2[1]
                parts_id[part_num] = part_id
                # parts (serie_id, part_id, part_num)

            seri =  {'id' : id,
                     'title' : title, 
                     'like' : like,
                     'dislike' : dislike,
                     'coments' : coments,
                     'thum_url' : thum_url,
                     'parts_id' : parts_id,
                     'lang' : lang,
                     'type' : 'seri'}
            series.append(seri)
        
            

        conection.commit()
        conection.close()

        return series

    def get_top_movies(self, limit : int = 10):
        #SELECT * FROM movies ORDER BY like DESC LIMIT 10;
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        movies = []

        match = f"SELECT * FROM {self.movies} ORDER BY like DESC LIMIT {limit};"
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
                          'lang' : lang,
                          'type' : 'movi'}
            movies.append(movi)
            

        conection.commit()
        conection.close()
        
        return movies
    
    
    def is_saved(self, user_id : int = None, movie_id : int = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        for row in cursor.execute(f"SELECT * FROM saved WHERE user_id == {user_id} AND movie_id == {movie_id};"):
            conection.commit()
            conection.close()

            return True

        conection.commit()
        conection.close()

        return False

    def is_like(self, user_id : int = None, movie_id : int = None):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        for row in cursor.execute(f"SELECT * FROM liked WHERE user_id == {user_id} AND movie_id == {movie_id};"):
            conection.commit()
            conection.close()

            return 'like'
        
        for row in cursor.execute(f"SELECT * FROM disliked WHERE user_id == {user_id} AND movie_id == {movie_id};"):
            conection.commit()
            conection.close()

            return 'dislike'
        
        conection.commit()
        conection.close()


    def like_movi(self, user_id : int = None, movie_id : int = None, like_count : int = None, remove : bool = False, incres : bool = True):
        #UPDATE movies SET 'like' = 10 WHERE id == 2766;
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        if remove:
            match = f"DELETE FROM liked WHERE user_id == {user_id} AND movie_id == {movie_id};"
            cursor.execute(match)
            cursor.execute(f"UPDATE {self.movies} SET like = {like_count - 1} WHERE id == {movie_id};")
        else:
            match = f"INSERT INTO liked ('user_id', 'movie_id') VALUES ({user_id}, {movie_id});"
            cursor.execute(match)
            cursor.execute(f"UPDATE {self.movies} SET like = {like_count + 1} WHERE id == {movie_id};")
            
        conection.commit()
        conection.close()
    
    def dislike_movi(self, user_id : int = None, movie_id : int = None, like_count : int = None, remove : bool = False):
        #UPDATE movies SET 'like' = 10 WHERE id == 2766;
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()

        if remove:
            match = f"DELETE FROM disliked WHERE user_id == {user_id} AND movie_id == {movie_id};"
            cursor.execute(match)
            cursor.execute(f"UPDATE {self.movies} SET dislike = {like_count - 1} WHERE id == {movie_id};")
        else:
            match = f"INSERT INTO disliked ('user_id', 'movie_id') VALUES ({user_id}, {movie_id});"
            cursor.execute(match)
            cursor.execute(f"UPDATE {self.movies} SET dislike = {like_count + 1} WHERE id == {movie_id};")
            
        conection.commit()
        conection.close()
    


    
    def get_users(self):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        users_data = {}

        match = f"SELECT * FROM {self.users};"
        for row in cursor.execute(match):
            id, name, lang, registred_time = row[0], row[1], row[2], row[3]
            users_data[id] = {'name' : name, 'lang' : lang, 'where' : 'none',  'iwhere' : 'none', 'action' : 'none', 'registred' : registred_time}
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
            admins_data[id] = {'name' : name, 'lang' : lang, 'where' : 'none', 'iwhere' : 'none', 'action' : 'none', 'registred' : registred_time}
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
    
    def delet_admin(self, id : int):
        conection = sqlite3.connect(self.file)
        cursor = conection.cursor()
        
        cursor.execute(f"DELETE  FROM {self.admins} WHERE id == {id};")

        conection.commit()
        conection.close()


if __name__ == '__main__':
    data_base = Database('data/database.db')
    # data = data_base.get_users()
    # data_base.add_movi(title = "y'axs'hi \"kino3",
    #                    caption = "Yaxshi title2",
    #                    message_id = 18,
    #                    duration = '20:00',
    #                    size = 100,
    #                    coment_url = "htpp/telegram/17",
    #                    thum_url = "htpp:/telegraph.org/1345")
    # print(data_base.get_movies())

    # print(data_base.is_like(user_id = 1661189380, movie_id = 2805))   
    # data_base.add_seri(title = 'arkein', message_id = 3, coment_url = 'coment', thumb = 'www.thum.org', lang = 'en', parts_id = {1 : 11, 2 : 12, 3 : 13, 4 : 14, 5 : 15, 6 : 16})
    for ser in data_base.get_series():
        print(ser)