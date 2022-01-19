# Описание.

Проект «API для Yatube» даёт доступ к постам, комментариям, группам и подпискам блога Yatube в зависимости от статуса пользователя. Реализована аутентификация по JWT-токену.

Стек: Python 3, Django 3, Django REST Framework, Simple-JWT

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/KaterinaSolovyeva/api_final_yatube
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
# Примеры запросов к API.

Получить список всех публикаций. При указании параметров limit и offset выдача работаtn с пагинацией.
```
GET /api/v1/posts/
```
Получение публикации по id.
```
GET /api/v1/posts/{id}/
```
Получение комментария к публикации по id.
```
GET /api/v1/posts/{post_id}/comments/{id}/
```
