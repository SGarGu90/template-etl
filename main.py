import sys, logging

from argparse import ArgumentParser

from src.settings import settings_loader
from src.Logger.Logger import *
from src.orchestrator import *
from src.env_config.config import *

def main(args):
    """Capture logs and environment values
    """

    config = LoadEnvironmentClass()

    print(config.log_path)
    print(config.log_level)
    print(config.log_identifier)

    # Creating the Logger Object
    logger = LoggerClass(log_path=config.log_path,
                            logging_level=config.log_level,
                            log_identifier=config.log_identifier)

    # Init the logger and first message
    logger.init_logger()
    # First default log
    logger.first_log()

    orchestrator(args)


if __name__ == '__main__':

    try:
        """Capture input arguments
        """
        parser = ArgumentParser(description="ETL arguments parser")

        parser.add_argument('--environment', '-env', type=str, choices=['dev', 'prod'], default='dev', help=': Choose environment execution config')
        parser.add_argument('--logs-dir', '-ldir', type=str, default='logs/', help=': Choose logs output directory, default (logs/)')
        parser.add_argument('--logs-identifier', '-lid', type=str, default='Main ETL logger', help=': Choose logger identifier name, default (Main ETL logger)')
        app_args = parser.parse_args()
        main(app_args)

    except Exception as err:
        print("\n Main function Error: ", sys.exc_info()[0])
        sys.exit(-1)
