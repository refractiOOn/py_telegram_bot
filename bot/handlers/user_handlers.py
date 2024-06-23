from aiogram import Router, types
from aiogram.filters import Command
from bot.config import BotConfig


user_router = Router()


@user_router.message(Command('start'))
async def cmd_start(msg: types.Message, config: BotConfig) -> None:
    ''' Process the "start" command '''

    await msg.answer(config.welcome_message)


@user_router.message(Command('admin_info'))
async def cmd_admin_info(msg: types.Message, config: BotConfig) -> None:
    if msg.from_user.id in config.admin_ids:
        await msg.answer('You are an admin.')
    else:
        await msg.answer('You are not an admin.')


@user_router.message(Command('dice'))
async def cmd_dice(msg: types.Message, config: BotConfig) -> None:
    await msg.answer_dice(emoji='🎲')


@user_router.message(Command('reply'))
async def cmd_reply(msg: types.Message, config: BotConfig) -> None:
    await msg.reply('Reply message replies') 