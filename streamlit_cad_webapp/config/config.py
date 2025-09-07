from environs import Env
from pydantic_settings import BaseSettings

env = Env()
env.read_env()


class Settings(BaseSettings):
    app_name: str = "CAD WebApp"
    api_endpoint_binary: str = "https://cad.eucalytics.uk/cv/v1/predict/binary"
    api_endpoint_url: str = "https://cad.eucalytics.uk/cv/v1/predict/url"
    api_key: str = env.str("API_KEY")


settings = Settings()
