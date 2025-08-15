import multiprocessing
import os

# Привязка к порту из переменной окружения или 10000 по умолчанию
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Количество рабочих процессов
workers = multiprocessing.cpu_count() * 2 + 1

# Таймаут
timeout = 120

# Другие настройки
keepalive = 5
max_requests = 1000
max_requests_jitter = 50

# Логирование
accesslog = '-'
errorlog = '-'
loglevel = 'info'
