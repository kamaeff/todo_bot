from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Добавить задачу', callback_data='add_data'),
   InlineKeyboardButton(text='Список задач', callback_data='data_list')],
  # [InlineKeyboardButton(text='Сайт', web_app=WebAppInfo(url='https://stockhub12.ru'))]
])

_list = [1, 2, 3]

async def inline_keyboard():
  keyboard = InlineKeyboardBuilder
  for item in _list:
    keyboard.add(InlineKeyboardButton(text=item, callback_data=item))