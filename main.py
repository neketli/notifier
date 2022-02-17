from scripts import tg_bot, sl_bot, vk_bot
import psycopg2
import time

"""
 Микросервис для отправки уведомлений в мессенджеры, на основе скриптов

 Структура бд : TIMESTAMP – время добавления записи в таблицу;
 MESSENGER – параметр,  определяющий  тип мессенджера;
 DESTINATION – идентификатор  контакта  или  чата в мессенджере;
 MESSAGE – текст уведомления.
"""


# Класс DB реализует бизнес-логику работы с БД


class DB:
    def __init__(self, dbname='baza', user='postgres',
                 password='admin', host='localhost'):
        try:
            self.__conn = psycopg2.connect(dbname=dbname, user=user,  # dbname сделать адекватным
                                           password=password, host=host)
            self.__cursor = self.__conn.cursor()
            print("Connected")
        except psycopg2.Error as err:
            print("Connection error ", err)
        finally:
            if self.__conn:
                self.__conn.close()
                print("Disconnected")

    # Метод помогающий получить все поля из таблицы
    def get_table(self):
        self.__cursor.execute('''SELECT * FROM hac''')
        if self.__cursor.fetchall():
            print("Successful")
            return self.__cursor.fetchall()
        else:
            return []

    # Метод для удаления использованной строки по id - принимает в себя destination
    def delete_row(self, timestamp, destination):
        self.__cursor.execute('''DELETE FROM hac WHERE timestamp = ? and destination = ?''', (timestamp, destination, ))
        self.__conn.commit()
        print("Successful")


if __name__ == "__main__":
    # init databse
    db = DB()
    # init services, the bot token is passed as a parameter
    tg = tg_bot.Bot()
    sl = sl_bot.Bot()
    vk = vk_bot.Bot()
    while True:
        records = db.get_table()
        for record in records:
            timestamp, messenger, destination, message = record  # поменять порядок в зависимости от бд
            if messenger.toLower() == "tg":
                tg.send_message(destination, message)
                db.delete_row(destination)
            elif messenger.toLower() == "vk":
                vk.send_message(destination, message)
                db.delete_row(destination)
            elif messenger.toLower() == "sl":
                sl.send_message(destination, message)
                db.delete_row(destination)
            else:
                print("I don't know what it is => ", record)
        time.sleep(60)  # время в секундах
