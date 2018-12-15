# importing
from itertools import islice
import time
import random
import commands
import json
import requests
import grouptest
import speech
import fx
import apiai
from yandex import Translater
import vk_api
import xlwt
import xlrd


def convert_base(num, from_base=10, to_base=10):
    # first convert to decimal number
    n = int(str(num), int(from_base))

    # convert decimal to base
    alphabet = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]

    else:
        return convert_base(n // to_base, 10, to_base) + alphabet[n % to_base]


# func-ns which will change file with all ids
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
    out = open(file_name, 'w', encoding="utf-8")
    out.writelines(lines)
    out.close()


# yandex translate auth
token = 'trnsl.1.1.20180822T035034Z.c4e6b0734a1501db.3c10535039452db4d70963681df09234674e4b33'

all_lang = ['az', 'sq', 'am', 'en', 'ar', 'hy', 'af', 'eu', 'ba', 'be', 'bn', 'my',
            'bg', 'bs', 'cy', 'hu', 'vi', 'ht', 'gl', 'nl', 'mrj', 'el', 'ka', 'gu',
            'da', 'he', 'yi', 'id', 'ga', 'it', 'is', 'es', 'kk', 'kn', 'ca', 'ky',
            'zh', 'ko', 'xh', 'km', 'lo', 'la', 'lv', 'lt', 'lb', 'mg', 'ms', 'ml',
            'mt', 'mk', 'mi', 'mr', 'mhr', 'mn', 'de', 'ne', 'no', 'pa', 'pap', 'fa',
            'pl', 'pt', 'ro', 'ru', 'ceb', 'sr', 'si', 'sk', 'sl', 'sw', 'su', 'tg',
            'th', 'tl', 'ta', 'tt', 'te', 'tr', 'udm', 'uz', 'uk', 'ur', 'fi', 'fr',
            'hi', 'hr', 'cs', 'sv', 'gd', 'et', 'eo', 'jv', 'ja']

# VK auth
vk = vk_api.VkApi(token='9348c5fa44e74d04840ce92338aa10d7dc9784d626756f952ad8d2266a2e5417965ee306181c58111a75b')
vk._auth_token()


# creating keyboard for easier communication in VK
def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


# keyboard values
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

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))



dict_of_names = {
    'id': 0,
    'money': 1,
    'rating': 2,
    'work_time':3,
    'bonus_time': 4,
    'priv': 5,
    'work_up': 6,
    'pay': 7,
    'bank': 8,
    'nothing': 9,
    'pl_work?': 10,
    'x50': 11,
    'cheats': 12,
    'rating_mult': 13,
    'hungry': 14
}
# opening file with all users
idss = open('allids.txt', 'r')
idc = open('allids.txt', 'a')
ids = idss.read().split()
wb = xlrd.open_workbook('bot возраждение\mb.xlsx', on_demand = True)
sheet = wb.sheet_by_index(0)

book = xlwt.Workbook()

# Add a sheet to the workbook
sheet1 = book.add_sheet("Sheet1")
cc = 0

while True:
    # try:
        cc += 1

        # all files with users
        idss = open('allids.txt', 'r')
        idc = open('allids.txt', 'a')
        ids = idss.read()
        wb = xlrd.open_workbook('bot возраждение\mb.xlsx', on_demand=True)
        sheet = wb.sheet_by_index(0)

        book = xlwt.Workbook()

        # Add a sheet to the workbook
        sheet1 = book.add_sheet("Лист1")

        ids = idss.read().split()
        print(int(sheet.cell(2,dict_of_names['bonus_time']).value))
        for us in range(1, len(ids)):
            print(int(sheet.cell(us, dict_of_names['bonus_time']).value))
            if int(sheet.cell(us, dict_of_names['bonus_time']).value) > -10:
                row = sheet1.row(us)
                print(row)
                row.write(dict_of_names['bonus_time'], str(int(sheet.cell(us, dict_of_names['bonus_time']))-1))
        book.save("bot возраждение\wsd.xls")
        print(123)
        # pass
        time.sleep(1)
    # except:
    #     pass
# The data
# cols = ["A", "B", "C", "D", "E"]
# txt = [0,1,2,3,4]

# Loop over the rows and columns and fill in the values
# for num in range(2,5):
#       row = sheet1.row(num)
#       for index, col in enumerate(cols):
#           value = txt[index] + num
#           row.write(index, value)
#
# # Save the result
book.save("bot возраждение\wsd.xls")