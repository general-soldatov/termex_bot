import asyncio
import logging
import yaml

import logging.config

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.infrastructure import Config, load_config
# from keyboards.main.menu

from aiogram.filters import Command
from aiogram.types import Message

from __app__ import register_handlers


# from os import getenv
# from sys import stdout

from app.infrastructure import user_un, user_var, user_study, user_sheet

logger = logging.getLogger(__name__)


async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    await register_handlers(dp)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
