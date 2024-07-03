from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Напишите "картинка", и я отправлю вам изображение.')

# Функция обработки текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    if "картинка" in text:
        # Отправляем изображение в ответ на сообщение, содержащее слово "картинка"
        update.message.reply_photo(photo=open('path_to_your_image.jpg', 'rb'))
    else:
        update.message.reply_text('Ваше сообщение не содержит слово "картинка".')

def main() -> None:
    # Введите свой токен от BotFather
    updater = Updater("YOUR_TOKEN_HERE")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
