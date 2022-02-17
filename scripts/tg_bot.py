import telebot


class Bot:
    def __init__(self, token="2077073869:AAGcMYKv3Mf0nmrc0BBihA9PjPeyNUxwlaw"):
        self._bot = telebot.TeleBot(token)

    def send_message(self, destination, text):
        self._bot.send_message(destination, text)

    def start_polling(self):
        self._bot.polling(none_stop=True)


#def file_user_id(user, uid): # не вижу в этом необходимости, рома объяснит
#    # Открываем файл для записи
#    file = open(str(uid)+'.txt', 'w')
#    # Записываем
#    file.write("User: {}, id: {}\n".format(user, uid))
#    # Закрываем файл
#    file.close()

# @bot.message_handler(content_types=['text'])
# def send_message(message,text,id):
#
#     # bot = telebot.TeleBot("2077073869:AAGcMYKv3Mf0nmrc0BBihA9PjPeyNUxwlaw")
#     bot.send_message(id, text)
#     file_user_id(message.chat.id,)
#
#
# send_message(text="324234",id = someid)
#
# bot.polling(none_stop=True)


#@bot.message_handler(content_types=['text'])
#def send_text(message):
#    if message.text.lower() == '0':
#        bot.send_message(message.chat.id, "some sex")#records[0][4])
#        file_user_id(message.chat.id, message.chat.id)
#    elif message.text.lower() == '1':
#        bot.send_message(message.chat.id, message.chat.id)
#        print(message.chat.id)
#
#    elif message.text.lower() == '2':
#        bot.send_message(message.chat.id, '''хуй 2''')
#    else:
#        bot.send_message(message.chat.id, 'Моя твоя не понимать')
#        file_user_id(message.chat.id, message.chat.id)






