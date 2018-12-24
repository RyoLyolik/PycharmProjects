import sqlite3
import time

def update_base():
    conn = sqlite3.connect('USERS.sqlite')
    cursor = conn.cursor()

    cur = conn.cursor()
    cur.execute("SELECT * FROM Us")
    rows = cur.fetchall()

    for i in range(len(rows)):
        rows[i] = list(rows[i])

    conn.commit()
    cursor.close()
    conn.close()
    return rows

def time_changes():
    while True:
        conn = sqlite3.connect('USERS.sqlite')
        cursor = conn.cursor()
        users = update_base()
        for user in users:
            if int(user[3]) > -10:
                cursor.execute('UPDATE Us SET bonus_time=' + '"' +str(int(user[3]) - 1)+ '"' + ' WHERE id=' + str(user[0]))
            if int(user[4]) > -10:
                cursor.execute('UPDATE Us SET work_time=' + '"' +str(int(user[4]) - 1) + '"' +' WHERE id=' + str(user[0]))
        cursor.close()
        conn.commit()
        conn.close()
        time.sleep(1)

time_changes()