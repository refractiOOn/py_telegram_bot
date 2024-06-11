import asyncio

from aiogram import Dispatcher
from bot_instance import bot
from bot.handlers.user_handlers import user_router


def register_routers(dp: Dispatcher) -> None:
    dp.include_router(user_router)


async def main() -> None:
    dispatcher = Dispatcher()

    register_routers(dispatcher)

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())