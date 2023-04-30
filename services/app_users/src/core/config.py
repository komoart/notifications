import os
from logging import config as logging_config

from pydantic import BaseSettings

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'Тестовый сервис пользовательских данных')
    PROJECT_DESCRIPTION: str = os.getenv('PROJECT_DESCRIPTION',
                                         'Тестовый сервис предоставляет информацию о пользователях')
    API_VERSION: str = '1.0.0'

    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Адрес API, принимающего события для отправки уведомлений
    NOTIFICATION_API_REGISTRATION_EVENT_URL: str = os.getenv('NOTIFICATION_API_REGISTRATION_EVENT_URL')


config = Settings()
