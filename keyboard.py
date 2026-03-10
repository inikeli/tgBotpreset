from pyrogram.raw.types import ReplyKeyboardMarkup
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
