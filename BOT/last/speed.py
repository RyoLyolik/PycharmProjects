import wave
import struct
import vk_api

source = wave.open("say.wav", mode="rb")
dest = wave.open("say.wav", mode="wb")
dest.setparams(source.getparams())
# найдем количество фреймов
frames_count = source.getnframes()
frames_count *= 2
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
# собственно, основная строка программы - переворот списка
# newdata = data[::5]
print(type(data))
newdata = []
for i in range(len(data)):
    newdata.append(data[i])
    newdata.append(data[i])

newdata = tuple(newdata)
newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
# записываем содержимое в преобразованный файл.
dest.writeframes(newframes)
source.close()
dest.close()

def up(speed):
    if int(float(speed)) <= 50:
        dest.setparams(source.getparams())
        # найдем количество фреймов
        frames_count = source.getnframes()
        frames_count *= 2
        data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
        # собственно, основная строка программы - переворот списка
        # newdata = data[::5]
        # print(type(data))
        newdata = data[::int(float(speed))]
        # for i in range(len(data)):
        #     newdata.append(data[i])
        #     newdata.append(data[i])

        newdata = tuple(newdata)
        newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
        # записываем содержимое в преобразованный файл.
        dest.writeframes(newframes)
        source.close()
        dest.close()
        save()

def down(speed):
    if int(float(speed))<= 50:
        dest.setparams(source.getparams())
        # найдем количество фреймов
        frames_count = source.getnframes()
        frames_count *= 2
        data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
        # собственно, основная строка программы - переворот списка
        # newdata = data[::5]
        # print(type(data))
        # newdata = data[::int(float(speed))]
        newdata = []
        for i in range(len(data)):
            for j in range(int(float(speed()))):
                newdata.append(data[i])
                newdata.append(data[i])

        newdata = tuple(newdata)
        newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
        # записываем содержимое в преобразованный файл.
        dest.writeframes(newframes)
        source.close()
        dest.close()
        save()


def save():
    url = vk.method('docs.getUploadServer', {'type': 'audio_message'})[
        'upload_url']  # получаем ссылку для загрузки файла
    # print(url)
    files = [('file', ('say.wav', open('say.wav', 'rb')))]  # записываем этот файл в переменную
    # print(files,'files')
    url_2 = requests.post(url, files=files).text  # загружаем файл и получаем ответ
    # print(url_2, 'url2')
    RESPONSE = json.loads(url_2)['file']  # получаю ответ и перевожу в json
    RESPONSE_2 = vk.method('docs.save', {'file': RESPONSE})
    # print(RESPONSE,'response')
    # print(RESPONSE_2,'response_2')
    _id = RESPONSE_2[0]['id']
    # print(_id, 'id')
    owner_id = RESPONSE_2[0]['owner_id']  # получаю owner_id файла
    # print(owner_id, 'owner id')
    # print(owner_id)
    document = 'doc%s_%s' % (str(owner_id), str(_id))  # формирую ссылку на документs
    # print(document, 'href to doc')
    href = RESPONSE_2[0]['url']
    href = [i for i in href]
    href = href[14:]
    href = ''.join(href)
    # print(href)
    return href

down(2)