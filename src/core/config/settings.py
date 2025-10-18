from typing import Optional


class BaseConfig:
    DOCS_URL: Optional[str] = '/docs'
    REDOC_URL: Optional[str] = '/redoc'
    DOMAIN_NAME: str = 'http://localhost:8000/'
    ALLOWED_HOSTS: list[str] = ['*']

SETTINGS = BaseConfig()