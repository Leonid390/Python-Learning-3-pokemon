import telebot 
from logic import Wizard, Fighter
from config import token
from random import randint
from logic import Pokemon
bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,2)
        if chance == 1:
            pokemon = Wizard(message.from_user.username)
            a = 'Wizard'
        elif chance == 2:
            pokemon = Fighter(message.from_user.username)
            a = 'Wizard'
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, f'Класс: {a}')
        bot.send_photo(message.chat.id, pokemon.show_img())
        #bot.send_message(message.chat.id, pokemon.show_img())
        #bot.send_message(message.chat.id, pokemon.skill())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
            
@bot.message_handler(commands=['info'])
def inform(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.send_message(message.chat.id, f'У вас нет покемона, сначала получите его')
    
@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=['info'])
def inform(message):
    bot.send_message(message.chat.id, )

bot.infinity_polling(none_stop=True)

