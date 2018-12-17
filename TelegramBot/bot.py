from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
import telegram

# 624990039:AAGTYXZ6cpD-GRCmgKLXDfBhrEz7WUPpUYk
# 5ef4fdfb36bb46728b64c62af81e5d97   support 26cd3d3225b342de92a5baae2c7f0ea5
updater = Updater(token='624990039:AAGTYXZ6cpD-GRCmgKLXDfBhrEz7WUPpUYk')  # Токен API к Telegram
dispatcher = updater.dispatcher


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')


def textMessage(bot, update):
    print(update['message']['text'])
    request = apiai.ApiAI('5ef4fdfb36bb46728b64c62af81e5d97').text_request()  # Токен API к Dialogflow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text  # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял.')


# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
