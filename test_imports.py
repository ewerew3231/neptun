import spacy
import lingua
from lingua import Language
from deeppavlov import build_model, configs
import flask
import telegram
from telegram.ext import Application
import aiohttp
import googlemaps
from unidecode import unidecode
from transformers import AutoTokenizer
from deep_translator import GoogleTranslator
import openai
import pytz
from dotenv import load_dotenv

print("Все библиотеки успешно импортированы!")

# Загрузка языковых моделей
nlp_en = spacy.load('en_core_web_sm')
nlp_uk = spacy.load('uk_core_news_sm')

print("Языковые модели загружены успешно!")
