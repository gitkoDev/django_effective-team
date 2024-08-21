# Effective team REST API
Rest API с использованием `Django` и `Django Rest Framework`

## Сущности
1. Creator
2. Team
3. Member
4. Request
5. Transaction

## Endpoints

#### CRUD операции

- /api/***имя_сущности***/ &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Добавить сущность (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/ &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Получить все сущности (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/***id***/ &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Получить сущность по id (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/***id***/ &ensp; `=>`  &ensp; **PUT** &ensp;  `=>` &ensp; Обновить сущность (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/***id***/ &ensp; `=>`  &ensp; **DELETE** &ensp;  `=>` &ensp; Удалить сущность (`creator`/`team`/`member`/`request`)

#### Операции с транзакциями

- /api/***transactions***/ &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Получить все транзакции 
- /api/***transactions***/ &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Осуществить транзакцию 

#### Операции с запросами на вступленние в комманды

- /api/***teams***/***id***/request &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Получить все запросы в команду 
- /api/***teams***/***id***/request &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Отправить запрос в команду
- /api/***teams***/***id***/recruit &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Принять в команду участников (отбор по выносливости в случае ограниченного количества мест в групппе)

## Swagger документация по доступным эндпоинтам
- /api/schema/swagger-ui/ &ensp; `=>`  &ensp; **GET** &ensp; 
- /api/schema/redoc/ &ensp; `=>`  &ensp; **GET** &ensp; 


## Запуск

Первоначальный запуск для установки всех небходимых зависимостей и миграций
```
make initUp
```

Повторный запуск

```
make up
```
