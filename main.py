import socket
import time

# Не трогаем
BUFFER_SIZE = 1024

# Адрес сервера и порт
address_to_server = ('localhost', 8686)

# Имя пользователя, полученное через параметры запуска (первый параметр) и код вашего приложения
USERNAME = "dengadiplom"
APP = "B"

# Сообщение, отправляемое на сервер. Получаем строку LICENCE-dengadiplom-B (licence - сущ. license - глагол)0))0)0))
message = "LICENCE-" + USERNAME + "-" + APP

try:
    # Подключение к серверу
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(address_to_server)

    # Отправляем сообщение, кодировка utf-8 (это обязательно!)
    message = message.encode("utf-8")
    client.send(message)

    # Получаем результат результат и декодируем (тоже utf-8)
    data = client.recv(BUFFER_SIZE)
    data = data.decode('utf-8')
    print(data)
    if data == 'OK':
        print('Включаем приложение')  # Открываем окно через поток или типа того

        # Включаем магию
        pony = True
        while pony:
            data = client.recv(BUFFER_SIZE)
            data = data.decode("utf-8")
            print(data)
            # Раз в минуту от сервера приходит сообщение "ОК"/
            # В идеале сделать так, чтобы в случае если пришло что-то другое, программа закрывалась
            if data != 'OK':
                break
        # После выхода закрыть соединение
        client.close()
    elif data == 'NO':
        print('Открываем окно типа нет доступа к бизнес-приложенмию '
              'обратитесь к администратору ИС бла бла бла и отключаемся')
        client.close()

except socket.error:
    print("Вывести окно с ошибкой соединения с сервером")
