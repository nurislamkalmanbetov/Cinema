# Установка базового проекта 
FROM python:3.8.10   

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей проекта в контейнер
COPY requirments.txt .

# Установка зависимостей проекта
RUN pip install -r requirments.txt 

# Копирование файлов проекта в контейнер
COPY . .

# Запуск проекта 
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# # # Запускаем Celery worker
# CMD ["celery", "-A", "sinema", "worker", "-l", "info"]

# # # Запускаем Celery beat
# CMD ["celery", "-A", "sinema", "beat", "-l", "info", "--scheduler", "beat.schedulers:DatabaseScheduler"]

# # # Запускаем Flower
# CMD ["celery", "flower", "-A", "sinema", "--port=5566"]

