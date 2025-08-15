# Инструкции по установке виртуального окружения

1. Закройте VS Code

2. Откройте PowerShell от имени администратора

3. Разрешите выполнение скриптов (если требуется):
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

4. Выполните команды:
```powershell
cd "C:\Users\vavaika\Desktop\test"
Remove-Item -Recurse -Force venv -ErrorAction SilentlyContinue
python -m venv venv
.\venv\Scripts\Activate.ps1

# Установка базовых пакетов
pip install wheel==0.41.2 setuptools==68.0.0
pip install numpy==1.24.3
pip install tqdm==4.64.1
pip install spacy==3.7.4

# Установка языковых моделей
python -m spacy download en_core_web_sm
python -m spacy download uk_core_news_sm

# Установка остальных пакетов
pip install flask==3.0.2
pip install python-telegram-bot==20.8
pip install aiohttp==3.9.3
pip install googlemaps==4.2.0
pip install unidecode==1.3.8
pip install python-dotenv==1.0.1
pip install openai==0.28.1
pip install lingua-language-detector==1.3.2
pip install transformers==4.31.0
pip install sentence-transformers==2.2.2
pip install scikit-learn==1.0.2
pip install deep-translator==1.11.4
pip install pytz==2024.1
pip install requests==2.31.0
pip install pandas==1.5.3
pip install deeppavlov==1.1.0
pip install torch==1.13.1
pip install geopy==2.4.1
```

5. После выполнения всех команд, откройте VS Code снова

Если возникнут проблемы, обращайтесь за помощью.
