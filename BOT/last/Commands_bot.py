import vk_api
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
    lines = open(file_name, 'r',encoding="utf-8").readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
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
        replacer_line('Commands_bot.py',200, "\n\n\t\t\telif body.lower()=='"+name+"':\n\t\t\t\tvk.method('messages.send', {'peer_id': id, 'message': random.choice("+list+")})\n\n\n")
    def halfchance(self, name, list):
        ch = open('Commands_bot.py', 'a')
        replacer_line('Commands_bot.py',200, "\n\n\t\t\telif body.lower().split()[0]=='"+name+"':\n\n\t\t\t\t\tif body.lower().split()[1].isdigit and int(body.lower().split()[1]) <= float(users[n][1]):\n\t\t\t\t\tusers[n][1] = str(float(users[n][1])-int(body.lower().split()[1]))\n\t\t\t\t\trnd = random.choice("+list+")\n\t\t\t\t\tif rnd == body.lower().split()[2]:\n\t\t\t\t\t\tusers[n][1] = str(float(users[n][1])+(int(body.lower().split()[1])*2))\n\t\t\t\t\t\tvk.method('messages.send', {'peer_id': id, 'message': 'You are win ' + str(int(body.lower().split()[1])) + '\\nYour balance: ' + commands.bt(int(float(users[n][1])))})\n\t\t\t\t\telse:\n\t\t\t\t\t\tvk.method('messages.send', {'peer_id': id, 'message': 'You are lose ' + str(int(body.lower().split()[1])) + '\\nYour balance: ' + commands.bt(int(float(users[n][1])))})\n\n\n\n")


cg = CommandsGenerate()

wh = False

while True:
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
        usid = messages['items'][0]['last_message']['from_id']
        body = messages['items'][0]['last_message']['text']


        if not str(id) in ids:
            wh = False
            if wh == False:
                if body.lower() == 'hello':
                    vk.method('messages.send', {'peer_id': id, 'message': 'User' + ',' + ' ''hi!' + str(usid)})
            if body.lower().split()[0] == '�����������':
                name = body.split()[1:]
                name = ' '.join(name)
                idc.write(' ' + str(usid))
                userc.write(str(usid) + ',' + '0' + ',' + '0' + ',' + '10,' + '10,' + '0,' + name + '\n')
                vk.method('messages.send',
                          {'peer_id': id, 'message': '������� ������. ������ � ���� ���������� � ���, ��� ' + name + '\n�������� ������� ��� ������ ������ ������'})
            else:
                vk.method('messages.send', {'peer_id': id,
                                            'message': '���������� ������� �������. ��� ����� ��������: "����������� <���� ���>"'})

        elif str(usid) in ids:

            print(body + '\n' + 'by: ' + users[ids.index(str(usid))][-1])
            wh = True
            n = ids.index(str(usid))
            users[n][1] = str(round(float(users[n][1]), 2))
            if body.lower() == 'hello':
                vk.method('messages.send', {'peer_id': id, 'message': users[n][-1] + ',' + ' ''hi!'})


            elif body.lower() == '������':
                vk.method('messages.send', {'peer_id': id, 'message': users[n][-1] + ', ��� ������: ' + commands.bt(int(float(users[n][1])))})




            elif body.lower().split()[0] == '������':
                summ = body.split()[1]
                if (str(summ) != '���' and str(summ) != '��') and not str(summ).isdigit():
                    vk.method('messages.send', {'peer_id': id, 'message': '��� ������'})
                else:
                    if not str(summ).isdigit():
                        summ = float(users[n][1])

                    summ = float(summ)
                    if summ > float(users[n][1]):
                        vk.method('messages.send', {'peer_id': id, 'message': '������������ �����'})
                    else:
                        if summ > 0:
                            users[n][1] = str(float(users[n][1]) - summ)
                            ch = random.choice(range(1, 51))
                            if ch >= 1 and ch < 5:
                                m = 0
                                summ *= m
                            elif ch >= 5 and ch <= 10:
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
                            vk.method('messages.send', {'peer_id': id, 'message': '��� ������� (�' + str(
                                m) + ')' + '\n' + '��� ������: ' + commands.bt(int(float(users[n][1])))})


            elif body.lower() == '��������':
                if int(users[n][4]) <= 0:
                    users[n][1] = str(float(users[n][1]) + 100000)
                    vk.method('messages.send', {'peer_id': id, 'message': '�� ���������� 100000'})
                    users[n][4] = str(60)
                else:
                    vk.method('messages.send',
                              {'peer_id': id, 'message': '�������� �������� �����: ' + str(int(users[n][4]))})

            elif body.lower() == '�����':
                if int(users[n][3]) <= 0:
                    users[n][1] = str(float(users[n][1]) + 1000000)
                    vk.method('messages.send',
                              {'peer_id': id, 'message': '�� �������� 1000000' + '\n' + '��� ������: ' + commands.bt(int(float(users[n][1])))})
                    users[n][3] = str(60)
                else:
                    vk.method('messages.send',
                              {'peer_id': id, 'message': '�� ������ ��������:' + str(int(users[n][3]))})

            elif body.lower() == '�������':
                vk.method('messages.send', {'peer_id': id,
                                            'message': '��� ��� � ����: \n' + '������ <�����>\n' + '������ \n' + '�������� \n' + '����� \n' + '\n' + '(Version: 0.01)'})






            elif body.lower() == '������ �������':
                if users[n][5] == '1':
                    vk.method('messages.send',
                              {'peer_id': id, 'message': '����� ��������: ������� ������� <parameters>\n\n'
                                                         '���������:\n'
                                                         '1. ������ <name> <������ ��������� �������, ... , n-�� ��������� �������>\n'
                                                         '2. 50%50 <name> <1st, 2nd> (���� ������ �����/����)'})

            elif body.lower().split()[:2] == ['�������', '�������']:
                if users[n][5] == '1':
                    all = body.lower().split()
                    if all[2] == '������':
                        cg.random(all[3], all[4])
                        vk.method('messages.send', {'peer_id': id, 'message': '������'})
                    elif all[2] == '50%50':
                        cg.halfchance(all[3], all[4])
                        vk.method('messages.send', {'peer_id': id, 'message': '������'})

            elif body.lower().split()[0] == '��������':
                if users[n][5] == '1' and body.lower().split()[1].isdigit():
                    vk.method('messages.send', {'peer_id': id, 'message': '������'})
                    users[n][1] = str(int(users[n][1])+int(body.lower().split()[1]))








            # elif body.lower().split()[0] == '50chance':
            #
            #
            #     if body.lower().split()[1].isdigit and int(body.lower().split()[1]) <= float(users[n][1]):
            #
            #         users[n][1] = str(float(users[n][1]) - int(body.lower().split()[1]))
            #
            #         rnd = random.choice(['yes', 'no'])
            #
            #         if rnd == body.lower().split()[2]:
            #             users[n][1] = str(float(users[n][1]) + (int(body.lower().split()[1]) * 2))
            #
            #             vk.method('messages.send', {'peer_id': id, 'message': 'You are win ' + str(int(body.lower().split()[1]) * 2) + '\nYour balance: ' + commands.bt(int(float(users[n][1])))})












            else:
                vk.method('messages.send', {'peer_id': id, 'message': '�'})
            replace_line('users.txt', ids.index(str(usid)), ','.join(users[n]) + '\n')





















    time.sleep(1)