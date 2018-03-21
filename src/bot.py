#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Bot forwards your message to channel.')

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def main():
    """Run the bot."""
    updater = Updater(os.environ['CHANNELBOT_TOKEN'])
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(filters=Filters.all,
                                  callback=send_message))

    # Start the Bot
    updater.start_polling()

    updater.idle()

def send_message(bot,update):
    """Send message based on message type"""

    if update.message.text:
        print('attemting to send')
        print(bot.sendMessage(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                        text=update.message.text,
                        disable_notification=True
                        ))
    elif update.message.sticker:
        print(bot.sendSticker(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                         sticker=update.message.sticker,
                         disable_notification=True))



if __name__ == '__main__':
    main()