import sqlite3


def login(login, passw, signal):
    con = sqlite3.connect("Handler/UsersDB.db")
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация')
    else:
        signal.emit('Давай по новой миша все хуйня')

    cur.close()
    con.close()
