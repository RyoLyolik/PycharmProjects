import sys
import time

def replace_line_bu(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def replacer_line(file_name, line_num, text):
    lines = open(file_name, 'r', encoding="utf-8").readlines()
    lines[line_num] = text
    out = open(file_name, 'w',encoding="utf-8")
    out.writelines(lines)
    out.close()


# print("""Я бы не хотел никогда услышать, как он говорит: '''Она сказала: "Он сказал: 'Дай мне двести рублей'"'''""")

while True:
    u = open('users.txt', 'r+')
    i = open('allids.txt', 'r+')
    u = u.read()
    i = i.read()
    code_2 = open('gbot.py', 'r', encoding='utf-8')
    code = code_2.read()
    # code = code.encode('utf-8')
    # print(code)
    s = open('c.txt', 'r+')

    c = s.read()
    c = c.encode('utf-8')
    # print(c)
    c = int(c)

    c += 1
    f = open('backups/users/users' + str(c)+'.txt', 'w+')
    f2 = open('backups/ids/allids'+str(c)+'.txt','w+')
    f3 = open('backups/sourcecode/code'+str(c)+'.txt', 'w+', encoding='utf-8')
    f3.writelines(code)
    f2.writelines(i)
    f.writelines(u)
    replace_line_bu('c.txt',0,str(c))
    f.close()
    f2.close()
    f3.close()
    time.sleep(1800)