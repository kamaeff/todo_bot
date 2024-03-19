import app.keyboards as key

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
  await message.answer(f"🫰🏼 Hello {message.from_user.first_name}!\n💭Отправь мне фото ;)",
                       reply_markup=key.main)

@router.message(F.photo)
async def get_photo(message: Message):
  photo_path = message.photo[-1].file_id
  await message.answer_photo(photo=photo_path,
                             caption= f'ID photo: {photo_path}')