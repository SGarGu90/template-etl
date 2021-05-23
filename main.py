from src.FileManager.FileManager import FileManager
import sys

from argparse import ArgumentParser

from src.Logger.Logger import *
from src.orchestrator import *
from src.EnvLoader.EnvLoader import *

def main(args):
    """Capture logs and environment values
    """

    config = EnvLoader(args.environment)

    # Creating the Logger Object
    logger = LoggerClass(log_path = config.log_path,
                            logging_level = config.log_level,
                            log_identifier = config.log_identifier)
    # Init the logger and first message
    logger.init_logger()
    # Print arguments using log
    logger.log.info(f'Arguments: {args}')

    try:

        data_file = FileManager(
            dir_path = config.file_manager_path,
            filename = config.file_manager_filename,
            write_op = config.file_manager_write_op,
            read_op = config.file_manager_read_op,
            logger = logger
        )

        data_file.write_file("Example write file\n")
        read_file_result = data_file.read_file()
        print(f'Example reading written file {read_file_result}')

        orchestrator(config, logger)
    except Exception as err:
        logger.log_traceback(err)


if __name__ == '__main__':

    try:
        """Capture input arguments
        """
        parser = ArgumentParser(description="ETL arguments parser")

        parser.add_argument('--environment', '-env', type=str, choices=['dev', 'prod'], default='dev', help=': Choose environment execution config')
        app_args = parser.parse_args()
        main(app_args)

    except Exception as err:
        print("\n Main function Error: ", sys.exc_info()[0], err)
        sys.exit(-1)
