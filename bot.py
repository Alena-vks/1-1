import os
import time
import logging
from telegram import Bot
from telegram.error import TelegramError

# Логирование для Railway
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Получение токена и ID из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Проверка переменных
if not BOT_TOKEN or not CHAT_ID:
    logger.error("❌ BOT_TOKEN или CHAT_ID не заданы.")
    exit(1)

# Инициализация бота
bot = Bot(token=BOT_TOKEN)

# Функция отправки сообщений
def send_signal(message):
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        logger.info("✅ Сообщение успешно отправлено.")
    except TelegramError as e:
        logger.error(f"Ошибка отправки сообщения: {e}")

# Основной цикл
def check_match():
    while True:
        send_signal("🟢 TEST SIGNAL: Арсенал – Реал. xG 1.78 – 0.44. Срочно входи!")
        time.sleep(900)  # Каждые 15 минут

# Точка входа
if __name__ == "__main__":
    check_match()
