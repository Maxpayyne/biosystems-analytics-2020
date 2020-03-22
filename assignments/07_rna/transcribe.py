#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-03-19
Purpose: Maxpayyne is Programming
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        default=None)
    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory', type=argparse.FileType('wt'),
                        metavar='DIR', default='out')

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makdirs(outdir)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:



# --------------------------------------------------
if __name__ == '__main__':
    main()
