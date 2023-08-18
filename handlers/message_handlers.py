from aiogram import types

from aiogram.fsm.context import FSMContext
import requests

from utils.stateforms import StepsForm


async def start_handler(message: types.Message):
    await message.answer(
        f"Добро пожаловать в Message Sender Bot {message.from_user.full_name}\nВам нужно прислать мне свой токен \nчтобы я смог отправлять вам сообщения",
    )
    # await state.set_state(StepsForm.GET_user_token)


async def get_token_handler(message: types.Message):
    url = "https://project-factory-api.vercel.app/api/v1/add-telegram-id/"
    data = {"telegram_id": message.from_user.id, "telegram_token": message.text}
    print(message.text)
    response = requests.patch(url, data)
    print(response.status_code)
    print(response.json())

    await message.reply(
        f"Спасибо я получил ваш токен теперь я могу пересылать вам ваши сообщения",
    )