from config import token
import logging
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.NOTSET)

# Initialize bot and dispatcher
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    keyboard = types.InlineKeyboardMarkup()
    language_button = types.InlineKeyboardButton(text='По языку', callback_data = "/language")
    topic_button = types.InlineKeyboardButton(text="По теме", callback_data = "/topic")
    keyboard.add(language_button, topic_button)
    await message.reply("Привет!\nЯ PrrogBooksBot!\nВыберите, как Вам будет удобнее ориентироваться", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
