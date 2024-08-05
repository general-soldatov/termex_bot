from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from dotenv import load_dotenv
from os import getenv
from base import user_un, user_var, user_study, user_sheet
from tasks import task_user

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command(commands=['start']))
async def start_bot(message: Message):
    await message.answer('Hello, i`m bot')


if __name__ == '__main__':
    dp.run_polling(bot)
