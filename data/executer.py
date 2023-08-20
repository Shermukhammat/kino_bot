import sqlite3


if __name__ == '__main__':
    conection = sqlite3.connect("database.db")
    cursor = conection.cursor()

    for row in cursor.execute("SELECT * FROM admins;"):
        print(row)
    
    conection.commit()
    conection.close()