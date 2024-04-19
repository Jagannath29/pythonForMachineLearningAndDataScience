import sqlite3
import bcrypt

# Database setup
conn = sqlite3.connect('myDb.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS myDb (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL UNIQUE,
             email TEXT NOT NULL UNIQUE,
             password_hash TEXT NOT NULL)''')
conn.commit()



def register_user(username, email, password):
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    c.execute("INSERT INTO myDb (username, email, password_hash) VALUES (?, ?, ?)",
              (username, email, password_hash))
    conn.commit()



def login_user(username, password):
    c.execute("SELECT password_hash FROM myDb WHERE username=?", (username,))
    row = c.fetchone()
    if row:
        stored_hash = row[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            print("Login successful")
        else:
            print("Invalid username or password")
    else:
        print("Invalid username or password")



def update_password(username, current_password, new_password):
    c.execute("SELECT password_hash FROM myDb WHERE username=?", (username,))
    row = c.fetchone()
    if row and bcrypt.checkpw(current_password.encode('utf-8'), row[0]):
        new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        c.execute("UPDATE myDb SET password_hash=? WHERE username=?", (new_password_hash, username))
        conn.commit()
        print("Password updated successfully")
    else:
        print("Invalid username or password")



def delete_account(username, password):
    c.execute("SELECT password_hash FROM myDb WHERE username=?", (username,))
    row = c.fetchone()
    if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
        c.execute("DELETE FROM myDb WHERE username=?", (username,))
        conn.commit()
        print("Account deleted successfully")
    else:
        print("Invalid username or password")

user = input('Enter user name: \n')
email = input('Enter email: \n')
password = input('enter password.\n')
new_pass = input('Update your password: ')

register_user(user, email, password)
login_user(user, password)
update_password(user, password, new_pass)
delete_account(user, password)

for row in c.execute("select * from myDb"):
    print(row)
conn.close()




