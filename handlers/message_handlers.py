from aiogram import types

from aiogram.fsm.context import FSMContext
import requests


async def start_handler(message: types.Message):
    url = "http://127.0.0.1:8000/api/v1/add-telegram-id/"
    data = {'telegram_id': message.from_user.id}
    response = requests.post(url,data)

    await message.answer(
        f"Добро пожаловать {message.from_user.full_name}, в Message Sender телеграмм бот\nВам нужно прислать мне свой токен чтобы я смогу отправлять вам сообщения",
    )
