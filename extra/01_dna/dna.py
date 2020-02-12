#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-12
Purpose: Nucleotide Counting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Count DNA nucleotides',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        help='DNA')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    string = args.string

    first = string.count('A') + string.count('a')
    second = string.count('C') + string.count('c')
    third = string.count('G') + string.count('g')
    fourth = string.count('T') + string.count('t')

    print(f'{first} {second} {third} {fourth}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
