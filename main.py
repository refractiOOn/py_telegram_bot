import asyncio

from aiogram import Dispatcher
from aiogram.utils.markdown import hbold
from bot_instance import bot
from bot.handlers.user_handlers import user_router
from bot.config import BotConfig


def register_routers(dp: Dispatcher) -> None:
    """ Registering routers """

    dp.include_router(user_router)


async def main() -> None:
    """ Entry point """
    
    config = BotConfig(
        admin_ids=[6589588177],
        welcome_message=f'Welcome to out {hbold('Bot')}!'
    )
    dispatcher = Dispatcher()
    dispatcher['config'] = config

    register_routers(dispatcher)

    print('Starting...')
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())