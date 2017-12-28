Реинкарнация интеграции фреймворка Django с сервисом sape.ru.
За основу были взяты идеи проекта на https://github.com/Dimmma/sape и его форка(https://github.com/fedosov/sape).

Данное приложение ориентировано исключительно на работу с Python 3. Причиной его создания послужила работа по миграции одного "пожилого" сайта с PHP на Python. 

## Установка
```bash
pip install django-sape3
```
или
```bash
pip install git+https://github.com/dalay/django-sape3.git
```
## Настройка

`settings.py`

```python
INSTALLED_APPS = (
    ...
    'sape',
)
```

```python
# SAPE.RU
# Обязательные настройки
SAPE_DOMAIN = 'example.com'
SAPE_USER = 'sape_username'
# Остальные настройки
SAPE_SHOW_CODE = False # Показывать или нет проверочный код sape
                       # (при добавлении страниц сайте в сервис).
SAPE_CHARSET = 'utf8' # Кодировка сайта
SAPE_DIR = '/tmp/sape_cache/' # Где будет храниться файл,
                              # содержащий полученные с sape ссылки.
```

## Шаблоны
### Общее использование
```
{% load sape %}
...
{% sape_links %} 
или так, если нужен заголовок для блока с ссылками
{% sape_links 'Заголовок блока ссылок' %} 
```
### Встроенные базовые шаблоны приложения
Родительский шаблон с кодом блока ссылок.
```
sape/block.hml 
```
Дочерний шаблон вывода для конкретно ссылок.
```
sape/links.html 
```

## Обновление ссылочной базы 
Получение ссылок для сайта с сервера sape.ru
```
./manage.py sape update
```

