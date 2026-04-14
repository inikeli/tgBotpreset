from pyrogram.emoji import UP_BUTTON
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
btn_startFishing = KeyboardButton(f'{emoji.FISHING_POLE} Начать рыбалку')
btn_shopFishing = KeyboardButton(f'{emoji.SHOPPING_BAGS} Магазин')
btn_backGame = KeyboardButton(f'{emoji.BACK_ARROW} Назад')

kb_fish = ReplyKeyboardMarkup(
    keyboard=[
        [btn_startFishing,btn_shopFishing,btn_backGame],
    ],
      resize_keyboard=True
)

btn_casting = KeyboardButton(f'{emoji.NATIONAL_PARK} Забросить удочку')
btn_catch = KeyboardButton(f'{emoji.HANDBAG} Улов')
btn_backFishing = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
kb_gaming = ReplyKeyboardMarkup(
    keyboard=[
        [btn_casting,btn_catch,btn_backFishing],
    ],
    resize_keyboard=True
)
btn_send = KeyboardButton(f'{emoji.DOLLAR_BANKNOTE} Продать улов')
btn_upRoad = KeyboardButton(f'{emoji.UP_BUTTON} Улучшить удочку')
btn_backGame = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
kb_shop = ReplyKeyboardMarkup(
    keyboard=[
        [btn_send,btn_upRoad,btn_backGame],
    ],
    resize_keyboard=True
)