#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-20
Purpose: Howler Assignment
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        help="Input File",
        type=argparse.FileType("r"),
        default=None,
    )
    parser.add_argument('-n', '--num', metavar='int', help="Number of lines", default=10)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        print(fh.readline(), end ="") #if args.num > 0 else print()
        #fh.read


# --------------------------------------------------
if __name__ == "__main__":
    main()
