from aiogram import Bot, Dispatcher, types, F
import asyncio
from app.handlers import router
from app.fd import router1
from app.config import TOKEN
from parser import parser

async def start():
    parser()
    bot = Bot(token = TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(router1)
    await dp.start_polling(bot)

def rabota():
    asyncio.run(start())