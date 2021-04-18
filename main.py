import sys

from argparse import ArgumentParser
from src.settings import settings_loader
from src.orchestrator import *

def main(args):
    """Capture logs and environment values
    """

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
