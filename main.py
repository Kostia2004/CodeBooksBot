from config import token
import logging
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
