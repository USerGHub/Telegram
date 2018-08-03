import telebot

bot = telebot.TeleBot('606971001:AAGYAt9B8RskqCjczuZ9q5D0UtLLl_QX8jI')

def handle_text(message):
    if message.text == 'Прив':
        bot.send_message(message.from_user.id, 'Здраствуй')
    
bot.polling(none_stop=True, interval = 1)
