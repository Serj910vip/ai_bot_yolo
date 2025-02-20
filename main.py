import telebot
#from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic
from model import get_class
import datetime

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7830796741:AAEmZsGGjvaLzyDgDwZcChJ4s9c2iU9e9Oc")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye или просто обычный текст. Если не знаешь, что на картинке, загрузи её и я тебе скажу кто это")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Рассказывай, что нового?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Возвращайся!")


@bot.message_handler(content_types=['text', 'photo'])
def handle_docs_photo(message):
    # Проверяем, есть ли фотографии
    if not message.photo:
        dtn = datetime.datetime.now()
        botlogfile = open('./ai_bot_safety/TestBot.log', 'a', encoding='utf-8')
        print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, 'NickName: ' + message.from_user.username, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
        botlogfile.close()
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку :(")
    
    if message.photo:
        # Получаем файл и сохраняем его
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = file_info.file_path.split('/')[-1]
        
        src='./ai_bot_safety/'+file_info.file_path

        # Загружаем файл и сохраняем
        downloaded_file = bot.download_file(file_info.file_path)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        result = get_class(input_image=src, output_image="./ai_bot_safety/photos/output_image.jpg", model_path="./ai_bot_safety/yolov3.pt")
        print(result)
        
        if result is None:
            bot.send_message(message.chat.id, 'На картинке никого нет')           
        else: 
            # bot.send_message(message.chat.id, result)
            with open('./ai_bot_safety/photos/output_image.jpg', 'rb') as f:
            # Отправляем фото с использованием файла
                bot.send_photo(message.chat.id, f, caption=result)




# Запускаем бота
bot.polling()





