import asyncio
import logging

from aiogram import Bot, Dispatcher, F

from config import TOKEN
from app.heandlers import router
from db import conn

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
  dp.include_router(router)
  await dp.start_polling(bot)

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  asyncio.run(conn())
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
    print('Exit')