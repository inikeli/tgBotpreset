import config
from pyrogram import Client ,filters
import keyboard

bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name = "my_bot"
)
def button_filter(button):
    async  def func(_,__,msg):
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
    await message.reply(f'Тут будут игры')

@bot.on_message(filters.command("start"))
async def start(bot,message):
    await message.reply("Добро пожаловать!",reply_markup=keyboard.kb_main)
    await bot.send_photo(message.chat.id,"https://belkniga.by/upload/resize_cache/iblock/98e/c3u0azr6p2d48nitjsfxb7wot31p1h9z/350_350_17626458c13eabe00cfe36870533c95c9/obzh-5-kl-rabochaya-tetrad.jpg")
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