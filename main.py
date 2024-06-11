import asyncio

from aiogram import Dispatcher
from bot_instance import bot


dp = Dispatcher()


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())