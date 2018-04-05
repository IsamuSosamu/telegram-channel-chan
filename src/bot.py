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
    print(update.message)
    if update.message.text:
        print(bot.sendMessage(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                        text=update.message.text,
                        disable_notification=True
                        ))
    elif update.message.sticker:
        print(bot.sendSticker(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                         sticker=update.message.sticker['file_id'],
                         disable_notification=True))
    elif update.message.photo:
        print(bot.sendPhoto(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                         photo=update.message.photo[0]['file_id'],
                         disable_notification=True))
    elif update.message.voice:
        print(bot.sendVoice(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                  voice=update.message.voice['file_id'],
                  disable_notification=True))
    elif update.message.video:
        print(bot.sendVideo(chat_id=os.environ['CHANNELBOT_CHANNEL'],
                  video=update.message.video,
                  disable_notification=True))
    elif update.message.video_note:
        print(bot.sendVideoNote(chat_id=os.environ['CHANNELBOT_CHANNEL'],
              video_note=update.message.video_note['file_id'],
              disable_notification=True))

if __name__ == '__main__':
    main()
