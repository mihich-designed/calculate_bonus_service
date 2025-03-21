calculate_bonus_service - микросервис для рассчета суммы бонусов с каждой
покупки.

Запуск:
1. Установка зависимостей: pip install requirements.txt

Для запуска вместе с БД и балансировщиком:
- Сборка образов и запуск контейнеров: docker-compose up --build -d

Для запуска непосредственно bonus_calculate_service:
- Введите в cmd: python app/main.py

Изменять условия начисления бонусов можно в конфигурационном файле:
./config/config.yaml