#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-04-19
Purpose: Maxpayyne is Programming
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Classify a given string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        type=str,
                        metavar='str',
                        help='Some text')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """The Core of the Program"""

    args = get_args()

    if args.text.isupper():
        print(args.text+' is uppercase.')
    elif args.text.islower():
        print(args.text+' is lowercase.')
    elif args.text.istitle():
        print(args.text+' is title case.')
    elif args.text.isnumeric():
        print(args.text+' is a digit.')
    elif args.text.isspace():
        print('input is space.')
    else:
        print(args.text+' is unclassified.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
