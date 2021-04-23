import configparser
import platform
import logging
import sys


import sys, logging, platform, configparser

class LoadEnvironmentClass:
    logger = None

    def __init__(self):

        try:

            self.config = None

            if platform.system() == "Linux":
                print("Running the ETL from Linux System")
                root_dir = "./config"
                config_file = root_dir + "/config.ini"
            else:
                print("Running the ETL from Windows System")
                root_dir = ".\\config"
                config_file = root_dir + "\\config_win.ini"

            # Read config file
            self.config = configparser.ConfigParser()
            self.config.sections()
            self.config.read(config_file)

            # logger configuration
            self.log_path = self.config['LOGGING']['LOG_PATH']
            self.log_level = self.config['LOGGING']['LOG_LEVEL']
            self.log_identifier = self.config['LOGGING']['LOG_IDENTIFIER']

            self.input_file = self.config['FILE_PATH']['INPUT_FILE']


        except Exception as err:
            print("\n Load env function Error ({0})".format(err))
            sys.exit(-1)