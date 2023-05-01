from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    authjwt_secret_key: str = Field("qwerty", env='SECRET_KEY')
    NOTIFICATION_API_REGISTRATION_EVENT_URL: str = Field(..., env='NOTIFICATION_API_REGISTRATION_EVENT_URL')


settings = Settings()
