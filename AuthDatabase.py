import sqlite3, re, bcrypt

def main():
    user = None
    while user != 1 and user != 2:
        try:
            user = int(input('--- HELLO ---\n(Input 1 or 2)\n1. Login\n2. Sign up\n'))
        except ValueError:
            continue
    if user == 1:
        username = input('username: ')
        password = input('password: ')


    else:
        username = input('username: ')
        password = input('password: ')
        


def usernameValidator(username):
# Must start/end with Alphabets, can contain periods/underscores only in between.
# Alphabets are compulsory and must be a minmum of three. Min 3 chars, max 20.
    if pattern:= re.search(r'^(?=.{3,20}$)(?=([a-zA-Z][_.]?){3,})[a-zA-Z0-9]+([_.][a-zA-Z0-9]+)*$', username):
        return True
    else:
        return False

def database(username, password):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(username, password)')
    cur.execute('INSERT INTO users VALUES(?, ?)', (username, password))
    con.commit()

def pwHasher(password):
    return bcrypt.hashpw(b'password', bcrypt.gensalt(12))

if __name__ == '__main__':
    main()


