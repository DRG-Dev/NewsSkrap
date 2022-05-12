import sqlite3

def login(login, passw, signal):
    con = sqlite3.connect("Handler/UsersDB.db")
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name ="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        signal.emit('Успешная авторизация')
    else:
        signal.emit('Данные введены неверно')

    cur.close()
    con.close()
def register(login, passw, signal):
    con = sqlite3.connect("Handler/UsersDB.db")
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name ="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой логин уже используется')
    elif value == []:
        cur.execute(f"INSERT INTO users (name,password) VALUES('{login}','{passw}')")
        signal.emit('Вы успешно зарегестрировались')
        con.commit()

    cur.close()
    con.close()
