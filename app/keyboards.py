from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Что я умею?')],
                                     [KeyboardButton(text='Отправить мотивационную картинку')],
                                     [KeyboardButton(text='Обновить')]],
                           resize_keyboard=True, input_field_placeholder='Выберите пункт ниже')