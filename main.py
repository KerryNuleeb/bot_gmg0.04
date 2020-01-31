from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import random
import datetime
import get_audio
import read_audio
import create_post
import log

token = log.get_token()
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
vk_session.api_version = 5.103


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, 2147483648),
                       "attachment": attachment, 'keyboard': keyboard})


def start():
    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                print("Текст сообщения: " + str(event.text))
                print(event.user_id)
                response = event.text.lower()


                if response.find('привет') != -1 and not (event.from_me):
                    send_message(vk_session, 'user_id', event.user_id, message='Хай!')
                    #get_audio.get(-210528)
                elif response.find('навали') != -1 and not (event.from_me):
                    attachment = read_audio.read()
                    send_message(vk_session, 'user_id', event.user_id, message='Наваливаю! Качает? Чи не? Трэш кал кста', attachment=attachment)
                elif response.find('работать') != -1:
                    attachment = 'photo580559802_457239019'
                    attachment += ',' + read_audio.read()
                    create_post.create(-33731414, 'Я съел админов теперь я тут главный!', session_api, attachment)
                    send_message(vk_session, 'user_id', event.user_id, message='Я насрал в предложку, иди чекни')
                elif response.find('обновить') != -1 and not (event.from_me):
                    f =open('audio.txt', 'w')
                    f.close()
                    get_audio.get(-45919397)
                    get_audio.get(-33731414)
                    send_message(vk_session, 'user_id', event.user_id, message='База данных успешно обновлена')



try:
    start()
except:
    print('Ошибка!!!')
    start()