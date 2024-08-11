import telebot

name = ''
surname = ''
email = ''
CHAT_ID = ''

bot = telebot.TeleBot('7346026260:AAFkDie023ZDmarmPuSk6FsYpdy7Ef-cY4M')
markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
itembtn1 = telebot.types.KeyboardButton('/start')
#itembtn2 = telebot.types.KeyboardButton('Сделать заказ')
#itembtn3 = telebot.types.KeyboardButton('Привет')
itembtn4 = telebot.types.KeyboardButton('/reg')
markup.add(itembtn1, itembtn4)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите опцию из меню ниже.", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Напиши /reg")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help или /reg.")

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Напиши email для завершения регистрации на сайте')
    bot.register_next_step_handler(message, get_email)

def get_email(message):
    global email
    email = message.text
    bot.send_message(message.from_user.id, f'Твой email {email} лет, тебя зовут {name} {surname}?')
    write_to_db(email, message.from_user.id, name, surname)


def write_to_db( _email, _id,_name, _surname):
    print(_email)
    f = open('C:\\Users\\Asus\\Documents\\GitHub\\FDA2\\flower_delivery\\customers_id.flower', "+w")
    new_text_file = '';
    flag = 0;
    line = f.readline()
    while (line != ''):
        if(line.find(_email) == 0):
            new_text_file = new_text_file + _email + ' ' + _id + ' ' + _name + ' ' + _surname + '\n'
            flag = 1;
        else:
            new_text_file = new_text_file + line + '\n'

    if(flag == 0):
        new_text_file = new_text_file + _email + ' ' + _id + ' ' + _name + ' ' + _surname + '\n'
    f.write(new_text_file)
    f.close();


def start_bot():
    print("Start TG Bot")
    bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
    start_bot()