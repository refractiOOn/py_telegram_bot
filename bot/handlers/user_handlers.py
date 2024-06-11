from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.markdown import hbold


user_router = Router()


@user_router.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(f'Hello, {hbold('world')}!')