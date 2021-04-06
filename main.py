import argparse
import sys
from methods.hot_deck import hot_deck
from methods.interpolate import interpolate
from methods.m_interpolate import m_interpolate


parser = argparse.ArgumentParser(description='Imputation methods')
choices = {'hotdeck':hot_deck, 'interpolate':interpolate, 'minterpolate':m_interpolate}

parser.add_argument('-m', '--method',
                    type=str,
                    help='The imputation method to use', choices= choices.keys(), required=True)

parser.add_argument('-f', '--filename',
                    type=str,
                    help='The filename on which the operation will be performed', required=True)

args = parser.parse_args()
method = args.method

if method in choices:
    choices[method](args.filename)
else:
    print('Method not found.')
    sys.exit()
