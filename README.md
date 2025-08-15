# Neptun

## Переменные окружения

Создайте файл `.env` в корневой директории проекта со следующими переменными:

```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_key
OPENCAGE_API_KEY=your_opencage_key
```

## Локальная разработка

1. Установите Python 3.10.8
2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
- Windows:
```powershell
.\venv\Scripts\Activate.ps1
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Установите языковые модели:
```bash
python -m spacy download en_core_web_sm
python -m spacy download uk_core_news_sm
```

## Запуск

Для разработки:
```bash
python main.py
```

Для продакшена:
```bash
gunicorn wsgi:app --config gunicorn_config.py
```

## Деплой на Render

1. Создайте аккаунт на Render.com
2. Подключите GitHub репозиторий
3. Создайте новый Web Service
4. Добавьте необходимые переменные окружения
5. Дождитесь завершения деплоя
