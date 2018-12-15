from gtts import gTTS
import vk_api
import json
import requests

def speech(text, id, lang):
    vk = vk_api.VkApi(login='89605187783', password='1524360798')
    vk._auth_token()
    # print(len(text))
    if len(text.split()) <= 500:
        tts = gTTS(text=text, lang=lang)
        name = "say.mp3"
        tts.save(name)
        url = vk.method('docs.getUploadServer', {'type': 'audio_message'})['upload_url']  # получаем ссылку для загрузки файла
        # print(url)
        files = [('file', (name, open(name, 'rb')))]  # записываем этот файл в переменную
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

speech('Ало',155118230,'ru')