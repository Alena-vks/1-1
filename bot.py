import os
from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

try:
    bot.send_message(chat_id=CHAT_ID, text="🔁 РУЧНОЙ ТЕСТ: сообщение доставлено немедленно.")
    print("✅ Сообщение отправлено")
except TelegramError as e:
    print(f"Ошибка: {e}")
