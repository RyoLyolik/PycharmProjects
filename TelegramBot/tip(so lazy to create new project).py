import vk_api
import time
import random
import commands
import json
import requests
import grouptest
import speech
import fx
import apiai

def convert_base(num, from_base = 10, to_base = 10):
    # first convert to decimal number
    print(from_base)
    n = int(str(num), int(from_base))
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(n)
    if n < to_base:
        print(n,1)
        return alphabet[n]
    else:
        print(alphabet[n% to_base], 'alpabet %')
        return convert_base(n // to_base, 10, to_base) + alphabet[n % to_base]

from yandex import Translater

token = 'trnsl.1.1.20180822T035034Z.c4e6b0734a1501db.3c10535039452db4d70963681df09234674e4b33'
all_lang = ['az','sq','am','en','ar','hy','af','eu','ba','be','bn','my',
                          'bg','bs','cy','hu','vi','ht','gl','nl','mrj','el','ka','gu',
                           'da','he','yi','id','ga','it','is','es','kk','kn','ca','ky',
                           'zh','ko','xh','km','lo','la','lv','lt','lb','mg','ms','ml',
                           'mt','mk','mi','mr','mhr','mn','de','ne','no','pa','pap','fa',
                           'pl','pt','ro','ru','ceb','sr','si','sk','sl','sw','su','tg',
                           'th','tl','ta','tt','te','tr','udm','uz','uk','ur','fi','fr',
                           'hi','hr','cs','sv','gd','et','eo','jv','ja']


def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()
def replace_line_bu(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] += text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def replacer_line(file_name, line_num, text):
    lines = open(file_name, 'r', encoding="utf-8").readlines()
    lines[line_num] = text
    out = open(file_name, 'w',encoding="utf-8")
    out.writelines(lines)
    out.close()




vk = vk_api.VkApi(token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
vk._auth_token()
# vk = vk_api.VkApi(login='89605187783', password='N1524360798n')
# vk.auth()


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
    [get_button(label="Баланс", color="primary"),get_button(label="Профиль", color="default")],
    [get_button(label="Работать", color="positive"),get_button(label="Бонус", color="positive")],
    [get_button(label="Есть", color="default")]


    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
print(keyboard)

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


def typer(arg):
    if arg == '0':
        return 'id'
    elif arg == '1':
        return 'money'
    elif arg == '2':
        return 'рейтинг'
    elif arg == '3':
        return 'время до бонуса'
    elif arg == '4':
        return 'время до окончания выходных'
    elif arg == '5':
        return 'привилегия'
    elif arg == '6':
        return 'Как скоро повышение(1 - нескоро, 10 - прямо сейчас)'
    elif arg == '7':
        return 'зарплата'
    elif arg == '8':
        return 'деньги в банке'
    elif arg == '9':
        return 'пока что ничего'
    elif arg == '10':
        return 'работал ли игрок вообще'

    elif arg == '11':
        return 'выпадало ли игроку х50'
    elif arg == '12':
        return 'вводил ли игрок хоть один читкод'
    elif arg == '13':
        return 'рейтинг множитель'

    elif arg == '14':
        return 'голод'
    elif arg == '15':
        return 'имя'



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
gs = False

while True:
    ans = False
    try:
        cc += 1

        # bis = open('bisnes.json','r+',encoding='utf-8')

        user = open('users.txt', 'r')
        idss = open('allids.txt', 'r')
        idc = open('allids.txt', 'a')
        userc = open('users.txt', 'a')

        # dat = json.loads(bis.read())
        # print(dat)
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


        if gs == False:
            print('\nBot get started')
            gs = True

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
                    idc.write(' ' + str(usid))                                                                    #15
                    userc.write(str(usid) + ',' + '0' + ',' + '0' + ',' + '10,' + '10,' + 'User,0,1000,0,0,0,0,0,1,10,' + name + '\n')
                    # dat['"'+str(id)+'"'] = {
                    #     "bis_lvl":"0",
                    #     "bis_type":"none"
                    # }
                    # bis.writelines(str(dat))
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'Аккаунт создан. Теперь я буду обращаться к вам, как ' + name + '\nНапишите "помощь" для списка команд'})
                else:
                    vk.method('messages.send', {'peer_id': id,
                                                'message': 'Необходимо завести аккаунт. Для этого напишите: "регистрация <Ваше имя>"'})

            elif str(usid) in ids:


                print(body + '\n' + 'by: ' + users[ids.index(str(usid))][-1])
                wh = True
                n = ids.index(str(usid))
                # if str(id) == '502004139' or str(id) == '155118230':
                #     users[ids.index('502004139')][5] = 'Admin'
                #     users[ids.index('155118230')][5] = 'Admin'
                #     replace_line('users.txt', n, ','.join(users[n]) + '\n')
                users[n][1] = str(round(float(users[n][1]), 2))
                users[n][8] = str(round(float(users[n][8]), 2))
                users[n][13] = str(round(float(users[n][13]),2))
                users[n][7] = str(round(float(users[n][7]),2))
                if float(users[n][1]) >= 99999999999999:
                    users[n][1] = '99999999999999'
                if float(users[n][8]) >= 99999999999999:
                    users[n][8] = '99999999999999'

                if 'все' in body.lower().split() and not 'снять' in body.lower().split():
                    print(body.lower())
                    body = body.lower().split()
                    body[body.index('все')] = str(int(float(users[n][1])))
                    body = ' '.join(body)
                    print(body,1)


                elif 'всё' in body.lower().split() and not 'снять' in body.lower().split():
                    print(body.lower())
                    body = body.lower().split()
                    body[body.index('всё')] = str(int(float(users[n][1])))
                    body = ' '.join(body)
                    print(body, 1)



                if body.lower() == 'hello':
                    vk.method('messages.send', {'peer_id': id, 'message': users[n][-1] + ',' + ' ''hi!'})
                    ans = True


                elif body.lower() == 'баланс':
                    vk.method('messages.send', {'peer_id': id, 'message': users[n][-1] + ', Ваш баланс: ' + commands.bt(
                        int(float(users[n][1]))) + '\nВ банке: ' + commands.bt(
                        int(float(users[n][8])))})

                    ans = True








                elif len(body.split()) > 1 and body.lower().split()[0] == 'казино':
                    ans = True
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
                                elif ch <= 35 and ch > 25:
                                    m = 0.75
                                    summ *= m
                                elif ch <= 45 and ch > 35:
                                    m = 2
                                    summ *= m
                                elif ch < 50 and ch > 45:
                                    m = 5
                                    summ *= m
                                elif ch == 50:
                                    if users[n][11] == '0':
                                        users[n][11] = '1'
                                        users[n][2] = str((int(float(users[n][2])) + 50))
                                        vk.method('messages.send', {'peer_id': id, 'message': 'Ура, вы первый раз выбили х50, награда 50 рейтинга!'})
                                    m = 50
                                    summ *= m
                                users[n][1] = str(float(users[n][1]) + summ)
                                vk.method('messages.send', {'peer_id': id, 'message': 'Вам попался (х' + str(m) + ')' + '\n' + 'Ваш баланс: ' + commands.bt(int(float(users[n][1])))})


                elif body.lower() == 'работать':
                    ans = True
                    if int(users[n][14]) <= 2:
                        vk.method('messages.send', {'peer_id': id,
                                                    'message': 'Вам нужно срочно поесть'})
                    else:
                        if int(users[n][4]) <= 0 and int(float(users[n][6])) == 10:
                            vk.method('messages.send', {'peer_id': id, 'message': 'Вы устроились на новую работу. Награда ' + str(float(users[n][13])*10) + ' рейтинга'})
                            users[n][2] = str(float(users[n][2]) + float(users[n][13])*10)
                            users[n][7] = str((int(float(users[n][7])) * 2.5))
                            if float(users[n][13]) < 50:
                                users[n][13] = str(float(users[n][13]) * 2.5)
                            users[n][6] = '0'
                        elif int(float(users[n][6])) != 10 and int(users[n][4]) <= 0:
                            users[n][6] = str((int(float(users[n][6])) + 1))
                            users[n][14] = str((int(float(users[n][14])) - 1))
                            users[n][1] = str(int(float(users[n][1])) + int(float(users[n][7])))
                            users[n][2] = str(float(users[n][2]) + float(users[n][13]))
                            vk.method('messages.send', {'peer_id': id, 'message': 'Вы заработали ' + users[n][7] + '$ ' + 'и ' + users[n][13] + ' рейтинга'})
                            users[n][4] = str(60)
                            if users[n][10] == '0':
                                users[n][10] = '1'
                                users[n][2] = str((int(float(users[n][2])) + 20))
                                vk.method('messages.send', {'peer_id': id, 'message': 'Ура, вы поработали 1-ый раз.\nНаграда 20 рейтинга'})
                        elif int(users[n][4]) > 0:
                            vk.method('messages.send',
                                      {'peer_id': id, 'message': 'Выходные кончатся через ' + str(int(users[n][4]))})
                elif body.lower() == 'бонус':
                    ans = True
                    if int(users[n][3]) <= 0:
                        if random.choice('mmmr') == 'm':
                            p = random.choice([100,100000,100000,500000000,500000000,500000000,25000000000])
                            users[n][1] = str(float(users[n][1]) + p)
                            vk.method('messages.send',
                                  {'peer_id': id, 'message': 'Вы получили '+commands.bt(p) + " $" + '\n' + 'Ваш баланс: ' + commands.bt(
                                      int(float(users[n][1])))})


                        else:
                            p = random.choice([2,2,10,10,10,50,50,100])
                            users[n][2] = str(float(users[n][2]) + p)
                            vk.method('messages.send',
                                  {'peer_id': id, 'message': 'Вы получили '+commands.bt(p) + " рейтинга" + '\n' + 'Ваш рейтинг ' + commands.bt(
                                      int(float(users[n][2])))})
                        users[n][3] = str(60)
                    else:
                        vk.method('messages.send',{'peer_id': id, 'message': 'До бонуса осталось:' + str(int(users[n][3]))})

                elif body.lower() == 'помощь':
                    ans = True
                    vk.method('messages.send', {'peer_id': id,
                                                'message': 'Вот что я могу: \nКлава (клавиатура с некоторыми командами)\nПередать <id> <сумма>\n' + 'Казино <сумма>\n' + 'Баланс \nБанк\nБанк положить\n Банк снять\nперевести <from> <to> <text>\nязыки(список языков для переводчика)' + '\nРаботать \n' + 'Бонус \n' + 'имя <имя>\nскажи <слова(<=500)>(будет отправлена ссылка на документ)\n' + 'топ (топ игроков)\nнаписать админу <сообщение>\nГраф <массив> (Пример: [[1,4],[0,3],[4],[1],[0,2]])' + '\nсс(по-русски) <число> <системы счисления из которой нужно перевести> <в которую>\n\n(Version: 0.2)'})
                    if users[n][5] == 'Admin':
                        vk.method('messages.send', {'peer_id': id,
                                                    'message': 'Доп команды для админов:\nПолучить <сумма>\nСоздать команду\nпомощь создать\nget_all_ids\nget_all_users\nюзеры(как get_all_users, красивее и проще)\nget_me (инфо о тебе)'})
                    if users[n][0] == '502004139' or users[n][0] == '155118230':
                        vk.method('messages.send', {'peer_id': id,
                                                    'message': 'Доп команды для меня: \nprefix\nedit_profile <id> <prefix> <значение>'})

                elif len(body.split()) > 1 and body.split()[0].lower() == 'имя':
                    ans = True
                    users[n][-1] = str(' '.join(body.split()[1:]))
                    vk.method('messages.send',{'peer_id': id, 'message': 'Имя изменено. Теперь я буду обращаться к вам, как ' + ' '.join(body.split()[1:])})


                elif body.lower() == 'топ':
                    ans = True
                    new_per = users[:]
                    new_per = [i[:] for i in new_per[:]]

                    for i in range(len(new_per)):
                        for j in range(len(new_per) - 1, i, -1):
                            if len(new_per[j]) > 1:
                                if int(float(new_per[j][2])) > int(float(new_per[j - 1][2])):
                                    new_per[j], new_per[j - 1] = new_per[j - 1], new_per[j]

                    new_per = [i for i in new_per if i[0] != '155118230' and str(i[0]) != '502004139']
                    new_per = new_per[:-1]
                    if len(new_per) > 5:
                        new_per = new_per[:5]
                    if users[n][5] == 'Admin':
                        top = [str(new_per.index(i) + 1) + ". " + "[id" + i[0] + "|" + i[-1] + "]" + ", money " + i[1]+", rating "+i[2] + ", id " + i[0] for i in new_per]
                        top = [i + '\n' for i in top]
                        top = ''.join(top)
                    else:
                        top = [str(new_per.index(i) + 1) + ". " + "[id"+i[0]+"|"+i[-1]+"]"+ ", money " + i[1] + ", rating " + i[2] for i in new_per]
                        top = [i + '\n' for i in top]
                        top = ''.join(top)
                    vk.method('messages.send', {'peer_id': id,'message': '0. [id155118230|Admin], money ∞, rating ∞\n'+top})

                elif body.lower() == 'помощь создать':
                    ans = True
                    if users[n][5] == 'Admin':
                        vk.method('messages.send',
                                  {'peer_id': id, 'message': 'Нужно написать: создать команду <parameters>\n\n'
                                                             'Параметры:\n'
                                                             '1. рандом <name> <первый рандомный элемент, ... , n-ый рандомный элемент>\n'
                                                             '2. 50%50 <name> <1st, 2nd> (Типа трейда вверх/вниз)'})

                elif body.lower() == 'профиль':
                    ans = True
                    vk.method('messages.send', {'peer_id': id,'message': 'Ваш профиль, '+users[n][-1]+':\n1. Ваш id: '+users[n][0] +'\n2. Баланс:' + commands.bt(str(int(float(users[n][1])))) + '\n3. В банке '+commands.bt(str(int(float(users[n][8]))))+'\n4. Рейтинг: ' + users[n][2] + '\n5. Привилегия: '+users[n][5] + '\n6. Голод: '+users[n][14]})






                elif body.lower().split()[:2] == ['создать', 'команду']:
                    ans = True
                    vk.method('messages.send', {'peer_id': id, 'message': 'Данная функция находится в активной разработке'})
                    # if users[n][5] == 'Admin':
                    #     all = body.lower().split()
                    #     if all[2] == 'рандом':
                    #         cg.random(all[3], all[4])
                    #         vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
                    #     elif all[2] == '50%50':
                    #         cg.halfchance(all[3], all[4])
                    #         vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})


                elif len(body.split()) > 1 and body.lower().split()[0] == 'получить':
                    ans = True
                    if users[n][5] == 'Admin' and body.lower().split()[1].isdigit():
                        users[n][1] = str(float(users[n][1]) + int(body.lower().split()[1].strip(
                            'asdfghjklqwertyuiopzxcvbnmфывапролдйцукенгшщзхъячсмитьбю?"}][;.>:{/!@#$%^&*()_+-=~`')))
                        vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})


                elif len(body.split()) > 1 and  body.lower().split()[0] == 'передать':
                    ans = True
                    g = body.lower().split()
                    if len(g) == 3 and g[2].isdigit() and int(float(users[n][1])) >= int(g[2]) and g[1] in ids and int(g[2]) > 0:
                        users[n][1] = str(int(float(users[n][1])) - int(g[2]))
                        users[ids.index(g[1])][1] = str(int(float(users[ids.index(g[1])][1]))+int(g[2]))
                        replace_line('users.txt', ids.index(str(g[1])), ','.join(users[ids.index(g[1])]) + '\n')
                        vk.method('messages.send',
                                  {'peer_id': id, 'message': 'Вы передали игроку ' + users[ids.index(g[1])][-1] + ' ' + g[2] + ' $'})
                        vk.method('messages.send',{'peer_id': g[1], 'message': 'Вам передал ' + users[n][-1] + ' ' + g[2] + ' $'})
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
                    ans = True
                    vk.method('messages.send',
                              {'peer_id': id, 'message': 'В банке ' + commands.bt(str(int(float(users[n][8]))))})

                elif body.lower().split()[:2] == ['банк','положить'] and len(body.lower().split()) >= 3 and body.lower().split()[2].isdigit():
                    ans = True

                    if int(float(users[n][1])) >= int(float(body.lower().split()[2])):
                        users[n][8] = str(int(float(users[n][8])) + int(float(body.lower().split()[2])))
                        users[n][1] = str(int(float(users[n][1])) - int(float(body.lower().split()[2])))
                        vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
                    else:
                        vk.method('messages.send', {'peer_id': id, 'message': 'Недостаточно денег'})


                elif body.lower().split()[:2] == ['банк', 'снять'] and len(body.lower().split()) >= 3:
                    ans = True
                    summ = body.split()[2]
                    # print(summ)
                    if (str(summ) != 'все' and str(summ) != 'всё') and not str(summ).isdigit():
                        vk.method('messages.send', {'peer_id': id, 'message': 'Так нельзя'})
                    else:
                        if not str(summ).isdigit():
                            summ = float(users[n][8])
                        summ = int(summ)
                        print(summ)
                        if summ <= int(float(users[n][8])):
                            users[n][8] = str(int(float(users[n][8])) - int(summ))
                            users[n][1] = str(int(float(users[n][1])) + int(summ))
                            vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
                        else:
                            vk.method('messages.send', {'peer_id': id, 'message': 'Недостаточно денег в банке'})


                elif len(body.split()) > 1 and body.split()[0].lower() == 'edit_profile' and len(body.split()) == 4 and (users[n][0] == '502004139' or users[n][0] == '155118230'):
                    ans = True
                    args = body.split()[1:]

                    users[ids.index(args[0])][int(args[1])] = args[2]
                    vk.method('messages.send', {'peer_id': id,
                                                'message': '[id'+users[ids.index(args[0])][0]+'|'+users[ids.index(args[0])][-1]+']' + ' теперь имеет ' + args[
                                                    2] + ' ' + typer(args[1])})
                    replace_line('users.txt', ids.index(str(args[0])), ','.join(users[ids.index(args[0])]) + '\n')


                elif body.lower() == 'prefix' and (users[n][0]=='502004139' or users[n][0] == '155118230'):
                    ans = True
                    pref = [str(i) + ' - ' + typer(str(i)) for i in range(len(users[0]))]
                    vk.method('messages.send', {'peer_id': id, 'message': '\n'.join(pref)})

                elif body.lower() == 'get_all_ids' and users[n][5] == 'Admin':
                    ans = True
                    vk.method('messages.send', {'peer_id':id, 'message': ' '.join(ids)})
                elif body.lower() == 'get_all_users' and users[n][5] == 'Admin':
                    ans = True
                    uss = [','.join(i) for i in users]
                    uss = '\n'.join(uss)
                    vk.method('messages.send', {'peer_id': id, 'message': uss})

                elif body.lower() == 'юзеры' and users[n][5] == 'Admin':
                    ans = True
                    uss = ["[id"+i[0]+"|"+i[-1]+"] \n" + 'id: ' + i[0] + '\n' + 'привилегия: '+i[5]+'\nденьги,рейтинг:' + i[1] + ',\t' + i[2] + '\n\n' for i in users if len(i) > 1]
                    uss = '\n'.join(uss)
                    vk.method('messages.send', {'peer_id': id, 'message': uss})

                elif body.lower() == 'get_all_admins' and users[n][5] == 'Admin':
                    ans = True
                    adm = ["[id"+i[0]+"|"+i[-1]+"] " + i[0] for i in users if len(i) > 1 and i[5] == 'Admin']
                    adm = '\n'.join(adm)
                    vk.method('messages.send', {'peer_id': id, 'message': adm})

                elif body.lower() == 'yayangi':
                    ans = True
                    if users[n][12] == '0':
                        users[n][12] = '1'
                        users[n][2] = str(float(users[n][2]) + 50)
                        vk.method('messages.send', {'peer_id': id, 'message': 'Воу, вы нашли читкод, награда 50 рейтинга'})
                    else:
                        vk.method('messages.send', {'peer_id': id, 'message': 'Ты уже вводил этот читкод'})

                elif body.lower() == 'get_me' and users[n][5] == 'Admin':
                    ans = True
                    getting = [typer(str(i)) + ' ' + str(users[n][i]) + '\n' for i in range(len(users[n]))]
                    vk.method('messages.send', {'peer_id': id, 'message': ''.join(getting)})

                elif body.lower().split()[:2] == ['написать', 'админу']:
                    ans = True
                    message = body.split()[2:]
                    di = str(users[n][0])
                    di = "[id"+users[n][0]+"|"+users[n][-1]+" "+users[n][0]+"]"
                    # print(di)

                    vk.method('messages.send', {'peer_id': '155118230', 'message': ' '.join(message) + "\nby: "+di})
                    vk.method('messages.send', {'peer_id': id,'message': 'Готово'})



                elif body.lower().split()[:1] == ['перевести']:
                    ans = True
                    eng_text = body.split()[1:]
                    langs = [eng_text[0], eng_text[1]]
                    eng_text = body.split()[3:]

                    eng_text = ' '.join(eng_text)
                    # print(eng_text, langs)
                    if langs[0] in all_lang and langs[1] in all_lang:
                        url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
                        trans_option = {'key': token, 'lang': langs[0]+"-"+langs[1], 'text': eng_text}
                        # trans_option = {'key': token, 'lang': "en-ru", 'text': eng_text}
                        webRequest = requests.get(url_trans, params=trans_option)
                        rus_text = webRequest.text
                        srez = 32+len(langs[0])+len(langs[1])
                        rus_text = rus_text[srez:(len(rus_text) - 3)]

                        vk.method('messages.send', {'peer_id': id, 'message': rus_text+ '\n\nПереведено сервисом «Яндекс.Переводчик»\nhttp://translate.yandex.ru/'})
                elif body.lower() == 'языки':
                    ans = True
                    vk.method('messages.send', {'peer_id': id, 'message': 'азербайджанский	az	\nмалаялам	ml\n\
    албанский	sq	\nмальтийский	mt\n\
    амхарский	am	\nмакедонский	mk\n\
    английский	en	\nмаори	mi\n\
    арабский	ar	\nмаратхи	mr\n\
    армянский	hy	\nмарийский	mhr\n\
    африкаанс	af	\nмонгольский	mn\n\
    баскский	eu	\nнемецкий	de\n\
    башкирский	ba	\nнепальский	ne\n\
    белорусский	be	\nнорвежский	no\n\
    бенгальский	bn	\nпанджаби	pa\n\
    бирманский	my	\nпапьяменто	pap\n\
    болгарский	bg	\nперсидский	fa\n\
    боснийский	bs	\nпольский	pl\n\
    валлийский	cy	\nпортугальский	pt\n\
    венгерский	hu	\nрумынский	ro\n\
    вьетнамский	vi	\nрусский	ru\n\
    гаитянский (креольский)	ht	\nсебуанский	ceb\n\
    галисийский	gl	\nсербский	sr\n\
    голландский	nl	\nсингальский	si\n\
    горномарийский	\nmrj	словацкий	sk\n\
    греческий	el	\nсловенский	sl\n\
    грузинский	ka	\nсуахили	sw\n\
    гуджарати	gu	\nсунданский	su\n\
    датский	da	\nтаджикский	tg\n\
    иврит	he	\nтайский	th\n\
    идиш	yi	\nтагальский	tl\n\
    индонезийский	id	\nтамильский	ta\n\
    ирландский	ga	\nтатарский	tt\n\
    итальянский	it	\nтелугу	te\n\
    исландский	is	\nтурецкий	tr\n\
    испанский	es	\nудмуртский	udm\n\
    казахский	kk	\nузбекский	uz\n\
    каннада	kn	\nукраинский	uk\n\
    каталанский	ca	\nурду	ur\n\
    киргизский	ky	\nфинский	fi\n\
    китайский	zh	\nфранцузский	fr\n\
    корейский	ko	\nхинди	hi\n\
    коса	xh	\nхорватский	hr\n\
    кхмерский	km	\nчешский	cs\n\
    лаосский	lo	\nшведский	sv\n\
    латынь	la	\nшотландский	gd\n\
    латышский	lv	\nэстонский	et\n\
    литовский	lt	\nэсперанто	eo\n\
    люксембургский	lb	\nяванский	jv\n\
    малагасийский	mg	\nяпонский	ja\n\
    малайский	ms	'})


                elif len(body.split()) == 2 and body.lower().split()[0] == 'граф':
                    ans = True
                    print('graph')
                    if body.lower().split()[1] == 'рандом':
                        nums = random.choice(range(1,15))
                        # print(nums)
                        points = [i for i in range(nums)]
                        # print(points)
                        comps = random.choice(range(nums,nums+5))
                        # print(nums)
                        cord = [[random.choice(points) for i in range(random.choice(range(1,5)))] for i in range(nums)]
                        # print(''.join(str(cord).split()))

                        try:
                            # cord = json.loads(cord)
                            grouptest.graph(cord)
                            a = vk.method("photos.getMessagesUploadServer")
                            b = requests.post(a['upload_url'], files={'photo': open('test.png', 'rb')}).json()
                            c = vk.method('photos.saveMessagesPhoto',
                                          {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                            d = "photo{}_{}".format(c["owner_id"], c["id"])
                            vk.method('messages.send', {'peer_id': id, "attachment": d, "message": 'Вот граф ' + ''.join(str(cord).split())})
                        except:
                            vk.method('messages.send', {'peer_id': id, "message": 'Ошибка'})
                    elif body.lower().split()[1] != 'рандом':
                        ans = True
                        print(123)
                        try:
                            cord = body.split()[1:]
                            cord = ''.join(cord)

                            cord = json.loads(cord)
                            grouptest.graph(cord)
                            a = vk.method("photos.getMessagesUploadServer")
                            b = requests.post(a['upload_url'], files={'photo': open('test.png', 'rb')}).json()
                            c = vk.method('photos.saveMessagesPhoto',
                                          {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                            d = "photo{}_{}".format(c["owner_id"], c["id"])
                            vk.method('messages.send', {'peer_id': id, "attachment": d, "message": 'Вот граф'})
                        except:
                            vk.method('messages.send', {'peer_id': id, "message": 'Неверный формат'})

                elif body.lower().split()[0] == 'f(x)':
                    ans = True
                    pass

                elif body.lower() == 'клава':
                    ans = True
                    vk.method("messages.send", {"peer_id": id, "message": "Клавиатура выведена", "keyboard": keyboard})

                elif body.lower() == 'есть':
                    ans = True
                    if float(users[n][1]) < 500:
                        vk.method("messages.send", {"peer_id": id, "message": ":( недостаточно денег, вы можете начать игру сначала, написав заново <ваш id>"})
                    else:
                        users[n][1] = str(float(users[n][1]) - 500)
                        users[n][14] = str(10)
                        vk.method("messages.send", {"peer_id": id, "message": "Вы поели на 500$"})

                elif body.lower() == 'заново '+users[n][0]:
                    ans = True
                    print(users[n][5])

                    users[n][1],users[n][2],users[n][3],users[n][4],users[n][6],users[n][7],users[n][8] = '0', '0', '10', '10', '0', '1000', '0'
                    users[n][9], users[n][10],users[n][11], users[n][12], users[n][13], users[n][14] = '0','0', '0', '0', '1','10'
                    vk.method("messages.send", {"peer_id": id, "message": "Ваш аккаунт сброшен. Сохранено: привилегия, имя"})



                elif body.split()[0].lower() == 'скажи' or body.split()[0].lower() == 'tts' or body.split()[0].lower() == 'ттс':
                    ans = True
                    words = ' '.join(body.split()[1:])

                    hr = speech.speech(words,id,'ru')


                    vk.method('messages.send', {'peer_id': id, 'message': 'https://vk.com/'+hr})  # отправляю сообщение


                elif len(body.lower().split()) == 1:
                    ans = True
                    # print(body.lower().split('e'))
                    if len(''.join(body.lower().split('е'))) == 0:
                        vk.method('messages.send', {'peer_id': id, 'message': 'Б'+'О'*len(body)+'Й'})

                    elif len(''.join(body.lower().split('e'))) == 0:
                        vk.method('messages.send', {'peer_id': id, 'message': 'B'+'O'*len(body)+'Y'})


                elif len(body.lower().split()) == 4 and body.lower().split()[0] == 'сс':
                    ans = True
                    body = body.lower().split()
                    print(body)
                    try:
                        vk.method('messages.send', {'peer_id': id, 'message': str(convert_base(str(body[1]), int(body[2]), int(body[3])))})

                    except:
                        vk.method('messages.send', {'peer_id': id, 'message': 'Error!\n\n Возможно указано неверное значение системы из который нужно переводить.\nИли в числе используются не англ символы.\nЕсли все условия соблюдены - повторите попытку.'})

                    # vk.method('messages.send', {'peer_id': id, 'message': '123'})
                    # Обработка команд
                def textMessage(update):
                    request = apiai.ApiAI('6a64d8a88c164253990049e41c5c4f06').text_request() # Токен API к Dialogflow
                    request.lang = 'ru' # На каком языке будет послан запрос
                    request.session_id = 'BatlabAIBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
                    request.query = update # Посылаем запрос к ИИ с сообщением от юзера
                    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
                    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
                    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
                    if response:
                        vk.method('messages.send', {'peer_id': id, 'message': response})
                    else:
                        vk.method('messages.send', {'peer_id': id, 'message': 'Не понял вас'})
                print(123456789)
                textMessage(body)
                replace_line('users.txt', ids.index(str(usid)), ','.join(users[n]) + '\n')






        # print(cc)
        if cc % 3600 == 0:
            cc = 0
            for i in range(len(users)):
                if len(users[i]) > 1:
                    users[i][8] = str(float(users[i][8])*1.1)
                    replace_line('users.txt', i, ','.join(users[i]) + '\n')


        time.sleep(1)
    except:
        time.sleep(2)