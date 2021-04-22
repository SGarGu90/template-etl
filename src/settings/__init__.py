from .common import *
from src.settings import settings_prod, settings_dev


def settings_loader(environment):
    if environment == "dev":
        print(f'DEVELOPMENT ENVIRONMENT {APP_VERSION}')

        return settings_dev

    elif environment == "prod":
        print(f'PRODUCTION ENVIRONMENT {APP_VERSION}')

        return settings_prod
