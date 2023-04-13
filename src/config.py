import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME = "flask celey tdd"
    API_V1_STR = "/v1"


settings = Settings()
