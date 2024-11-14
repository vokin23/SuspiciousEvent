Определить папку миграций - alembic init app/migrations
Сгенерировать миграцию - alembic revision --autogenerate
Применить миграцию - alembic upgrade head

Расширить файл requirements.txt новой зависимостью - pip freeze > requirements.txt

Запуск проекта из папки app - uvicorn app.main:app --reload


docker network create asbp

docker run --name asbp_db -p 5433:5432 -e POSTGRES_USER=testuser -e POSTGRES_PASSWORD=Fedora132 -e POSTGRES_DB=asbp -d postgres:16

docker run --name redis -p 6379:6379 -d redis:7.4

docker run --name booking_back -p 7777:8000  --network=test booking_image
