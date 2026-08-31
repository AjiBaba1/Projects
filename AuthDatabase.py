import sqlite3, re, bcrypt

def main():
     while True:
        try:
            user = int(input('\n--- HELLO ---\n(Input 1 or 2)\n1. Login\n2. Sign up\n'))
        except ValueError:
            continue

        if user == 1:
            username = input('username: ')
            password = input('password: ')
            if dbMatch(username) is None:
                print('\nIncorrect username or password')
            else:
                hashedpw = dbPassword(username)
                if pwMatch(password, hashedpw):
                    exit(f'Login successful\nWelcome {username}')
                else:
                    print('\nIncorrect username or password')

        elif user == 2:
            username = input('username: ')
            password = input('password: ')

            if usernameValidator(username) is True:
                try:
                    if dbMatch(username) is None:
                        password = pwHasher(password)
                        dbStore(username, password)
                        exit(f'\nRegistration Sucessful\nWelcome {username}')
                    else:
                        print('\nUser already exists')
                #For first user
                except sqlite3.OperationalError:
                    password = pwHasher(password)
                    dbStore(username, password)
                    exit(f'\nRegistration Sucessful\nWelcome {username}')
            else:
                if (username.startswith('_') or username.startswith('.')) or (username.endswith('_') or username.endswith('.')):
                    print('\nInvalid username: Cannot begin or end with special characters')

                elif ('__') in username or ('..') in username or ('._') in username or ('_.') in username:
                    print('\nInvalid username: Cannot contain consecutive special characters')

                else:
                    print('\nInvalid username: Can ONLY contain Alphabets, Numbers, and periods/underscores')

def usernameValidator(username):
# Must start/end with Alphabets, can contain periods/underscores only in between.
# Alphabets are compulsory and must be a minmum of three. Min 3 chars, max 20.
    if pattern:= re.search(r'^(?=.{3,20}$)(?=([a-zA-Z][_.]?){3,})[a-zA-Z0-9]+([_.][a-zA-Z0-9]+)*$', username):
        return True
    else:
        return False

def dbStore(username, password):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users(username, password)')
    cur.execute('INSERT INTO users VALUES(?, ?)', (username, password))
    con.commit()

def dbMatch(username):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    match = cur.execute('SELECT username FROM users WHERE username = ?', (username,))
    return match.fetchone()

def dbPassword(username):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    sql = cur.execute('SELECT password FROM users WHERE username = ?', (username,))
    return sql.fetchone()

def pwHasher(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12))

def pwMatch(password, hashedpw):
    hashedpw = str(hashedpw).strip("(),b''")
    return bcrypt.checkpw(password.encode('utf-8'), hashedpw.encode('utf-8'))

if __name__ == '__main__':
    main()