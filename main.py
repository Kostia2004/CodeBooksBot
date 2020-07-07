from config import token
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import telegram

# Configure logging
logging.basicConfig(level=logging.NOTSET)

# Initialize bot and dispatcher
updater = Updater(token=token, use_context=True)
dp = updater.dispatcher

def start(update, context):
    keyboard = [[InlineKeyboardButton('По языку', callback_data = "/language"),
                 InlineKeyboardButton("По теме", callback_data = "/topic")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет!\nЯ PrrogBooksBot!\nВыберите, как Вам будет удобнее ориентироваться", reply_markup=reply_markup)

def button(update, context): 
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    print(query.answer())
    print("{}".format(query.data))
    if ("{}".format(query.data)=='/topic'):
        keyboard = [[InlineKeyboardButton(text='Data Sciense', callback_data = "/DS"),
                     InlineKeyboardButton(text="Bots", callback_data = "/Bots"),
                     InlineKeyboardButton(text="Frontend", callback_data = "/frontend")],
                    [InlineKeyboardButton(text="Backend", callback_data = "/backend"),
                     InlineKeyboardButton(text="Blockchain", callback_data = "/blockchain"),
                     InlineKeyboardButton(text="Cryptography", callback_data = "/crypto")],
                    [InlineKeyboardButton(text="IOT", callback_data = "/iot"),
                     InlineKeyboardButton(text="Mobile dev", callback_data = "/mobile"),
                     InlineKeyboardButton(text="Game dev", callback_data = "/games")]]

        reply_markup = InlineKeyboardMarkup(keyboard)
        
        context.bot.send_message(chat_id=update.effective_chat.id, text = "Выберите тему", reply_markup=reply_markup)
    


def help_command(update, context):
    update.message.reply_text("Use /start to test this bot.")



def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
    
