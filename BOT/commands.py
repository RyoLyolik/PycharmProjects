import random

# import draw
import requests
# import speech
import json
# import vk_api

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


token = 'trnsl.1.1.20180822T035034Z.c4e6b0734a1501db.3c10535039452db4d70963681df09234674e4b33'
all_lang = ['az', 'sq', 'am', 'en', 'ar', 'hy', 'af', 'eu', 'ba', 'be', 'bn', 'my',
            'bg', 'bs', 'cy', 'hu', 'vi', 'ht', 'gl', 'nl', 'mrj', 'el', 'ka', 'gu',
            'da', 'he', 'yi', 'id', 'ga', 'it', 'is', 'es', 'kk', 'kn', 'ca', 'ky',
            'zh', 'ko', 'xh', 'km', 'lo', 'la', 'lv', 'lt', 'lb', 'mg', 'ms', 'ml',
            'mt', 'mk', 'mi', 'mr', 'mhr', 'mn', 'de', 'ne', 'no', 'pa', 'pap', 'fa',
            'pl', 'pt', 'ro', 'ru', 'ceb', 'sr', 'si', 'sk', 'sl', 'sw', 'su', 'tg',
            'th', 'tl', 'ta', 'tt', 'te', 'tr', 'udm', 'uz', 'uk', 'ur', 'fi', 'fr',
            'hi', 'hr', 'cs', 'sv', 'gd', 'et', 'eo', 'jv', 'ja']

def reformat(num):
    end = ''
    num = int(num)
    num = str(num)
    num = [i for i in num]
    num = reversed(num)
    num = ''.join(num)

    cnt = 0
    for i in range(0, len(num)):

        if cnt == 3:
            end += ' '
            end += num[i]
            cnt = 0
        else:
            end += num[i]
        cnt += 1
    end = [i for i in end]
    end = reversed(end)
    end = ''.join(end)
    return end


def check_message(command, users, ids, n):
    if '|_|_|' in command or '|_|' in command:
        return 'недопустимы формат сообщения'
    else:
        return command_detect(command, users, ids, n)


