from aiogram import Bot, Dispatcher
from handlers import (
    start_handler,
    get_token_handler
)
from dotenv import load_dotenv
import os
import asyncio

from aiogram.filters import Command



async def main() -> None:
    load_dotenv()
    bot = Bot(os.getenv("TOKEN"))
    dp = Dispatcher()

    dp.message.register(start_handler, Command(commands=["start", "run"]))
    dp.message.register(get_token_handler)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
