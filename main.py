import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6488561998:AAGiUfwq5t47UBLoH7_A0TYaQUufs5pnMgY')

@bot.message_handler(content_types=['photo'])
def photo(message):
    markup = types.InlineKeyboardMarkup
    btn1 = types.InlineKeyboardButton(types.InlineKeyboardButton('Переити на веб саит', url='https://www.youtube.com/shorts/chaLRQZKi6w?feature=share'))
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить', callback_data='edit')
    markup.row(btn2,btn3)
    bot.reply_to(message, 'Норм фото жокпа не?', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['website'])
def site(message):
        webbrowser.open('https://www.youtube.com/shorts/chaLRQZKi6w?feature=share')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'settings')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'admin':
        bot.send_message(message.chat.id,f'info, {message.from_user.first_name} ')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
    