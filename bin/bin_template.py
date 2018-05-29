#!/usr/bin/env python3
"""
    Purpose:
        Imput the Purpose of the Template Here

    Steps:
        - Step 1
        - Step 2
        - Step 3
        - Step 4

    function call:
        ./bin_template.py --necessary_param {{--optional_param}}

        example call: ./bin_template.py --necessary_param='value'
            {{--optional_param='value_2'}}
"""

# Python Library Imports
import sys
import os
from argparse import ArgumentParser

# Custom Python Library Imports
current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, current_path + '/../')
from config import config
from lib.executor import executor

# Import config and logging details
CONFIGS = config.Config.get()
logging = CONFIGS.get_logging()


@executor
def main(necessary_param, optional_param):
    """
        Create New Migration Record
    """

    logging.info('Starting Script to Do X')

    # Call functions and Libraries Here

    logging.info('Script to Do X Complete')


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument(
        '-n', '--necessary_param', dest='necessary_param', action='store',
        help='Necessary Param to Pass in Command Line', default=None)
    parser.add_argument(
        '-o', '--optional_param', dest='optional_param', action='store',
        help='Optional Param to Pass in Command Line', default=None)
    args = parser.parse_args()

    if not args.necessary_param:
        print(
            './bin_template.py --necessary_param {{--optional_param}}'
        )
        logging.error('Failure to run due to lack of options: {args}'.format(
            args=args))
        sys.exit()

    main(args.necessary_param, args.optional_param)
