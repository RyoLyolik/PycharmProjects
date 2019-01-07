import vk_api
import random
import time

casino = True

def all():
    global cnt_2, casino
    vk = vk_api.VkApi(login='89605187783', password='1524360798')
    vk._auth_token()

    casino = True
    cnt_2 = 0

    commands = 'Работать Баланс Ферма Курс'
    commands = commands.split()
    cnt = 0
    orig_id = 0
    all = False
    while True:
        try:
            messages = vk.method('messages.getConversations', {'out': 0, 'time_offset': 60, 'count': 100, 'filter': "unread"})
            if messages['count'] >= 1 and casino:
                id = messages['items'][0]['last_message']['from_id']
                usid = messages['items'][0]['last_message']['peer_id']
                body = messages['items'][0]['last_message']['text']

                if 'Баланс:' and '(' and ')' in body and int(id) == -158861435 and casino:
                    data = body.split()
                    try:
                        data[4] = float(data[4][2:-1])
                    except ValueError:
                        data = [0, 0, 0, 0, 1]

                    mult = data[4]

                    if mult >= 1:
                        cnt = 0

                    if cnt >= 2:
                        vk.method('messages.send', {'peer_id': id, 'message': 'Казино все'})
                        all = True

                    elif mult < 1:
                        cnt += 1
                        vk.method('messages.send', {'peer_id': id, 'message': 'Казино ' + str(random.choice(range(1, 100)))})
                        all = False

                    elif mult >= 1:
                        cnt = 0
                        vk.method('messages.send', {'peer_id': id, 'message': 'Казино ' + str(random.choice(range(1, 100)))})
                        all = False


                    print(mult, cnt)
                    if mult == 0 and all:
                        print('ну ты и лох')
                        quit(0)
                    time.sleep(3)

                time.sleep(3)

            elif messages['count'] < 1 and casino:
                print('out')
                vk.method('messages.send', {'peer_id': -158861435, 'message': 'Казино ' + str(random.choice(range(1, 100)))})
                time.sleep(300)

            elif casino is False and messages['count'] >= 1:
                id = messages['items'][0]['last_message']['from_id']
                usid = messages['items'][0]['last_message']['peer_id']
                body = messages['items'][0]['last_message']['text']

                if 'биткоины' in body and int(id) == -158861435 and casino:
                    vk.method('messages.send',{'peer_id': -158861435, 'message':'Продать биткоин '+body.split()[3][:-2]})
                    casino = True
                    cnt_2 = 0

                elif 'Баланс:' and '(' and ')' in body and int(id) == -158861435 and casino:
                    vk.method('messages.send', {'peer_id': -158861435, 'message': 'Ферма'})
                    cnt_2 = 0

                time.sleep(3)


            elif messages['count'] < 1 and not casino:
                vk.method('messages.send', {'peer_id': -158861435, 'message': 'Ферма'})
                time.sleep(3000)

            else:
                time.sleep(3)

        except:
            print('Captcha needed')
            time.sleep(30)

def careful():
    global cnt_2, casino
    vk = vk_api.VkApi(login='89605187783', password='1524360798')
    vk._auth_token()

    casino = True
    cnt_2 = 0

    commands = 'Работать Баланс Ферма Курс'
    commands = commands.split()
    bal= int(input())
    orig_id = 0
    stavka = 0.02 * bal
    while True:
        try:
            messages = vk.method('messages.getConversations', {'out': 0, 'time_offset': 60, 'count': 100, 'filter': "unread"})
            if messages['count'] >= 1:
                id = messages['items'][0]['last_message']['from_id']
                usid = messages['items'][0]['last_message']['peer_id']
                body = messages['items'][0]['last_message']['text']

                if 'Баланс:' and '(' and ')' in body and int(id) == -158861435 and casino:
                    data = body.split()
                    try:
                        data[4] = float(data[4][2:-1])
                    except ValueError:
                        data = [0, 0, 0, 0, 1]

                    mult = data[4]
                    print(mult, stavka, bal)

                    if mult >= 1:
                        stavka = 0.02*bal
                        bal = mult*bal
                        vk.method('messages.send', {'peer_id': id, 'message': 'Казино ' + str(stavka)})

                    elif mult < 1:
                        bal = mult * bal
                        stavka = stavka*2 if stavka != 0 else 0.02*bal
                        vk.method('messages.send', {'peer_id': id, 'message': 'Казино ' + str(stavka)})
                    time.sleep(3)

                time.sleep(3)

            elif casino is False and messages['count'] >= 1:
                id = messages['items'][0]['last_message']['from_id']
                usid = messages['items'][0]['last_message']['peer_id']
                body = messages['items'][0]['last_message']['text']

                if 'биткоины' in body and int(id) == -158861435 and casino:
                    vk.method('messages.send',{'peer_id': -158861435, 'message':'Продать биткоин '+body.split()[3][:-2]})
                    casino = True
                    cnt_2 = 0

                elif 'Баланс:' and '(' and ')' in body and int(id) == -158861435 and casino:
                    vk.method('messages.send', {'peer_id': -158861435, 'message': 'Ферма'})
                    cnt_2 = 0

                time.sleep(3)


            elif messages['count'] < 1 and not casino:
                vk.method('messages.send', {'peer_id': -158861435, 'message': 'Ферма'})
                time.sleep(3000)

            else:
                time.sleep(3)

        except:
            time.sleep(30)

if __name__ == '__main__':
    all() if input() == 'all' else careful()
