import argparse
import sys
from methods.hot_deck import hot_deck

parser = argparse.ArgumentParser(description='Imputation methods')

parser.add_argument('-m', '--method',
                    type=str,
                    help='The imputation method to use', choices=['hot-deck'], required=True)

parser.add_argument('-f', '--filename',
                    type=str,
                    help='The filename on which the operation will be performed', required=True)

args = parser.parse_args()
method = args.method

if method == 'hot-deck':
    hot_deck(args.filename)
else:
    print('Method not found.')
    sys.exit()
