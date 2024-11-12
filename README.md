# Vanger Test Task
***
Лэндинг со слайдером картинок, настраиваемым через админ-панель.

## Демо-версия:
1. Расположена по адресу: http://178.21.8.237:8000/
2. Админка по адресу: http://178.21.8.237:8000/admin/
3. **Логин:** A  
**Пароль:** 1111

## Установка и использование:
- Клонируйте репозиторий; перейдите в нужную директорию и выполните:
```sh

```
- Установите виртуальное окружение и активируйте его:
> Установка и активация в корневой папке проекта
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate # for macOS
```
```bash
source venv/Scripts/activate # for Windows
```
- Установите зависимости: (из директории, содержащей req.pip)
```bash
pip install -r req.pip
```
- В директории проекта (содержащей файл manager.py) создайте .env, содержащий **DJANGO_KEY** (секретный ключ django), **DB_NAME**, **USER_NAME**, **USER_PASSWORD** (данные для подключения к бд MySQL)  
Пример наполнения env-file:
```bash
SECRET_KEY = 'django-insecure-auw3xt4b4-i!-8je2v36z)^h_rzpw@c13i)rp*)%9bjn1v$eq&'

DEBUG = 'True'

ALLOWED_HOSTS = '127.0.0.1, localhost,'

DB_NAME=my_database

USER_NAME=root

USER_PASSWORD=root_password
```
- Совершите миграции и создайте суперпользователя: (из директории, содержащей manage.py)
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py createsuperuser
```
```bash
Login: A
Email: 1@1.ru
Password: 1111
Password repeat: 1111
```
- Запустите проект (из директории, содержащей файл manage.py):
```bash
python3 manage.py runserver
```

### Автор
[Кабанов Антон](https://github.com/Och1ta) 