# Reviews service

## О сервисе
Сервис по сбору комментариев.

Планы:
- добавить действия в засвисимости от эмоционального окраса комментария.

## Запуск
```commandline
poetry install
uvicorn app.main:app --reload
```

## Пример curl-запросов
```commandline
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/reviews/?sentiment=negative' \
  -H 'accept: application/json'
```

```commandline
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/reviews/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "что-то с чем-то"
}'
```

