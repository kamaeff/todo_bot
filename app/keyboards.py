from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo)

main = InlineKeyboardMarkup(inline_keyboard=[
  [InlineKeyboardButton(text='Добавить задачу', callback_data='add_data')],
  # [InlineKeyboardButton(text='Сайт', web_app=WebAppInfo(url='https://stockhub12.ru'))]
])