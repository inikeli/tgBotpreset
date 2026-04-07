import random
import config
from pyrogram import Client ,filters
import keyboard
from keyboard import kb_fish

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
async def gpt(bot,message):
    await message.reply(f'Тут будет ГПТ')

@bot.on_message(filters.command("games") | button_filter(keyboard.btn_games))
async def games(bot,message):
    await message.reply(f'Тут будут игры',reply_markup=keyboard.kb_games)

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
async def echo(bot,message):
    if message.text == "Привет":
        await message.reply("Добро пожаловать в бота")
        await message.reply("Что вы хотите приобрести?")
    elif message.text == "Пока":
        await message.reply("Досвидания?")
    elif message.text == "бесплатные робуксы":
        for i in range(100):
            await message.reply("Робукс")
    elif message.text == "фото":
        await bot.send_photo(message.chat.id,"https://static.wikia.nocookie.net/dota2_gamepedia/images/c/c0/Pudge_icon.png/revision/latest?cb=20160411211506")

bot.run()