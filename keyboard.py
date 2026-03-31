from pyrogram.types import ReplyKeyboardMarkup
from pyrogram.types import KeyboardButton
from pyrogram import emoji
btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} Игры')
btn_profile = KeyboardButton(f'{emoji.PERSON} Профиль')
btn_gpt = KeyboardButton(f'{emoji.ROBOT} Нейросеть')

kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_profile, btn_games],
        [btn_gpt, btn_info]
    ],
    resize_keyboard=True
)

btn_fishing = KeyboardButton(f'{emoji.FISH} Рыбалочка')
btn_randomCords = KeyboardButton(f'{emoji.GLOBE_SHOWING_EUROPE_AFRICA} Случайные координаты')
btn_back = KeyboardButton(f'{emoji.BACK_ARROW} Назад')

kb_games = ReplyKeyboardMarkup(
    keyboard=[
    [btn_fishing,btn_randomCords,btn_back],
],
    resize_keyboard=True
)