from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from random import randint


def main():
    application = Application.builder().token("7249287527:AAGf5G97partpBxokwnvW2cjXboxF4_mUMc").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


main()
