from gtts import gTTS
# import vk_api
# import json
# import requests
text = '''
Погиб поэт! — невольник чести —
        Пал, оклеветанный молвой,
        С свинцом в груди и жаждой мести,
        Поникнув гордой головой!..
        Не вынесла душа поэта
        Позора мелочных обид,
        Восстал он против мнений света
        Один, как прежде... и убит!
        Убит!.. к чему теперь рыданья,
        Пустых похвал ненужный хор
        И жалкий лепет оправданья?
        Судьбы свершился приговор!
        Не вы ль сперва так злобно гнали
        Его свободный, смелый дар
        И для потехи раздували
        Чуть затаившийся пожар?
        Что ж? веселитесь... — он мучений
        Последних вынести не мог:
        Угас, как светоч, дивный гений,
        Увял торжественный венок.
        Его убийца хладнокровно
        Навел удар... спасенья нет:
        Пустое сердце бьется ровно.
        В руке не дрогнул пистолет,
        И что за диво?.. издалека,
        Подобный сотням беглецов,
        На ловлю счастья и чинов
        Заброшен к нам по воле рока;
        Смеясь, он дерзко презирал
        Земли чужой язык и нравы;
        Не мог щадить он нашей славы;
        Не мог понять в сей миг кровавый,
        На что́ он руку поднимал!..
        И он убит — и взят могилой,
        Как тот певец, неведомый, но милый,
        Добыча ревности глухой,
        Воспетый им с такою чудной силой,
Сраженный, как и он, безжалостной рукой.
Зачем от мирных нег и дружбы простодушной
Вступил он в этот свет, завистливый и душный
Для сердца вольного и пламенных страстей?
Зачем он руку дал клеветникам ничтожным,
Зачем поверил он словам и ласкам ложным,
     Он, с юных лет постигнувший людей?..
И прежний сняв венок, — они венец терновый,
Увитый лаврами, надели на него:
     Но иглы тайные сурово
     Язвили славное чело;
Отравлены его последние мгновенья
Коварным шепотом насмешливых невежд,
     И умер он — с напрасной жаждой мщенья,
С досадой тайною обманутых надежд.
     Замолкли звуки чудных песен,
     Не раздаваться им опять:
     Приют певца угрюм и тесен,
     И на устах его печать.
     А вы, надменные потомки
Известной подлостью прославленных отцов,
Пятою рабскою поправшие обломки
Игрою счастия обиженных родов!
Вы, жадною толпой стоящие у трона,
Свободы, Гения и Славы палачи!
     Таитесь вы под сению закона,
     Пред вами суд и правда — всё молчи!..
Но есть и божий суд, наперсники разврата!
     Есть грозный суд: он ждет;
     Он не доступен звону злата,
И мысли и дела он знает наперед.
Тогда напрасно вы прибегнете к злословью:
     Оно вам не поможет вновь,
И вы не смоете всей вашей черной кровью
     Поэта праведную кровь!
'''
tts = gTTS(text=text, lang='ru')
name = "C:/Users/bicho/Desktop/SMERT.mp3"
tts.save(name)
# def speech(text, id, lang):
#     vk = vk_api.VkApi(login='89605187783', password='No')
#     vk._auth_token()
#     if len(text.split()) <= 500:
#         tts = gTTS(text=text, lang=lang)
#         name = "say.mp3"
#         tts.save(name)
#         url = vk.method('docs.getUploadServer', {'type': 'audio_message'})[
#             'upload_url']  # получаем ссылку для загрузки файла
#         files = [('file', (name, open(name, 'rb')))]  # записываем этот файл в переменную
#         url_2 = requests.post(url, files=files).text  # загружаем файл и получаем ответ
#         RESPONSE = json.loads(url_2)['file']  # получаю ответ и перевожу в json
#         RESPONSE_2 = vk.method('docs.save', {'file': RESPONSE})
#         _id = RESPONSE_2[0]['id']
#         owner_id = RESPONSE_2[0]['owner_id']  # получаю owner_id файла
#         document = 'doc%s_%s' % (str(owner_id), str(_id))  # формирую ссылку на документs
#         href = RESPONSE_2[0]['url']
#         href = [i for i in href]
#         href = href[14:]
#         href = ''.join(href)
#         # print(href)
#         return href
