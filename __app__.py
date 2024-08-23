import logging
import yaml
from aiogram import Dispatcher

from app.infrastructure import Config, load_config
from app.tgbot.handlers import user

logger = logging.getLogger(__name__)

async def register_handlers(dp: Dispatcher):
    config: Config = load_config()
    # Конфигурируем логирование
    with open('app/infrastructure/config_data/log_config.yaml') as logfile:
        configure = yaml.safe_load(logfile.read())
    logging.config.dictConfig(configure)
    logger.info('Starting bot')

    # Инициализируем объект хранилища (project!)

    # Создаём переменные окружения aiogram
    dp.workflow_data.update({'token': 'Super token', 'admin': config.tg_bot.admin_ids, 'super': 'Hello'})

    # Регистриуем роутеры
    logger.info('Initialize routers')
    dp.include_router(user.router)

    # Регистрируем миддлвари
    logger.info('Initialize middlewarez')
    # ...

    # Настраиваем главное меню бота
    # await set_main_menu(bot)