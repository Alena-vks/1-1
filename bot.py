import os
import time
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "your_chat_id_here")  # Заменим вручную при тесте

bot = Bot(token=BOT_TOKEN)

def send_signal(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

def check_match():
    # Пример простой логики для теста
    # Реальная логика будет сложнее: подключение к live-данным, xG и т.д.
    while True:
        send_signal("🟢 TEST SIGNAL: Арсенал – Реал. xG 1.78 – 0.44. Срочно входи!")
        time.sleep(900)  # Каждые 15 минут

if __name__ == "__main__":
    check_match()