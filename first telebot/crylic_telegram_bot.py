# KRIL LOTIN TG BOT

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5828941901:AAFHJZ-ei9-Vzn10C5FZazzaLrgmIrgNjtA'

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def sen_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsez!"
    answer +=  "\nMatn kiriting:"
    bot.reply_to(message=message, text=answer)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    print(msg.isascii())
    if msg.isascii():
        answer = to_cyrillic(msg)
    else:
        answer = to_latin(msg)
    bot.reply_to(message, answer)

bot.polling()


# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_cyrillic(matn))

