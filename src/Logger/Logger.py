import logging
import datetime
import sys

class LoggerClass:
    file_date_format = '%Y%m%d'
    print_date_format = '%Y-%m-%d %H:%M:%S'

    def __init__(self, log_path, logging_level, log_identifier):
        """Accept required parameters for logger instantiation

        Args:
            log_path (str): logger storage directory
            logging_level (str): type of error
            log_identifier (str): universal unique identifier
        """
        self.log_path = log_path
        self.logging_level = logging_level
        self.log_identifier = log_identifier
        self.logger = None

    def init_logger(self):
        """Initialize logger with two handlers, one for wrinte and save logs on disk and other for print out beauty on console
        """
        try:
            # Defining log level
            logger = logging.getLogger(self.log_identifier)
            logger.setLevel(self.logging_level)

            # File handler on Disk
            file_handler = logging.FileHandler(self.log_path +
                                               datetime.date.today().strftime(self.file_date_format) +
                                               '_' + self.log_identifier +
                                               '_ETL.log', mode='w')

            file_handler.setLevel(self.logging_level)

            # Console Handler
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.setLevel(self.logging_level)

            # Create formatter and addit to the handlers
            # formatter_0 = logging.Formatter('[%(asctime)s] || %(levelname)s || \
            #                                 (%(filename)s:%(lineno)s || \
            #                                 %(message)s', datefmt=self.print_date_format)
            formatter_1 = logging.Formatter('%(levelname)s [%(asctime)s] \n ├── %(filename)s:%(lineno)s \n └── %(message)s', datefmt=self.print_date_format)
            formatter_2 = logging.Formatter('%(levelname)s [%(asctime)s] %(filename)s:%(lineno)s \n └── %(message)s \n', datefmt=self.print_date_format)
            file_handler.setFormatter(formatter_2)
            console_handler.setFormatter(formatter_2)

            # Add the handlers to the logger
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)
            self.logger = logger

        except Exception as err:
            self.logger.log(logging.ERROR, "\n Init Logger Error ({0})".format(err))
            sys.exit(-1)

    def first_log(self):
        try:
            self.logger.info("*********** Start Execution ************* \n")
            self.logger.info("Execution Start")
            self.logger.info("Type of file to be processed: %s")

        except Exception as err:
            self.logger.log(logging.ERROR, "\n First_log Error ({})".format(err))
            sys.exit(-1)
