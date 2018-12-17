import json
import sqlite3

import commands
import vk_api
import time

# from telebot
# import telebot
# import speech

vk = vk_api.VkApi(token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
vk._auth_token()


def update_base():
    conn = sqlite3.connect('USERS.sqlite')
    cursor = conn.cursor()

    cur = conn.cursor()
    cur.execute("SELECT * FROM Us")
    rows = cur.fetchall()

    for i in range(len(rows)):
        rows[i] = list(rows[i])

    cursor.close()
    conn.close()

    return rows


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_button(label="Помощь", color="primary")],
        [get_button(label="Казино всё", color="negative")],
        [get_button(label="Баланс", color="primary"), get_button(label="Профиль", color="default")],
        [get_button(label="Работать", color="positive"), get_button(label="Бонус", color="positive")],
        [get_button(label="Есть", color="default")]

    ]
}


def save_changes(id, data):
    conn = sqlite3.connect('USERS.sqlite')
    cursor = conn.cursor()

    rows = 'id money rate bonus_time work_time privilage work_upgrade pay bank work_or_no x50_bonus cheats rating_mult hunger name'

    for row in range(len(rows.split())):
        # print(rows.split()[row], data[row])
        # print('UPDATE Us SET '+str(rows.split()[row])+'='+str(data[row])+' WHERE id='+str(id))
        cursor.execute(
            'UPDATE Us SET ' + str(rows.split()[row]) + '=' + '"' + str(data[row]) + '"' + ' WHERE id=' + str(id))

    conn.commit()
    cursor.close()
    conn.close()



keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
while True:
    messages = vk.method('messages.getConversations', {'out': 0, 'time_offset': 60, 'count': 100, 'filter': "unread"})
    users = update_base()
    if messages['count'] >= 1:
        id = messages['items'][0]['last_message']['from_id']
        usid = messages['items'][0]['last_message']['peer_id']
        body = messages['items'][0]['last_message']['text']
        id = str(id)

        ids = [user[0] for user in users]
        if id in ids:
            n = ids.index(id)
            answer = commands.check_message(body, users, ids, n)
            for i in range(len(users)):
                users[i] = tuple(users[i])


            if answer is not None:
                if isinstance(answer, dict):
                    vk.method("messages.send", {"peer_id": id, "message": "Клавиатура выведена", "keyboard": answer})
                elif isinstance(answer,tuple):
                    vk.method('messages.send',
                              {'peer_id': id, "attachment": answer[0], "message": answer[1]})
                else:
                    vk.method('messages.send', {'peer_id': id, 'message': answer})
        else:
            if body.lower().split()[0] == 'регистрация':
                name = body.split()[1:]
                name = ' '.join(name)
                # idc.write(' ' + str(usid))  # 15
                # userc.write(str(
                #     usid) + ',' + '0' + ',' + '0' + ',' + '10,' + '10,' + 'User,0,1000,0,0,0,0,0,1,10,' + name + '\n')

                conn = sqlite3.connect('USERS.sqlite')
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO Us (id,money,rate,bonus_time,work_time,privilage,work_upgrade,pay,bank,work_or_no,x50_bonus, cheats, rating_mult, hunger, name)
VALUES (''' + str(id) + ''', 0, 1, 10, 10,"User",1,1000,0,0,0,0,1,10,'''+'''"'''+name+'''"'''+''');''')
                cursor.close()
                conn.commit()
                conn.close()

                vk.method('messages.send',
                          {'peer_id': id,
                           'message': 'Аккаунт создан. Теперь я буду обращаться к вам, как ' + name + '\nНапишите "помощь" для списка команд'})
            else:
                vk.method('messages.send', {'peer_id': id,
                                            'message': 'Необходимо завести аккаунт. Для этого напишите: "регистрация <Ваше имя>"'})

    for user in users:
        save_changes(user[0], user)

    # conn = sqlite3.connect('USERS.sqlite')
    # cursor = conn.cursor()
    # for user in users:
    #     cursor.execute('UPDATE Us SET bonus_time='+str(int(user[3])-1)+' WHERE id='+str(user[0]))
    #     cursor.execute('UPDATE Us SET work_time=' + str(int(user[4])-1) + ' WHERE id=' + str(user[0]))
    # cursor.close()
    # conn.commit()
    # conn.close()

    time.sleep(1)
