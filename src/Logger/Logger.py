import logging, traceback
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
            logger.setLevel(logging.DEBUG)

            # File handler on Disk
            file_handler = logging.FileHandler(self.log_path +
                                               datetime.date.today().strftime(self.file_date_format) +
                                               '_' + self.log_identifier +
                                               '_ETL.log', mode='w')

            file_handler.setLevel(logging.DEBUG)

            # Console Handler
            console_handler = logging.StreamHandler(stream=sys.stdout)
            console_handler.setLevel(logging.DEBUG)

            # Create formatter and addit to the handlers
            # formatter_0 = logging.Formatter('[%(asctime)s] || %(levelname)s || \
            #                                 (%(filename)s:%(lineno)s || \
            #                                 %(message)s', datefmt=self.print_date_format)
            # formatter_1 = logging.Formatter('%(levelname)s [%(asctime)s] \n ├── %(filename)s:%(lineno)s \n └── %(message)s', datefmt=self.print_date_format)
            formatter_2 = logging.Formatter('%(levelname)s [%(asctime)s] %(filename)s:%(lineno)s \n %(message)s \n', datefmt=self.print_date_format)
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

    def log_traceback(self, logging_type):
        # Extract error traceback info
        formatted_lines = traceback.format_exc().splitlines()
        # Clean traceback lines from empty spaces
        formatted_lines = [line.strip() for line in formatted_lines]

        # Split each error line into small parts (file, line, element) to create custom message format
        MOST_RECENT_CALL_FILE = 1
        LAST_CALL_FILE = 3
        most_recent_call_parts = formatted_lines[MOST_RECENT_CALL_FILE].split(",")
        last_call_parts = formatted_lines[LAST_CALL_FILE].split(",")

        # Define custom traceback message format
        FILE = 0
        LINE = 1
        ELEMENT = 2
        most_recent_call_location = "{}:{}\" {}".format(most_recent_call_parts[FILE][:-1], most_recent_call_parts[LINE][6:], most_recent_call_parts[ELEMENT])
        last_call_location = "{}:{}\" {}".format(last_call_parts[FILE][:-1], last_call_parts[LINE][6:], last_call_parts[ELEMENT])

        # Make custom message format looks beauty
        MOST_RECENT_CALL_FN = 2
        LAST_CALL_FN= 4
        traceback_message = "" + \
        "├── " + formatted_lines[MOST_RECENT_CALL_FN] + "\n" \
        " │   └── " + most_recent_call_location + "\n" \
        " └── " + formatted_lines[LAST_CALL_FN] + "\n" \
        "     └── " + last_call_location + "\n"

        # Print message based on type passed
        self.logger.log(logging_type, traceback_message)
