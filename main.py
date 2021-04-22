import sys, logging

from argparse import ArgumentParser

from src.settings import settings_loader
from src.Logger.Logger import LoggerClass

from src.orchestrator import *

def main(args, logger):
    """Capture logs and environment values
    """
    # First default log
    logger.first_log()

    settings = settings_loader(args.environment)

    orchestrator(args, settings)


if __name__ == '__main__':

    try:
        """Capture input arguments
        """
        parser = ArgumentParser(description="ETL arguments parser")

        parser.add_argument('--environment', '-env', type=str, choices=['dev', 'prod'], default='dev', help=': Choose environment execution config')
        parser.add_argument('--logs-dir', '-ldir', type=str, default='logs/', help=': Choose logs output directory, default (logs/)')
        parser.add_argument('--logs-identifier', '-lid', type=str, default='Main ETL logger', help=': Choose logger identifier name, default (Main ETL logger)')

        app_args = parser.parse_args()

        # Creating the Logger Object
        logger = LoggerClass(log_path=app_args.logs_dir,
                                logging_level=logging.DEBUG,
                                log_identifier="Main ETL logger")

        # Init the logger and first message
        logger.init_logger()

        main(app_args, logger)

    except Exception as err:
        logger.log_traceback(logging.WARN)
        sys.exit(-1)
