import vk_api
import time
import random
import sys

# vk = vk_api.VkApi(token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
# vk._auth_token()
vk = vk_api.VkApi(login='89605187783', password='1524360798')
vk._auth_token()
cnt = 0
while True:
    # try:
    rnd = str(random.choice(range(1, 50)))
    messages = vk.method('messages.getConversations',
                         {'out': 0, 'time_offset': 60, 'count': 100, 'filter': "unread"})
    if messages['count'] >= 1:

        id = messages['items'][0]['last_message']['from_id']
        usid = messages['items'][0]['last_message']['peer_id']
        body = messages['items'][0]['last_message']['text']
        # try:
        mul = body.split()[4][2:-1]
        print('message by bot')
        # vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино 1'})
        # except:
        # mul = False
        # print('message isnt by  bot')
        if cnt > 3:
            vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино все'})
            print('printing казино все')
            cnt = 0
        # print(id,mul)

        else:
            try:
                if usid == -158861435:
                    # if mul:
                        if float(mul) < 1:
                            vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино ' + rnd})
                            print('printing казино 1\n')
                            cnt += 1

                        else:
                            print('cnt = 0\n')
                            vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино ' + rnd})
                            cnt = 0

                    # elif usid == -171493284:
                    #     vk.method('messages.send', {'peer_id': -171493284, 'message': 'Ok'})
                else:
                    vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино ' + rnd})
                    print('I dont have any message by this bot\n')
            except:
                print('EXCEPT')

        if messages['count'] >= 1:
            vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино ' + rnd})
    else:
        vk.method('messages.send', {'peer_id': -158861435, 'message': 'казино ' + rnd})
    print('cnt =', cnt)
    time.sleep(10)
# except:
#     print('Except')
#     time.sleep(2)
