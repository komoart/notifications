import os
from logging import config as logging_config

from pydantic import BaseConfig, Field

from core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)


class Settings(BaseConfig):
    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = Field(..., env='PROJECT_NAME', description='Тестовый сервис пользовательских данных')
    PROJECT_DESCRIPTION: str = Field(..., env='PROJECT_DESCRIPTION',
                                     description='Тестовый сервис предоставляет информацию о пользователях')
    API_VERSION: str = Field('1.0.0')

    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Адрес API, принимающего события для отправки уведомлений
    NOTIFICATION_API_REGISTRATION_EVENT_URL: str = Field(..., env='NOTIFICATION_API_REGISTRATION_EVENT_URL')


settings = Settings()
