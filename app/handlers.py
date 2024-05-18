from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from app.keyboards import main
from app.config import TOKEN
from random import randint

bot = Bot(token = TOKEN)
router = Router()
in_img =[]

@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(text = f"Привет, {message.from_user.first_name}! Готов зарядиться мотивацией?",
                         reply_markup=main)

@router.message(F.text == 'Что я умею?')
async def about(message: types.message):
    await message.answer(text="Я бот - мотиватор. По нажатию кнопки вы получите от меня мотивирующую картинку.")

@router.message(F.text == 'Отправить мотивационную картинку')
async def send(message: types.Message):
    image_url = in_img[randint(0, len(in_img)-1)]
    await bot.send_photo(message.chat.id, str(image_url))

def image(x):
    in_img.append(x)