import random
import config
from pyrogram import Client ,filters
import keyboard
from keyboard import kb_fish
import sqlite3
from transformers import pipeline

def get_data(message):
    user_text = message
    result = botGpt(
        user_text,
        max_length = 60,
        do_sample = True,
        temperature=0.9
    )
    answer = result[0]["generated_text"]
    return answer

botGpt = pipeline(
    "text-generation",
    model="ai-forever/rugpt3small_based_on_gpt2"
)
gpt_users = set()
conn = sqlite3.connect('fishing_game.bd')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS fishing_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fisherman TEXT NOT NULL,
    rod_type TEXT NOT NULL,
    weight REAL
    )
''')

conn.commit()

fish_dictionary = {
    "Карась": (18,50,1000),#(шанс, мин, макс)
    "Окунь": (15,20,500),
    "Лещ": (13,100,1700),
    "Голавль": (7,100,2500),
    "Сом": (10,500,25000),
    "Плотва": (23,20,300),
    "Карп":(13,500,12000),
    "Граната":(1,1200,1400)
}
fishes = fish_dictionary.keys()
dropChance = []
numder = (1,2,3,4,5,6,7,8,9,10)
weightChaince = [0.34, 0.25, 0.15, 0.1 , 0.07, 0.05 , 0.02 , 0.01 , 0.007 , 0.003]
for i in fishes:
    dropChance.append((fish_dictionary[i][0])/100)

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name = "my_bot"
)
def button_filter(button):
    async def func(_,__,msg):
        return msg.text == button.text
    return filters.create(func,"ButtonFilter", button=button)

@bot.on_message(filters.command("info") | button_filter(keyboard.btn_info))
async def info(bot,message):
    await message.reply("Привет, Этот бот для доброты")

@bot.on_message(filters.command("profile") | button_filter(keyboard.btn_profile))
async def profile(bot,message):
    await message.reply(f'Ваш id {message.chat.id} , Ваше имя {message.from_user.first_name}')

@bot.on_message(filters.command("gpt") | button_filter(keyboard.btn_gpt))
async def gpt(bot, message):
    gpt_users.add(message.chat.id)
    await message.reply("GPT-режим включён. Напишите запрос нейросети.")

@bot.on_message(filters.command("games") | button_filter(keyboard.btn_games))
async def games(bot,message):
    await message.reply(f'Выберите игру',reply_markup=keyboard.kb_games)

@bot.on_message(filters.command("start"))
async def start(bot,message):
    await message.reply("Добро пожаловать!",reply_markup=keyboard.kb_main)

@bot.on_message(filters.command("fish") | button_filter(keyboard.btn_fishing))
async def fish(bot,message):
    await message.reply(f'Рыбалка',reply_markup=kb_fish)

@bot.on_message(filters.command("back") | button_filter(keyboard.btn_back))
async def back(bot,message):
    await message.reply("Возврат назад", reply_markup=keyboard.kb_main)

@bot.on_message(button_filter(keyboard.btn_startFishing))
async def start_fishing(bot,message):
    await message.reply("Игра запущена",reply_markup=keyboard.kb_gaming)

@bot.on_message(button_filter(keyboard.btn_shopFishing))
async def shop_fishing(bot,message):
    await message.reply("Рыбацкий магазинчик",reply_markup=keyboard.kb_fishingShop)

@bot.on_message(button_filter(keyboard.btn_backGame))
async def backToGame(bot,message):
    await message.reply("Возвращаемся в меню игр",reply_markup=keyboard.kb_games)

@bot.on_message(button_filter(keyboard.btn_casting))
async def casting(bot,message):
    chosenFish = random.choices(list(fishes),dropChance)
    weight = fish_dictionary[chosenFish[0]]
    step = (weight[2] - weight[1]) / 10
    weight = random.choices(numder,weightChaince)[0] * step + weight[1] + random.randint(0,100)
    await message.reply("Вы поймали "+chosenFish[0] + " вес улова " + str(weight))

@bot.on_message(filters.command("maps") | button_filter(keyboard.btn_randomCords))
async def maps(bot,message):
    preset = "https://www.google.com/maps/@"
    degrees = random.randint(-90,90)
    preset = preset + str(degrees)+"."
    for i in range(7):
        number = random.randint(0,10)
        preset = preset+str(number)
    preset = preset + ","
    degrees = random.randint(-180, 180)
    preset = preset + str(degrees) + "."
    for i in range(7):
        number = random.randint(0,10)
        preset = preset+str(number)
    preset = preset + ",10z"
    await message.reply(preset)

@bot.on_message()
async def echo(bot, message):
    if message.chat.id in gpt_users:
        answer = get_data(message.text)
        await message.reply(answer)
        return
    if message.text == "Привет":
        await message.reply("Добро пожаловать в бота")
        await message.reply("Что вы хотите приобрести?")
    elif message.text == "Пока":
        await message.reply("Досвидания?")
    elif message.text == "бесплатные робуксы":
        for i in range(100):
            await message.reply("Робукс")

bot.run()