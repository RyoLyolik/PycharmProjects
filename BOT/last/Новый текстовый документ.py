﻿import vk_api
import time
import random
import commands


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


def replacer_line(file_name, line_num, text):
    lines = open(file_name, 'r', encoding="utf-8").readlines()
    lines[line_num] = text
    out = open(file_name, 'w', encoding="utf-8")
    out.writelines(lines)
    out.close()


vk = vk_api.VkApi(token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
vk._auth_token()

user = open('users.txt', 'r')
idss = open('allids.txt', 'r')
idc = open('allids.txt', 'a')
userc = open('users.txt', 'a')
ids = idss.read().split()
users = user.read()
users = users.split('\n')
users = [i.split(',') for i in users]
print(users)
print(ids)
print(str(type(2)))


class CommandsGenerate:
    def __init__(self):
        pass

    def random(self, name, list):
        ch = open('Commands_bot.py', 'a')
        replacer_line('gbot.py', 200,
                      "\n\n\t\t\telif body.lower()=='" + name + "':\n\t\t\t\tvk.method('messages.send', {'peer_id': id, 'message': random.choice(" + list + ")})\n\n\n")

    def halfchance(self, name, list):
        ch = open('Commands_bot.py', 'a')
        replacer_line('gbot.py', 200,
                      "\n\n\t\t\telif body.lower().split()[0]=='" + name + "': \n\n\t\t\t\t\tif body.lower().split()[1].isdigit and int(body.lower().split()[1]) <= float(users[n][1]): \n\t\t\t\t\tusers[n][1] = str(float(users[n][1])-int(body.lower().split()[1]))\n\t\t\t\t\trnd = random.choice(" + list + ")\n\t\t\t\t\tif rnd == body.lower().split()[2]:\n\t\t\t\t\t\tusers[n][1] = str(float(users[n][1])+(int(body.lower().split()[1])*2))\n\t\t\t\t\t\tvk.method('messages.send', {'peer_id': id, 'message': 'You are win ' + str(int(body.lower().split()[1])) + '\\nYour balance: ' + commands.bt(int(float(users[n][1])))})\n\t\t\t\t\telse: \n\t\t\t\t\t\tvk.method('messages.send', {'peer_id': id, 'message': 'You are lose ' + str(int(body.lower().split()[1])) + '\\nYour balance: ' + commands.bt(int(float(users[n][1])))})\n\n\n\n")


cg = CommandsGenerate()
cc = 0
wh = False

while True:
    cc += 1
    user = open('users.txt', 'r')
    idss = open('allids.txt', 'r')
    idc = open('allids.txt', 'a')
    userc = open('users.txt', 'a')
    ids = idss.read().split()
    users = user.read()
    users = users.split('\n')
    users = [i.split(',') for i in users]
    for us in range(len(users)):
        if len(users[us]) > 1:
            if int(users[us][3]) > -10:
                users[us][3] = str(int(users[us][3]) - 1)
            if int(users[us][4]) > -10:
                users[us][4] = str(int(users[us][4]) - 1)
            replace_line('users.txt', us, ','.join(users[us]) + '\n')

    messages = vk.method('messages.getConversations', {'out': 0, 'time_offset': 60, 'count': 100, 'filter': "unread"})
    if messages['count'] >= 1:

        id = messages['items'][0]['last_message']['from_id']
        usid = messages['items'][0]['last_message']['peer_id']
        body = messages['items'][0]['last_message']['text']

        if not str(id) in ids:
            wh = False
            if wh == False:
                if body.lower() == 'hello':
                    vk.method('messages.send', {'peer_id': id, 'message': 'User' + ',' + ' ''hi!' + str(usid)})
            if body.lower().split()[0] == 'регистрация':
                name = body.split()[1:]
                name = ' '.join(name)
                idc.write(' ' + str(usid))
                userc.write(str(usid) + ',' + '0' + ',' + '0' + ',' + '10,' + '10,' + '0,0,1000,0,10,' + name + '\n')
                vk.method('messages.send',
                          {'peer_id': id,
                           'message': 'Аккаунт создан. Теперь я буду обращаться к вам, как ' + name + '\nНапишите "команды" для списка команд'})
            else:
                vk.method('messages.send', {'peer_id': id,
                                            'message': 'Необходимо завести аккаунт. Для этого напишите: "регистрация <Ваше имя>"'})

        elif str(usid) in ids:

            print(body + '\n' + 'by: ' + users[ids.index(str(usid))][-1])
            wh = True
            n = ids.index(str(usid))
            users[n][1] = str(round(float(users[n][1]), 2))
            users[n][8] = str(round(float(users[n][8]), 2))
            if float(users[n][1]) >= 9999999999999:
                users[n][1] = '9999999999999'
            if body.lower() == 'hello':
                vk.method('messages.send', {'peer_id': id, 'message': users[n][-1] + ',' + ' ''hi!'})


            elif body.lower() == 'баланс':
                vk.method('messages.send', {'peer_id': id, 'message': users[n][-1] + ', Ваш баланс: ' + commands.bt(
                    int(float(users[n][1])))})




            elif body.lower().split()[0] == 'казино':
                summ = body.split()[1]
                if (str(summ) != 'все' and str(summ) != 'всё') and not str(summ).isdigit():
                    vk.method('messages.send', {'peer_id': id, 'message': 'Так нельзя'})
                else:
                    if not str(summ).isdigit():
                        summ = float(users[n][1])

                    summ = float(summ)
                    if summ > float(users[n][1]):
                        vk.method('messages.send', {'peer_id': id, 'message': 'Недостаточно денеГ'})
                    else:
                        if summ > 0:
                            users[n][1] = str(float(users[n][1]) - summ)
                            ch = random.choice(range(1, 51))
                            if ch == 1:
                                m = 0
                                summ *= m
                            elif ch >= 2 and ch <= 10:
                                m = 0.25
                                summ *= m
                            elif ch <= 25 and ch > 10:
                                m = 0.5
                                summ *= m
                            elif ch <= 30 and ch > 25:
                                m = 0.75
                                summ *= m
                            elif ch <= 40 and ch > 30:
                                m = 2
                                summ *= m
                            elif ch < 50 and ch > 40:
                                m = 5
                                summ *= m
                            elif ch == 50:
                                m = 50
                                summ *= m
                            users[n][1] = str(float(users[n][1]) + summ)
                            vk.method('messages.send', {'peer_id': id, 'message': 'Вам попался (х' + str(
                                m) + ')' + '\n' + 'Ваш баланс: ' + commands.bt(int(float(users[n][1])))})


            elif body.lower() == 'работать':
                if int(users[n][4]) <= 0 and int(float(users[n][6])) == 10:
                    vk.method('messages.send', {'peer_id': id, 'message': 'Вы устроились на новую работу'})
                    users[n][7] = str((int(float(users[n][7])) * 2.5))
                    users[n][6] = '0'
                elif int(float(users[n][6])) != 10 and int(users[n][4]) <= 0:
                    users[n][6] = str((int(float(users[n][6])) + 1))
                    users[n][1] = str(int(float(users[n][1])) + int(float(users[n][7])))
                    vk.method('messages.send', {'peer_id': id, 'message': 'Вы заработали ' + users[n][7]})
                    users[n][4] = '60'
                elif int(users[n][4]) > 0:
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'Выходные кончатся через ' + str(int(users[n][4]))})
            elif body.lower() == 'бонус':
                if int(users[n][3]) <= 0:
                    if random.choice('mmmr') == 'm':
                        p = random.choice([100, 100000, 100000, 500000000, 500000000, 500000000, 25000000000])
                        users[n][1] = str(float(users[n][1]) + p)
                        vk.method('messages.send',
                                  {'peer_id': id, 'message': 'Вы получили ' + commands.bt(
                                      p) + " $" + '\n' + 'Ваш баланс: ' + commands.bt(
                                      int(float(users[n][1])))})


                    else:
                        p = random.choice([2, 2, 10, 10, 10, 50, 50, 100])
                        users[n][2] = str(float(users[n][2]) + p)
                        vk.method('messages.send',
                                  {'peer_id': id, 'message': 'Вы получили ' + commands.bt(
                                      p) + " рейтинга" + '\n' + 'Ваш рейтинг ' + commands.bt(
                                      int(float(users[n][2])))})
                    users[n][3] = str(60)
                else:
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'До бонуса осталось:' + str(int(users[n][3]))})

            elif body.lower() == 'команды':
                vk.method('messages.send', {'peer_id': id,
                                            'message': 'Вот что я могу: \n' + 'Казино <сумма>\n' + 'Баланс \nБанк\nБанк положить\n Банк снять' + 'Работать \n' + 'Бонус \n' + 'имя <имя>\n' + '\n(Version: 0.05)'})
                if users[n][5] == 'Admin':
                    vk.method('messages.send', {'peer_id': id,
                                                'message': 'Доп команды для админов:\nПолучить <сумма>\nСоздать команду\nпомощь создать'})

            elif body.split()[0].lower() == 'имя':
                users[n][-1] = str(' '.join(body.split()[1:]))
                print(body)
                vk.method('messages.send', {'peer_id': id,
                                            'message': 'Имя изменено. Теперь я буду обращаться к вам, как ' + users[n][
                                                -1]})












            elif body.lower() == 'помощь создать':
                if users[n][5] == 'Admin':
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'Нужно написать: создать команду <parameters>\n\n'
                                                         'Параметры:\n'
                                                         '1. рандом <name> <первый рандомный элемент, ... , n-ый рандомный элемент>\n'
                                                         '2. 50%50 <name> <1st, 2nd> (Типа трейда вверх/вниз)'})

            elif body.lower() == 'профиль':
                vk.method('messages.send', {'peer_id': id,
                                            'message': 'Ваш профиль, ' + users[n][-1] + ':\n1. Ваш id: ' + users[n][
                                                0] + '\n2. Баланс:' + commands.bt(
                                                str(int(float(users[n][1])))) + '\n3. В банке ' + commands.bt(
                                                str(int(float(users[n][8])))) + '\n4. Рейтинг: ' + users[n][
                                                           2] + '\n4. Привилегия: ' + users[n][5]})
            elif body.lower() == 'кого-выебать':

                vk.method('messages.send',
                          {'peer_id': id,
                           'message': random.choice(["данила", "саунда", "гнома", "вована", "печеньку"])})





            elif body.lower().split()[:2] == ['создать', 'команду']:
                if users[n][5] == 'Admin':
                    all = body.lower().split()
                    if all[2] == 'рандом':
                        cg.random(all[3], all[4])
                        vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
                    elif all[2] == '50%50':
                        cg.halfchance(all[3], all[4])
                        vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})


            elif body.lower().split()[0] == 'получить':
                if users[n][5] == 'Admin' and body.lower().split()[1].isdigit():
                    users[n][1] = str(float(users[n][1]) + int(body.lower().split()[1].strip(
                        'asdfghjklqwertyuiopzxcvbnmфывапролдйцукенгшщзхъячсмитьбю?"}][;.>:{/!@#$%^&*()_+-=~`')))
                    vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})


            elif body.lower().split()[0] == 'передать':
                g = body.lower().split()
                if len(g) == 3 and g[2].isdigit() and int(float(users[n][1])) >= int(g[2]) and g[1] in ids and int(
                        g[2]) > 0:
                    users[n][1] = str(int(float(users[n][1])) - int(g[2]))
                    print(1)
                    users[ids.index(g[1])][1] = str(int(float(users[ids.index(g[1])][1])) + int(g[2]))
                    replace_line('users.txt', ids.index(str(g[1])), ','.join(users[ids.index(g[1])]) + '\n')
                    vk.method('messages.send',
                              {'peer_id': id,
                               'message': 'Вы передали игроку ' + users[ids.index(g[1])][-1] + ' ' + g[2] + ' $'})
                    vk.method('messages.send',
                              {'peer_id': g[1], 'message': 'Вам передал ' + users[n][-1] + ' ' + g[2] + ' $'})
                elif g[2].isdigit() and int(float(users[n][1])) < int(g[2]):
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'Недостаточно денег'})
                elif not g[1] in ids:
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'ID не существует'})
                else:
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'В боте это не предусмотренно'})


            elif body.lower() == 'банк':
                vk.method('messages.send',
                          {'peer_id': id, 'message': 'В банке ' + commands.bt(str(int(float(users[n][8]))))})
            elif body.lower().split()[:2] == ['банк', 'положить'] and len(body.lower().split()) >= 3 and \
                    body.lower().split()[2].isdigit():
                if int(float(users[n][1])) >= int(float(body.lower().split()[2])):
                    users[n][8] = str(int(float(users[n][8])) + int(float(body.lower().split()[2])))
                    users[n][1] = str(int(float(users[n][1])) - int(float(body.lower().split()[2])))
                    vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
                else:
                    vk.method('messages.send', {'peer_id': id, 'message': 'Недостаточно денег'})


            elif body.lower().split()[:2] == ['банк', 'снять'] and len(body.lower().split()) >= 3 and \
                    body.lower().split()[2].isdigit():
                if int(float(users[n][1])) <= int(float(body.lower().split()[2])):
                    users[n][8] = str(int(float(users[n][8])) - int(float(body.lower().split()[2])))
                    users[n][1] = str(int(float(users[n][1])) + int(float(body.lower().split()[2])))
                    vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
                else:
                    vk.method('messages.send', {'peer_id': id, 'message': 'Недостаточно денег в банке'})

            else:
                vk.method('messages.send', {'peer_id': id, 'message': '?'})
            replace_line('users.txt', ids.index(str(usid)), ','.join(users[n]) + '\n')

            elif body.lower().sp

    # print(cc)
    if cc % 60 == 0:
        cc = 0
        for i in range(len(users)):
            if len(users[i]) > 1:
                users[i][8] = str(float(users[i][8]) * 1.1)
                replace_line('users.txt', i, ','.join(users[i]) + '\n')

    time.sleep(1)