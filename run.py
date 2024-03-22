import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from prisma import Client

from config import TOKEN
from app.heandlers import router

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    client = Client()
    try:
        client.connect()
        print('Connectiing Succes')
        await dp.start_polling(bot)
    except Exception as e:
        print(f'Cannot connect to db. Stop proccessing\n{e}')
    finally:
        client.disconnect()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
