#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-10
Purpose: Favorite things Assignment
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='My Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('thing', metavar='str', nargs='+', help='Some things')
    parser.add_argument('-s',
                        '--sep',
                        help='A Separator',
                        metavar='str',
                        type=str,
                        default=', ')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Where the Printing Works"""

    args = get_args()
    thing = args.thing

    if len(thing) == 1:
        print(thing[0])
        print('This is one of my favorite things.')
    else:
        print(args.sep.join(thing))
        print('These are a few of my favorite things.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
