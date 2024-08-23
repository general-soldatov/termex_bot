from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

@dataclass
class DatabaseConfig:
    endpoint: str
    region: str
    aws_id: str
    aws_key_id: str

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    gsheet: str


def load_config():
    load_dotenv()

    return Config(
        tg_bot=TgBot(
            token=getenv('BOT_TOKEN'),
            admin_ids=getenv('ADMIN')
        ),
        db=DatabaseConfig(
            endpoint=getenv('ENDPOINT'),
            region='ru-central1',
            aws_id=getenv('AWS_ACCESS_KEY_ID'),
            aws_key_id=getenv('AWS_SECRET_ACCESS_KEY')
        ),
        gsheet=getenv('GOOGLE_SERVICE_ACCOUNT')
    )