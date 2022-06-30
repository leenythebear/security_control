
# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка "Надежда". Если вы попали в этот репозиторий случайно - вы не сможете запустить, т.к. у вас нет доступа к БД банка. Но, вы сможете использовать код вёрстки или посмотреть как реализованы запросы к БД банка.
Пульт охраны банка - это сайт, который можно подлкючить к удаленной базе данных с визитами и карточками пропусков сотрубников нашего банка.

## Как установить

1. Скачайте репозиторий
2. Для работы скрипта нужен Python версии не ниже 3
3. Установите зависимости, указанные в файле requirements.txt командой pip:

``pip install -r requirements.txt``

## Переменные окружения

Для работы сайта необходимо создать файл `.env` и указать в нем следующие переменные окружения:
1. __ENGINE__ - используемый движок для доступа к базе данных и работы с ней
2. __HOST__ - адрес базы данных
3. __PORT__ - порт для подключения к базе данных
4. __NAME__ - имя базы данных
5. __PASSWORD__ - пароль базы данных
6. __USER__ - имя пользователя для входа в базу данных
7. __SECRET_KEY__ - Django secret key
8. __DEBUG__ - необходим для включения и отключения режима отладки. 
9. __ALLOWED_HOSTS__ - список хостов/доменов, использует этот сайт

Пример указания значений переменных окружения:

```
ENGINE=django.db.backends.mysql

HOST=database.host.org

PORT=7076

NAME=basename

PASSWORD=kjdi17

USER=username

SECRET_KEY=YOUR_SECRET_KEY

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1
``` 


DEBUG устанавливается в зависимости от необходимого режима: **True - режим отладки включен, False - отключен**. По умолчанию это значение будет False

## Запуск

Сайт запускается командой:

`python manage.py runserver 0.0.0.0:8000`


Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
