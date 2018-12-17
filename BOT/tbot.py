import config
import json
import sqlite3
import commands
import time
import telebot

token = '624990039:AAGTYXZ6cpD-GRCmgKLXDfBhrEz7WUPpUYk'
bot = telebot.TeleBot(token=token)

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


def save_changes(id, data):
    conn = sqlite3.connect('USERS.sqlite')
    cursor = conn.cursor()

    rowss = 'id money rate bonus_time work_time privilage work_upgrade pay bank work_or_no x50_bonus cheats rating_mult hunger name'

    for row in range(len(rowss.split())):
        cursor.execute(
            'UPDATE Us SET ' + str(rowss.split()[row]) + '=' + '"' + str(data[row]) + '"' + ' WHERE id=' + '"' + str(
                id) + '"')
    conn.commit()
    cursor.close()
    conn.close()


@bot.message_handler(content_types=["text"])
def reply(message):
    users = update_base()
    ids = [str(user[0]) for user in users]
    id_ = str(message.from_user.id)
    body = message.text
    if str(id_) in ids:
        n = ids.index(id_)
        answer = commands.check_message(body, users, ids, n)
        for i in range(len(users)):
            users[i] = tuple(users[i])
        if answer is not None:
            if isinstance(answer, dict):
                pass
                # bot.send_message(message.chat.id, answer)
                # vk.method("messages.send", {"peer_id": id, "message": "Клавиатура выведена", "keyboard": answer})
            elif isinstance(answer, tuple):
                pass
                # vk.method('messages.send',
                #           {'peer_id': id, "attachment": answer[0], "message": answer[1]})
            else:
                bot.send_message(message.chat.id, answer)
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
VALUES (''' + str(id_) + ''', 0, 1, 10, 10,"User",1,1000,0,0,0,0,1,10,''' + '''"''' + name + '''"''' + ''');''')
            cursor.close()
            conn.commit()
            conn.close()
            bot.send_message(message.chat.id,
                             'Аккаунт создан. Теперь я буду обращаться к вам, как ' + name + '\nНапишите "помощь" для списка команд')
        else:
            bot.send_message(message.chat.id,
                             'Необходимо завести аккаунт. Для этого напишите: "регистрация <Ваше имя>"')
    for user in users:
        save_changes(user[0], user)

if __name__ == '__main__':
    print('Bot get started')
    bot.polling(none_stop=True)
