# Проектная работа 4 спринта
Вводная часть

# Описание проекта
Краткое описание проекта

# Документация API
Надо решить: OpenAPI или Wiki.js

# Технологии
- Код приложения на Python + FastAPI;
- Приложение запускается под управлением сервера ASGI(uvicorn);
- База данных: PostgresSQL;
- Хранилище данных: ElasticSearch;
- Кеширование данных: Redis Cluster;
- Все компоненты системы запускаются через Docker.

# Как развернуть проект

Склонируйте репозиторий
```
git clone git@github.com:crank2303/4_sprint_15_team.git
```

Перейдите в каталог с проектом
```
cd 4_sprint_15_team
```

Скопируйте файл настроек окружения
```
cp .env.example .env
```

Запустите сборку контейнера
```
docker compose up -d --build
```
<br>
<hr>

# Админка и API
Для доступа в админку перейдите по адресу: 
Локально: <a href="http://localhost:8082/admin">http://localhost:8082/admin
Через Интернет: <a href="http://movies.house-me.ru/admin">http://lmovies.house-me.ru/admin
```
Логин: admin
Пароль: admin
```

Описание параметров эндроинтов доступно по адресу: 
Локально: <a href="http://localhost:8082/api/openapi">http://localhost:8082/api/openapi
Через Интернет: <a href="http://movies.house-me.ru/api/openapi">http://lmovies.house-me.ru/api/openapi
