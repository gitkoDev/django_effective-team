# Effective team Django test task 
Rest API с использованием `Django` и `Django Rest Framework`

## Сущности
1. Creator
2. Team
3. Member
4. Request

## Endpoints

#### API
- /api/***имя_сущности***/ &ensp; `=>`  &ensp; **POST** &ensp;  `=>` &ensp; Добавить сущность (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/ &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Получить все сущности (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/***id***/ &ensp; `=>`  &ensp; **GET** &ensp;  `=>` &ensp; Получить сущность по id (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/***id***/ &ensp; `=>`  &ensp; **PUT** &ensp;  `=>` &ensp; Обновить сущность (`creator`/`team`/`member`/`request`)
- /api/***имя_сущности***/***id***/ &ensp; `=>`  &ensp; **DELETE** &ensp;  `=>` &ensp; Удалить сущность (`creator`/`team`/`member`/`request`)
