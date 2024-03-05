import sqlite3
database = 'myDatabase.db'
conn = sqlite3.connect(database)
c = conn.cursor()
print('db created sucessfully.')


def create_table():
    c.execute("create table user_login(Username varchar, password varchar)")
    conn.commit()
    
def enter():
    username = input('enter username: ')
    password = input('enter password: ')
    c.execute("""insert into user_login(username, password)
                values(?, ?)
              """, (username, password))
    
    conn.commit()
    
create_table()
enter()
    





