#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-28
Purpose: Hamming Assignment
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)


    parser.add_argument('-m',
                        '--min',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default='0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    min = args.min

    for line in args.file:
        word1, word = line.split()
        line_no = abs(len(word1) - len(word))
        char = list(zip(word1, word))
        dist = 0
        for w1, w2 in char:
                if w1 != w2: dist += 1
        tot_num = line_no + dist

        if tot_num >= min:
            print(f'{tot_num:8}:{word1:20}{word:20}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
