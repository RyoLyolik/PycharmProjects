from chatterbot import ChatBot

chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer

conversation = ['Bot', 'Привет!',
                'Салют!',
                'Привет',
                'Лучше не бывает!',
                'Как дела',
                'Отлично! Приятно слышать.',
                'У меня тоже все хорошо',
                'Отлично, приятно слышать!']

conversation = open('C:/Users/bicho/Desktop/dialog_converter-master/movie_lines2.txt').readlines(100000)
# print(conversation)
conversation = [i[1:] for i in conversation if i != '']
# print(conversation)
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

while True:
    ans = input()
    response = chatbot.get_response(ans)
    print(response)
    # print(chatbot)
