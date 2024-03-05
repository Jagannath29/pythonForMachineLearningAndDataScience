import sqlite3
import bcrypt 
database = 'myDatabase.db'
conn = sqlite3.connect(database)
c = conn.cursor()
print('db created sucessfully.')


    
c.execute("""CREATE TABLE IF NOT EXISTS myDatabase(id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL)""")
conn.commit()
    


def user_registration( username, email, password):
    pass_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    c.execute("""INSERT INTO myDatabase(username, email, password)
              VALUES(?, ?, ?)""",(username,email,pass_hash))
    conn.commit()
    
    
def user_login(email, password):
    c.execute("SELECT pass_hash FROM myDatabase WHERE email=?", (email, ))
    row = c.fetchone()
    try:
        if row:
            stored_hash = row[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                print('Login sucessful')
                
        #     else:
        #         print("Invalid Email or password")
                
        # else:
        #     print("Invalid Email or password")
    except ValueError as e:
        print(e)
        
        
def update_password(email, current_pass, new_pass):
    c.execute("SELECT pass_hash FROM myDatabase where email=?", (email,))
    row = c.fetchone()
    if row and bcrypt.checkpw(current_pass.encode('utf-8'), row[0]):
        new_has_pass = bcrypt.hashpw(new_pass.encode('utf-8'), bcrypt.gensalt())
        
        c.execute('UPDATE myDatabase SET pass_hash=? WHERE email=?', (new_has_pass, email))
        conn.commit()
        print('Password changed successfully')
        
    else:
        print('Invalid email or password')
        
def delete_account(email, password):
    c.execute("SELECT pass_hash FROM myDatabase WHERE email=?", (email,))
    row = c.fetchone()
    if row and bcrypt.checkpw(password.encode('utf-8'), row[0]):
        c.execute("DELETE FROM myDatabase WHERE email=?", (email,))
        conn.commit()
        print("Account deleted successfully")
    else:
        print("Invalid email or password")

        
        
user = input('Enter user name: \n')
email = input('Enter email: \n')
password = input('enter password.\n')
new_pass = input('Update your password: ')

user_registration(user, email, password)
user_login(user, password)
update_password(user, password, new_pass)
delete_account(user, password)

conn.close()
        

        
    

    





