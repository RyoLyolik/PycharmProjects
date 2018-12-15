import random

import requests


# import speech

class Commands:
    def __init__(self, command, users, ids, n):
        self.command_detect(command, users, ids, n)

    def beauty(self, num):
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

    def command_detect(self, body, users, ids, n):
        if 'все' in body.lower().split() and not 'снять' in body.lower().split():
            print(body.lower())
            body = body.lower().split()
            body[body.index('все')] = str(int(float(users[n][1])))
            body = ' '.join(body)
            print(body, 1)


        elif 'всё' in body.lower().split() and not 'снять' in body.lower().split():
            print(body.lower())
            body = body.lower().split()
            body[body.index('всё')] = str(int(float(users[n][1])))
            body = ' '.join(body)
            print(body, 1)

        if body.lower() == 'hello':
            return 'hi'



        elif body.lower() == 'баланс':
            return users[n][-1] + ', Ваш баланс: ' + self.beauty(
                int(float(users[n][1]))) + '\nВ банке: ' + self.beauty(
                int(float(users[n][8])))


        elif len(body.split()) > 1 and body.lower().split()[0] == 'казино':

            summ = body.split()[1]
            if (str(summ) != 'все' and str(summ) != 'всё') and not str(summ).isdigit():
                return 'Так нельзя'
            else:
                if not str(summ).isdigit():
                    summ = float(users[n][1])

                summ = float(summ)
                if summ > float(users[n][1]):
                    return 'Недостаточно денег'
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
                                return 'Ура, вы первый раз выбили х50, награда 50 рейтинга!' + 'Ваш баланс: ' + self.beauty(
                                    int(float(users[n][1])))
                            m = 50
                            summ *= m
                        users[n][1] = str(float(users[n][1]) + summ)
                        return 'Вам попался (х' + str(m) + ')' + '\n' + 'Ваш баланс: ' + self.beauty(int(float(users[n][1])))


        elif body.lower() == 'работать':

            if int(users[n][14]) <= 2:
                return 'Вам нужно срочно поесть'
            else:
                if int(users[n][4]) <= 0 and int(float(users[n][6])) == 10:
                    users[n][2] = str(float(users[n][2]) + float(users[n][13]) * 10)
                    users[n][7] = str((int(float(users[n][7])) * 2.5))
                    if float(users[n][13]) < 50:
                        users[n][13] = str(float(users[n][13]) * 2.5)
                    users[n][6] = '0'
                    return 'Вы устроились на новую работу. Награда ' + str(float(users[n][13]) / 2.5 * 10) + ' рейтинга'
                elif int(float(users[n][6])) != 10 and int(users[n][4]) <= 0:
                    users[n][6] = str((int(float(users[n][6])) + 1))
                    users[n][14] = str((int(float(users[n][14])) - 1))
                    users[n][1] = str(int(float(users[n][1])) + int(float(users[n][7])))
                    users[n][2] = str(float(users[n][2]) + float(users[n][13]))
                    users[n][4] = str(60)

                    if users[n][10] == '0':
                        users[n][10] = '1'
                        users[n][2] = str((int(float(users[n][2])) + 20))
                        return 'Ура, вы поработали 1-ый раз.\nНаграда 20 рейтинга'
                    return 'Вы заработали ' + users[n][7] + '$ ' + 'и ' + users[n][13] + ' рейтинга'
                elif int(users[n][4]) > 0:
                    return 'Выходные кончатся через ' + str(int(users[n][4]))
        elif body.lower() == 'бонус':

            if int(users[n][3]) <= 0:
                if random.choice('mmr') == 'm':
                    p = random.choice([100, 100000, 100000, 500000000, 500000000, 500000000, 25000000000])
                    users[n][1] = str(float(users[n][1]) + p)
                    users[n][3] = str(60)
                    return 'Вы получили ' + self.beauty(
                                  p) + " $" + '\n' + 'Ваш баланс: ' + self.beauty(
                                  int(float(users[n][1])))


                else:
                    p = random.choice([2, 2, 10, 10, 10, 50, 50, 100])
                    users[n][2] = str(float(users[n][2]) + p)
                    users[n][3] = str(60)
                    return  'Вы получили ' + self.beauty(
                                  p) + " рейтинга" + '\n' + 'Ваш рейтинг ' + self.beauty(
                                  int(float(users[n][2])))

            else:
                return 'До бонуса осталось:' + str(int(users[n][3]))

        elif body.lower() == 'помощь':
            answer = 'Вот что я могу: \nКлава (клавиатура с некоторыми командами)\nПередать <id> <сумма>\n' + 'Казино <сумма>\n' + 'Баланс \nБанк\nБанк положить\n Банк снять\nперевести <from> <to> <text>\nязыки(список языков для переводчика)' + '\nРаботать \n' + 'Бонус \n' + 'имя <имя>\nскажи <слова(<=500)>(будет отправлена ссылка на документ)\n' + 'топ (топ игроков)\nнаписать админу <сообщение>\nГраф <массив> (Пример: [[1,4],[0,3],[4],[1],[0,2]])' + '\nсс(по-русски) <число> <системы счисления из которой нужно перевести> <в которую>\n\n(Version: 0.2)'

            if users[n][5] == 'Admin':
                answer += '\nДоп команды для админов:\nПолучить <сумма>\nСоздать команду\nпомощь создать\nget_all_ids\nget_all_users\nюзеры(как get_all_users, красивее и проще)\nget_me (инфо о тебе)'
            if users[n][0] == '502004139' or users[n][0] == '155118230':
                answer += '\nДоп команды для меня: \nprefix\nedit_profile <id> <prefix> <значение>'
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

            new_per = [i for i in new_per if i[0] != '155118230' and str(i[0]) != '502004139']
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

            if users[n][5] == 'Admin': #  TODO
                return 'Данная функция находится в активной разработке'

        elif body.lower() == 'профиль':
            return 'Ваш профиль, ' + users[n][-1] + ':\n1. Ваш id: ' + users[n][
                                            0] + '\n2. Баланс:' + self.beauty(
                                            str(int(float(users[n][1])))) + '\n3. В банке ' + self.beauty(
                                            str(int(float(users[n][8])))) + '\n4. Рейтинг: ' + users[n][
                                                       2] + '\n5. Привилегия: ' + users[n][5] + '\n6. Голод: ' + users[n][14]






        elif body.lower().split()[:2] == ['создать', 'команду']:
            return 'Данная функция находится в активной разработке' #  TODO
            # if users[n][5] == 'Admin':
            #     all = body.lower().split()
            #     if all[2] == 'рандом':
            #         cg.random(all[3], all[4])
            #         vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
            #     elif all[2] == '50%50':
            #         cg.halfchance(all[3], all[4])
            #         vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})


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
                return 'Вы передали игроку ' + users[ids.index(g[1])][-1] + ' ' + g[2] + ' $' + '|_|_|' + 'Вам передал ' + users[n][-1] + ' ' + g[2] + ' $' #  TODO
            elif g[2].isdigit() and int(float(users[n][1])) < int(g[2]):
                return 'Недостаточно денег'
            elif not g[1] in ids:
                return 'ID не существует'
            else:
                return 'В боте это не предусмотренно'


        elif body.lower() == 'банк':
            return 'В банке ' + self.beauty(str(int(float(users[n][8]))))

        elif body.lower().split()[:2] == ['банк', 'положить'] and len(body.lower().split()) >= 3 and \
                body.lower().split()[2].isdigit():

            if int(float(users[n][1])) >= int(float(body.lower().split()[2])):
                users[n][8] = str(int(float(users[n][8])) + int(float(body.lower().split()[2])))
                users[n][1] = str(int(float(users[n][1])) - int(float(body.lower().split()[2])))
                vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})
            else:
                vk.method('messages.send', {'peer_id': id, 'message': 'Недостаточно денег'})


        elif body.lower().split()[:2] == ['банк', 'снять'] and len(body.lower().split()) >= 3:

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


        elif len(body.split()) > 1 and body.split()[0].lower() == 'edit_profile' and len(body.split()) == 4 and (
                users[n][0] == '502004139' or users[n][0] == '155118230'):

            args = body.split()[1:]

            users[ids.index(args[0])][int(args[1])] = args[2]
            vk.method('messages.send', {'peer_id': id,
                                        'message': '[id' + users[ids.index(args[0])][0] + '|' +
                                                   users[ids.index(args[0])][-1] + ']' + ' теперь имеет ' + args[
                                                       2] + ' ' + typer(args[1])})
            replace_line('users.txt', ids.index(str(args[0])), ','.join(users[ids.index(args[0])]) + '\n')


        elif body.lower() == 'prefix' and (users[n][0] == '502004139' or users[n][0] == '155118230'):

            pref = [str(i) + ' - ' + typer(str(i)) for i in range(len(users[0]))]
            vk.method('messages.send', {'peer_id': id, 'message': '\n'.join(pref)})

        elif body.lower() == 'get_all_ids' and users[n][5] == 'Admin':

            vk.method('messages.send', {'peer_id': id, 'message': ' '.join(ids)})
        elif body.lower() == 'get_all_users' and users[n][5] == 'Admin':

            uss = [','.join(i) for i in users]
            uss = '\n'.join(uss)
            vk.method('messages.send', {'peer_id': id, 'message': uss})

        elif body.lower() == 'юзеры' and users[n][5] == 'Admin':

            uss = ["[id" + i[0] + "|" + i[-1] + "] \n" + 'id: ' + i[0] + '\n' + 'привилегия: ' + i[
                5] + '\nденьги,рейтинг:' + i[1] + ',\t' + i[2] + '\n\n' for i in users if len(i) > 1]
            uss = '\n'.join(uss)
            vk.method('messages.send', {'peer_id': id, 'message': uss})

        elif body.lower() == 'get_all_admins' and users[n][5] == 'Admin':

            adm = ["[id" + i[0] + "|" + i[-1] + "] " + i[0] for i in users if len(i) > 1 and i[5] == 'Admin']
            adm = '\n'.join(adm)
            vk.method('messages.send', {'peer_id': id, 'message': adm})

        elif body.lower() == 'yayangi':

            if users[n][12] == '0':
                users[n][12] = '1'
                users[n][2] = str(float(users[n][2]) + 50)
                vk.method('messages.send', {'peer_id': id, 'message': 'Воу, вы нашли читкод, награда 50 рейтинга'})
            else:
                vk.method('messages.send', {'peer_id': id, 'message': 'Ты уже вводил этот читкод'})

        elif body.lower() == 'get_me' and users[n][5] == 'Admin':

            getting = [typer(str(i)) + ' ' + str(users[n][i]) + '\n' for i in range(len(users[n]))]
            vk.method('messages.send', {'peer_id': id, 'message': ''.join(getting)})

        elif body.lower().split()[:2] == ['написать', 'админу']:

            message = body.split()[2:]
            di = str(users[n][0])
            di = "[id" + users[n][0] + "|" + users[n][-1] + " " + users[n][0] + "]"
            # print(di)

            vk.method('messages.send', {'peer_id': '155118230', 'message': ' '.join(message) + "\nby: " + di})
            vk.method('messages.send', {'peer_id': id, 'message': 'Готово'})



        elif body.lower().split()[:1] == ['перевести']:

            eng_text = body.split()[1:]
            langs = [eng_text[0], eng_text[1]]
            eng_text = body.split()[3:]

            eng_text = ' '.join(eng_text)
            # print(eng_text, langs)
            if langs[0] in all_lang and langs[1] in all_lang:
                url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
                trans_option = {'key': token, 'lang': langs[0] + "-" + langs[1], 'text': eng_text}
                # trans_option = {'key': token, 'lang': "en-ru", 'text': eng_text}
                webRequest = requests.get(url_trans, params=trans_option)
                rus_text = webRequest.text
                srez = 32 + len(langs[0]) + len(langs[1])
                rus_text = rus_text[srez:(len(rus_text) - 3)]

                vk.method('messages.send', {'peer_id': id,
                                            'message': rus_text + '\n\nПереведено сервисом «Яндекс.Переводчик»\nhttp://translate.yandex.ru/'})
        elif body.lower() == 'языки':

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

            print('graph')
            if body.lower().split()[1] == 'рандом':
                nums = random.choice(range(1, 15))
                # print(nums)
                points = [i for i in range(nums)]
                # print(points)
                comps = random.choice(range(nums, nums + 5))
                # print(nums)
                cord = [[random.choice(points) for i in range(random.choice(range(1, 5)))] for i in range(nums)]
                # print(''.join(str(cord).split()))

                try:
                    # cord = json.loads(cord)
                    grouptest.graph(cord)
                    a = vk.method("photos.getMessagesUploadServer")
                    b = requests.post(a['upload_url'], files={'photo': open('test.png', 'rb')}).json()
                    c = vk.method('photos.saveMessagesPhoto',
                                  {'photo': b['photo'], 'server': b['server'], 'hash': b['hash']})[0]
                    d = "photo{}_{}".format(c["owner_id"], c["id"])
                    vk.method('messages.send',
                              {'peer_id': id, "attachment": d, "message": 'Вот граф ' + ''.join(str(cord).split())})
                except:
                    vk.method('messages.send', {'peer_id': id, "message": 'Ошибка'})
            elif body.lower().split()[1] != 'рандом':

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

            pass

        elif body.lower() == 'клава':

            vk.method("messages.send", {"peer_id": id, "message": "Клавиатура выведена", "keyboard": keyboard})

        elif body.lower() == 'есть':

            if float(users[n][1]) < 500:
                vk.method("messages.send", {"peer_id": id,
                                            "message": ":( недостаточно денег, вы можете начать игру сначала, написав заново <ваш id>"})
            else:
                users[n][1] = str(float(users[n][1]) - 500)
                users[n][14] = str(10)
                vk.method("messages.send", {"peer_id": id, "message": "Вы поели на 500$"})

        elif body.lower() == 'заново ' + users[n][0]:

            print(users[n][5])

            users[n][1], users[n][2], users[n][3], users[n][4], users[n][6], users[n][7], users[n][
                8] = '0', '0', '10', '10', '0', '1000', '0'
            users[n][9], users[n][10], users[n][11], users[n][12], users[n][13], users[n][
                14] = '0', '0', '0', '0', '1', '10'
            vk.method("messages.send",
                      {"peer_id": id, "message": "Ваш аккаунт сброшен. Сохранено: привилегия, имя"})



        # elif body.split()[0].lower() == 'скажи' or body.split()[0].lower() == 'tts' or body.split()[
        #     0].lower() == 'ттс':
        #
        #     words = ' '.join(body.split()[1:])

        #     hr = speech.speech(words, id, 'ru')

        #     vk.method('messages.send', {'peer_id': id, 'message': 'https://vk.com/' + hr})  # отправляю сообщение

        elif len(body.lower().split()) == 1 and (
                len(body.lower().split('e')) == 1 or len(body.lower().split('е')) == 1):

            # print(body.lower().split('e'))
            if len(''.join(body.lower().split('е'))) == 0:
                vk.method('messages.send', {'peer_id': id, 'message': 'Б' + 'О' * len(body) + 'Й'})

            elif len(''.join(body.lower().split('e'))) == 0:
                vk.method('messages.send', {'peer_id': id, 'message': 'B' + 'O' * len(body) + 'Y'})


        elif len(body.lower().split()) == 4 and body.lower().split()[0] == 'сс':

            body = body.lower().split()
            try:
                vk.method('messages.send', {'peer_id': id, 'message': str(
                    convert_base(str(body[1]), int(body[2]), int(body[3])))})

            except:
                vk.method('messages.send', {'peer_id': id,
                                            'message': 'Error!\n\n Возможно указано неверное значение системы из который нужно переводить.\nИли в числе используются не англ символы.\nЕсли все условия соблюдены - повторите попытку.'})
