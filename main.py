import sys, logging

from argparse import ArgumentParser

from src.settings import settings_loader
from src.Logger.Logger import LoggerClass
from src.orchestrator import *

def main(args):
    """Capture logs and environment values
    """

    # Creating the Logger Object
    logger = LoggerClass(log_path="logs/",
                             logging_level=logging.DEBUG,
                             log_identifier="Main ETL logger")

    # Init the logger and first message
    logger.init_logger()
    logger.first_log()

    settings = settings_loader(args.app_env)

    orchestrator(args, settings)


if __name__ == '__main__':

    try:
        """Capture input arguments
        """
        parser = ArgumentParser(description="ETL arguments parser")

        parser.add_argument('--environment', '-env', type=str, choices=['dev', 'prod'], default='dev', help=': Choose environment execution config')

        app_args = parser.parse_args()

        main(app_args)

    except Exception as err:
        print("\n Main function Error :", sys.exc_info()[0])
        sys.exit(-1)
