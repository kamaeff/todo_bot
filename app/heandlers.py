import app.keyboards as key
import asyncio

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from db import add_user

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):

    username = message.from_user.first_name
    res = await add_user(str(message.from_user.id), username)

    if res == True:
        await message.answer(f"🫰🏼 Hello {username}!\n💭Отправь мне фото ;)", reply_markup=key.main)
    else:
        await message.answer(f'{username}, кажется мне не по себе. Заходи попозже (')


@router.message(F.photo)
async def get_photo(message: Message):
    photo_path = message.photo[-1].file_id
    await message.answer_photo(photo=photo_path, caption=f'ID photo: {photo_path}')
