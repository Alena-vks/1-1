import os
import time
import logging
from telegram import Bot
from telegram.error import TelegramError

# Включим базовое логирование (для Railway logs)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Получаем токен и ID из переменных среды
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    logger.error("BOT_TOKEN или CHAT_ID не заданы в переменных окружения.")
    exit(1)

bot = Bot(token=BOT_TOKEN)

def send_signal(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        logger.info("Сообщение успешно отправлено.")
    except TelegramError as e:
        logger.error(f"Ошибка отправки: {e}")

def check_match():
    while True:
        send_signal("🟢 TEST SIGNAL: Арсенал – Реал. xG 1.78 – 0.44. Срочно входи!")
        time.sleep(900)  # Каждые 15 минут

if __name__ == "__main__":
    check_match()
