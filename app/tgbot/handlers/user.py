import logging
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from app.infrastructure.lexicon.lexicon_ru import LEXICON_RU

logger = logging.getLogger(__name__)

router = Router()

@router.message(Command(commands=['start']))
async def start_bot(message: Message, super):
    logger.warning('Log with warning')
    await message.answer(text=LEXICON_RU['/start'].format(name=super))

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])