def convert_base(num, from_base=10, to_base=10):
    # first convert to decimal number
    n = int(str(num), int(from_base))

    # convert decimal to base
    alphabet = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]

    else:
        return convert_base(n // to_base, 10, to_base) + alphabet[n % to_base]


def typer(arg):
    if arg == '0':
        return '0.id'
    elif arg == '1':
        return '1.money'
    elif arg == '2':
        return '2.рейтинг'
    elif arg == '3':
        return '3.время до бонуса'
    elif arg == '4':
        return '4.время до окончания выходных'
    elif arg == '5':
        return '5.привилегия'
    elif arg == '6':
        return '6.Как скоро повышение(1 - нескоро, 10 - прямо сейчас)'
    elif arg == '7':
        return '7.зарплата'
    elif arg == '8':
        return '8.деньги в банке'
    elif arg == '9':
        return '9.работал ли игрок вообще'

    elif arg == '10':
        return '10.выпадало ли игроку х50'
    elif arg == '11':
        return '11.вводил ли игрок хоть один читкод'
    elif arg == '12':
        return '12.рейтинг множитель'

    elif arg == '13':
        return '13.голод'
    elif arg == '14':
        return '14.имя'

def command_detect(body, users, ids, n):
    if 'все' in body.lower().split() and not 'снять' in body.lower().split():
        body = body.lower().split()
        body[body.index('все')] = str(int(float(users[n][1])))
        body = ' '.join(body)


    elif 'всё' in body.lower().split() and not 'снять' in body.lower().split():
        body = body.lower().split()
        body[body.index('всё')] = str(int(float(users[n][1])))
        body = ' '.join(body)

    if body.lower() == 'hello':
        return 'hi'



    elif body.lower() == 'баланс':
        return users[n][-1] + ', Ваш баланс: ' + reformat(
            int(float(users[n][1]))) + '\nВ банке: ' + reformat(
            int(float(users[n][8])))


    elif len(body.split()) > 1 and body.lower().split()[0] == 'казино':

        summ = body.split()[1]
        if (str(summ) != 'все' and str(summ) != 'всё') and not str(summ).isdigit():
            return 'Так нельзя'
        else:
            summ = float(summ)
            if not str(summ).isdigit():
                summ = float(users[n][1])

            if summ > float(users[n][1]):
                return 'Недостаточно денег'
            else:
                if summ > 0:
                    users[n][1] = int(float(users[n][1])) - int((float(summ)))
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
                            return 'Ура, вы первый раз выбили х50, награда 50 рейтинга!' + 'Ваш баланс: ' + reformat(
                                int(float(users[n][1])))
                        m = 50
                        summ *= m
                    users[n][1] = str(float(users[n][1]) + summ)
                    return 'Вам попался (х' + str(m) + ')' + '\n' + 'Ваш баланс: ' + reformat(
                        int(float(users[n][1])))


    elif body.lower() == 'работать':

        if int(users[n][13]) <= 2:
            return 'Вам нужно срочно поесть'
        else:
            if int(users[n][4]) <= 0 and int(float(users[n][6])) == 10:
                users[n][2] = str(int(users[n][2]) + int(users[n][13]) * 10)
                users[n][7] = str((int(float(users[n][7])) * 2.5))
                if float(users[n][13]) < 50:
                    users[n][12] = str(float(users[n][12]) * 2.5)
                users[n][6] = '0'
                return 'Вы устроились на новую работу. Награда ' + str(float(users[n][12]) / 2.5 * 10) + ' рейтинга'
            elif int(float(users[n][6])) != 10 and int(users[n][4]) <= 0:
                users[n][6] = str((int(float(users[n][6])) + 1))
                users[n][13] = str((int(float(users[n][13])) - 1))
                users[n][1] = str(int(float(users[n][1])) + int(float(users[n][7])))
                print(users[n])
                users[n][2] = str(int(float(users[n][2])) + int(float(users[n][12])))
                users[n][4] = str(60)
                if users[n][9] == '0':
                    users[n][9] = '1'
                    users[n][2] = str((int(float(users[n][2])) + 20))
                    return 'Ура, вы поработали 1-ый раз.\nНаграда 20 рейтинга'
                return 'Вы заработали ' + str(users[n][7]) + '$ ' + 'и ' + str(int(float(users[n][12]))) + ' рейтинга'
            elif int(users[n][4]) > 0:
                return 'Выходные кончатся через ' + str(int(users[n][4]))
    elif body.lower() == 'бонус':

        if int(users[n][3]) <= 0:
            if random.choice('mmr') == 'm':
                p = random.choice([100, 100000, 100000, 500000000, 500000000, 500000000, 25000000000])
                users[n][1] = str(float(users[n][1]) + p)
                users[n][3] = str(60)
                return 'Вы получили ' + reformat(
                    p) + " $" + '\n' + 'Ваш баланс: ' + reformat(
                    int(float(users[n][1])))


            else:
                p = random.choice([2, 2, 10, 10, 10, 50, 50, 100])
                users[n][2] = str(float(users[n][2]) + p)
                users[n][3] = str(60)
                return 'Вы получили ' + reformat(
                    p) + " рейтинга" + '\n' + 'Ваш рейтинг ' + reformat(
                    int(float(users[n][2])))

        else:
            return 'До бонуса осталось:' + str(int(users[n][3]))

    elif body.lower() == 'помощь':
        answer = 'Вот что я могу: \nКлава (клавиатура с некоторыми командами)\nПередать <id> <сумма>\n' + 'Казино <сумма>\n' + 'Баланс \nБанк\nБанк положить\n Банк снять\nперевести <from> <to> <text>\nязыки(список языков для переводчика)' + '\nРаботать \n' + 'Бонус \n' + 'имя <имя>\nскажи <слова(<=500)>(будет отправлена ссылка на документ)\n' + 'топ (топ игроков)\nнаписать админу <сообщение>\nГраф <массив> (Пример: [[1,4],[0,3],[4],[1],[0,2]])' + '\nсс(по-русски) <число> <системы счисления из которой нужно перевести> <в которую>\n\n(Version: 0.2)'

        if users[n][5] == 'Admin':
            answer += '\n\nДоп команды для админов:\nПолучить <сумма>\nСоздать команду\nпомощь создать\nget_all_ids\nget_all_users\nюзеры(как get_all_users, красивее и проще)\nget_me (инфо о тебе)'
        if users[n][0] == '454666989' or users[n][0] == '155118230':
            answer += '\n\nДоп команды для меня: \nprefix\nedit_profile <id> <prefix> <значение>'
        return answer

    elif len(body.split()) > 1 and body.split()[0].lower() == 'имя':

        users[n][-1] = str(' '.join(body.split()[1:]))
        return 'Имя изменено. Теперь я буду обращаться к вам, как ' + ' '.join(
            body.split()[1:])


    elif body.lower() == 'топ':
        new_per = users[:]
        new_per = [i[:] for i in new_per[:]]

        for i in range(len(new_per)):
            for j in range(len(new_per) - 1, i, -1):
                if len(new_per[j]) > 1:
                    if int(float(new_per[j][2])) > int(float(new_per[j - 1][2])):
                        new_per[j], new_per[j - 1] = new_per[j - 1], new_per[j]

        new_per = [i for i in new_per if i[0] != '155118230' and str(i[0]) != '454666989']
        new_per = new_per[:-1]
        if len(new_per) > 5:
            new_per = new_per[:5]
        if users[n][5] == 'Admin':
            top = [str(new_per.index(i) + 1) + ". " + "[id" + i[0] + "|" + i[-1] + "]" + ", money " + i[
                1] + ", rating " + i[2] + ", id " + i[0] for i in new_per]
            top = [i + '\n' for i in top]
            top = ''.join(top)
        else:
            top = [str(new_per.index(i) + 1) + ". " + "[id" + i[0] + "|" + i[-1] + "]" + ", money " + i[
                1] + ", rating " + i[2] for i in new_per]
            top = [i + '\n' for i in top]
            top = ''.join(top)
        return '0. [id155118230|Admin], money ∞, rating ∞\n' + top

    elif body.lower() == 'помощь создать':

        if users[n][5] == 'Admin':  # TODO
            return 'Данная функция находится в активной разработке'

    elif body.lower() == 'профиль':
        return 'Ваш профиль, ' + users[n][-1] + ':\n1. Ваш id: ' + str(users[n][
                                                                           0]) + '\n2. Баланс: ' + reformat(
            str(int(float(users[n][1])))) + '\n3. В банке ' + reformat(
            str(int(float(users[n][8])))) + '\n4. Рейтинг: ' + str(users[n][
                   2]) + '\n5. Привилегия: ' + str(users[n][5]) + '\n6. Голод: ' + str(users[n][13])

    elif body.lower().split()[:2] == ['создать', 'команду']:
        return 'Данная функция находится в активной разработке'  # TODO

    elif len(body.split()) > 1 and body.lower().split()[0] == 'получить':

        if users[n][5] == 'Admin' and body.lower().split()[1].isdigit():
            users[n][1] = str(float(users[n][1]) + int(body.lower().split()[1].strip(
                'asdfghjklqwertyuiopzxcvbnmфывапролдйцукенгшщзхъячсмитьбю?"}][;.>:{/!@#$%^&*()_+-=~`')))
            return 'Готово!'


    elif len(body.split()) > 1 and body.lower().split()[0] == 'передать':

        g = body.lower().split()
        if len(g) == 3 and g[2].isdigit() and int(float(users[n][1])) >= int(g[2]) and g[1] in ids and int(
                g[2]) > 0:
            users[n][1] = str(int(float(users[n][1])) - int(g[2]))
            users[ids.index(g[1])][1] = str(int(float(users[ids.index(g[1])][1])) + int(g[2]))
            replace_line('users.txt', ids.index(str(g[1])), ','.join(users[ids.index(g[1])]) + '\n')
            return 'Вы передали игроку ' + users[ids.index(g[1])][-1] + ' ' + g[
                2] + ' $' + '|_|_|' + 'Вам передал ' + users[n][-1] + ' ' + g[2] + ' $'  # TODO
        elif g[2].isdigit() and int(float(users[n][1])) < int(g[2]):
            return 'Недостаточно денег'
        elif not g[1] in ids:
            return 'ID не существует'
        else:
            return 'В боте это не предусмотренно'


    elif body.lower() == 'банк':
        return 'В банке ' + reformat(str(int(float(users[n][8]))))

    elif body.lower().split()[:2] == ['банк', 'положить'] and len(body.lower().split()) >= 3 and \
            body.lower().split()[2].isdigit():

        if int(float(users[n][1])) >= int(float(body.lower().split()[2])):
            users[n][8] = str(int(float(users[n][8])) + int(float(body.lower().split()[2])))
            users[n][1] = str(int(float(users[n][1])) - int(float(body.lower().split()[2])))
            return 'Готово'
        else:
            return 'Готово'


    elif body.lower().split()[:2] == ['банк', 'снять'] and len(body.lower().split()) >= 3:

        summ = body.split()[2]
        if (str(summ) != 'все' and str(summ) != 'всё') and not str(summ).isdigit():
            return 'Так нельзя'
        else:
            if not str(summ).isdigit():
                summ = float(users[n][8])
            summ = int(summ)
            if summ <= int(float(users[n][8])):
                users[n][8] = str(int(float(users[n][8])) - int(summ))
                users[n][1] = str(int(float(users[n][1])) + int(summ))
                return 'Готово'
            else:
                return 'Недостаточно денег в банке'


    elif len(body.split()) > 1 and body.split()[0].lower() == 'edit_profile' and len(body.split()) == 4 and (
            users[n][0] == '454666989' or users[n][0] == '155118230'):

        args = body.split()[1:]
        users[ids.index(str(args[0]))][int(args[1])] = args[2]

        return '[id' + str(users[ids.index(str(args[0]))][0]) + '|' + str(
            users[ids.index(str(args[0]))][-1]) + ']' + ' теперь имеет ' + \
               args[
                   2] + ' ' + typer(args[1])


    elif body.lower() == 'prefix' and (users[n][0] == '155118230' or users[n][0] == '454666989'):
        pref = [str(i) + ' - ' + typer(str(i)) for i in range(len(users[0]))]
        return '\n'.join(pref)

    elif body.lower() == 'get_all_ids' and users[n][5] == 'Admin':
        return ' '.join(ids)
    elif body.lower() == 'get_all_users' and users[n][5] == 'Admin':

        uss = [','.join(i) for i in users]
        uss = '\n'.join(uss)
        return uss

    elif body.lower() == 'юзеры' and users[n][5] == 'Admin':

        uss = ["[id" + i[0] + "|" + i[-1] + "] \n" + 'id: ' + i[0] + '\n' + 'привилегия: ' + i[
            5] + '\nденьги,рейтинг:' + i[1] + ',\t' + i[2] + '\n\n' for i in users if len(i) > 1]
        uss = '\n'.join(uss)
        return uss

    elif body.lower() == 'get_all_admins' and users[n][5] == 'Admin':

        adm = ["[id" + i[0] + "|" + i[-1] + "] " + i[0] for i in users if len(i) > 1 and i[5] == 'Admin']
        adm = '\n'.join(adm)
        return adm

    elif body.lower() == 'yayangi':

        if users[n][11] == '0':
            users[n][11] = '1'
            users[n][2] = str(float(users[n][2]) + 50)
            return 'Воу, вы нашли читкод, награда 50 рейтинга'
        else:
            return 'Ты уже вводил этот читкод'

    elif body.lower() == 'get_me' and users[n][5] == 'Admin':

        getting = [typer(str(i)) + ' ' + str(users[n][i]) + '\n' for i in range(len(users[n]))]
        return ''.join(getting)

    elif body.lower().split()[:2] == ['написать', 'админу']:

        message = body.split()[2:]
        di = str(users[n][0])
        di = "[id" + str(users[n][0]) + "|" + str(users[n][-1]) + " " + str(users[n][0]) + "]"
        return 'Готово' + '|_|_|' + ' '.join(message) + "\nby: " + di



    elif body.lower().split()[:1] == ['перевести']:

        eng_text = body.split()[1:]
        langs = [eng_text[0], eng_text[1]]
        eng_text = body.split()[3:]

        eng_text = ' '.join(eng_text)
        if langs[0] in all_lang and langs[1] in all_lang:
            url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
            trans_option = {'key': token, 'lang': langs[0] + "-" + langs[1], 'text': eng_text}
            # trans_option = {'key': token, 'lang': "en-ru", 'text': eng_text}
            webRequest = requests.get(url_trans, params=trans_option)
            rus_text = webRequest.text
            srez = 32 + len(langs[0]) + len(langs[1])
            rus_text = rus_text[srez:(len(rus_text) - 3)]

            return rus_text + '\n\nПереведено сервисом «Яндекс.Переводчик»\nhttp://translate.yandex.ru/'
    elif body.lower() == 'языки':
        return '''азербайджанский	az	\nмалаялам	ml\n\
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
    малайский	ms'''


    elif len(body.split()) == 2 and body.lower().split()[0] == 'граф':
        if body.lower().split()[1] == 'рандом':
            nums = random.choice(range(1, 15))
            points = [i for i in range(nums)]
            comps = random.choice(range(nums, nums + 5))
            cord = [list(set([random.choice(points) for i in range(random.choice(range(1, 5)))])) for i in range(nums)]
            try:
                # cord = json.loads(cord)
                vk = vk_api.VkApi(
                    token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
                vk._auth_token()
                draw.graph(cord)
                a = vk.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('test.png', 'rb')}).json()
                c = vk.method('photos.saveMessagesPhoto',
                              {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                # vk.method('messages.send',
                #           {'peer_id': id, "attachment": d, "message": 'Вот граф ' + ''.join(str(cord).split())})
                return (d, 'Вот граф ' + ''.join(str(cord).split()))
            except:
                return 'Ошибка'
        elif body.lower().split()[1] != 'рандом':
            try:
                cord = body.split()[1:]
                cord = ''.join(cord)

                cord = draw.loads(cord)
                draw.graph(cord)
                a = vk.method("photos.getMessagesUploadServer")
                b = requests.post(a['upload_url'], files={'photo': open('test.png', 'rb')}).json()
                c = vk.method('photos.saveMessagesPhoto',
                              {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                d = "photo{}_{}".format(c["owner_id"], c["id"])
                vk.method('messages.send', {'peer_id': id, "attachment": d, "message": 'Вот граф'})
                return (d, 'Вот граф')
            except:
                return 'Неверный формат'

    elif body.lower().split()[0] == 'f(x)':  # TODO
        pass

    elif body.lower() == 'клава':

        # keyboard = {
        #     "one_time": False,
        #     "buttons": [
        #         [get_button(label="Помощь", color="primary")],
        #         [get_button(label="Казино всё", color="negative")],
        #         [get_button(label="Баланс", color="primary"), get_button(label="Профиль", color="default")],
        #         [get_button(label="Работать", color="positive"), get_button(label="Бонус", color="positive")],
        #         [get_button(label="Есть", color="default")]
        #
        #     ]
        # }
        # vk.method("messages.send", {"peer_id": id, "message": "Клавиатура выведена", "keyboard": keyboard})
        return 'Ошибка'

    elif body.lower() == 'есть':

        if float(users[n][1]) < 500:
            return ":( недостаточно денег, вы можете начать игру сначала, написав заново <ваш id> или подождать до бонуса"
        else:
            users[n][1] = str(float(users[n][1]) - 500)
            users[n][13] = str(10)
            return "Вы поели на 500$"

    elif body.lower() == 'заново ' + str(users[n][0]):
        users[n][1], users[n][2], users[n][3], users[n][4], users[n][6], users[n][7], users[n][
            8] = '0', '0', '10', '10', '0', '1000', '0'
        users[n][9], users[n][10], users[n][11], users[n][12], users[n][13], users[n][
            14] = '0', '0', '0', '0', '10', users[n][14]
        return "Ваш аккаунт сброшен. Сохранено: привилегия, имя"



    elif body.split()[0].lower() == 'скажи' or body.split()[0].lower() == 'tts' or body.split()[
        0].lower() == 'ттс':  # ToDo
        pass
    #
    #     words = ' '.join(body.split()[1:])

    #     hr = speech.speech(words, id, 'ru')
    #     return hr

    elif len(body.lower().split()) == 1 and (
            len(body.lower().split('e')) == 1 or len(body.lower().split('е')) == 1):
        if len(''.join(body.lower().split('е'))) == 0:
            return 'Б' + 'О' * len(body) + 'Й'

        elif len(''.join(body.lower().split('e'))) == 0:
            return 'B' + 'O' * len(body) + 'Y'


    elif len(body.lower().split()) == 4 and body.lower().split()[0] == 'сс':

        body = body.lower().split()
        try:
            return str(convert_base(str(body[1]), int(body[2]), int(body[3])))

        except:
            vk.method('messages.send', {'peer_id': id,
                                        'message': 'Error!\n\n Возможно указано неверное значение системы из который нужно переводить.\nИли в числе используются не англ символы.\nЕсли все условия соблюдены - повторите попытку.'})
            return 'Error!\n\n Возможно указано неверное значение системы из который нужно переводить.\nИли в числе используются не латинские символы.\nЕсли все условия соблюдены - повторите попытку.'