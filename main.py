import logging
import logging.config
import yaml

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv
from os import getenv
from sys import stdout

from oath_user.profile import prod
from oath_user.reg import research

from database import user_un, user_var, user_study, user_sheet
from tasks import task_user

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

with open('config/log_config.yaml') as logfile:
    config = yaml.safe_load(logfile.read())

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)
logger.info('Bot is starting')

@dp.message(Command(commands=['start']))
async def start_bot(message: Message):
    logger.warning('Log with warning')
    await message.answer('Hello, i`m bot')


if __name__ == '__main__':
    dp.run_polling(bot)
