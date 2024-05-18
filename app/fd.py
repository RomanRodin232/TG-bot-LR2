from aiogram import Bot, Dispatcher, types, F, Router
from app.config import TOKEN
from parser import parser

bot = Bot(token = TOKEN)
router1 = Router()

@router1.message(F.text == 'Обновить')
async def send(message: types.Message):
    parser()
    await message.answer(text = "Картинки обновлены")