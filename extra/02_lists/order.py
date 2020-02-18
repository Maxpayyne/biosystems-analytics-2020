#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-12
Purpose: Order a List
"""
print('You have failed me for the last time, Commander.')

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Order all the things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        default='You have failed me for the last time, Commander.',
                        help='The things to order')

    parser.add_argument('-r',
                        '--reverse',
                        help='Reverse the sort order',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    #if len(args.string) is 0:
    print('foo')
# --------------------------------------------------
if __name__ == '__main__':
    main()
