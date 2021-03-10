from .common import *
from src.settings import settings_prod, settings_dev


def settings_loader(APP_ENV):
    if APP_ENV == "dev":
        print(f'DEVELOPMENT ENVIRONMENT {APP_VERSION}')

        return settings_dev

    elif APP_ENV == "prod":
        print(f'PRODUCTION ENVIRONMENT {APP_VERSION}')

        return settings_prod
