# 6 вариант, Порфирьев Антон
## База данных
База данных написана на mysql с одной таблицей 

*CREATE TABLE rates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    currency_left VARCHAR(50) NOT NULL,
	currency_right VARCHAR(50) NOT NULL,
    exchange DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP()
);*

## db_fuctions.py

В этом файле обёртка для работы с БД, чтобы программа работала корректно должен стоять пакет **mysql**

## server.py

Здесь реализован сервер приложения (который запускается просто с помощью интепритатора python3)

Чтобы он запустился должны стоять пакет **flask**

Всего реализовано 2 RESTful API:
- **`GET /rates**: Получение актуальных курсов валют. Ответ включает в себя пары валют и их курсы.
- **`POST /exchange**: Обмен валюты. Запрос принимает исходную валюту, целевую валюту и сумму. Возвращает тоже количество денег, но в новой валюте

## swagger
Также реализован swagger, однако из-за того что это localhost. Могут быть пробемы с некоторыми расширениями браузеров.
Самый простой способ запуска вставить код в [swagger editor](https://editor.swagger.io/)
