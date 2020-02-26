#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-20
Purpose: Howler Assignment
"""

import argparse
import os
import sys
import io


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
    for line in args.file:
        print(line.readline())

    #for fh in args.file:
        #print(fh.readline().open(args.fiile), end ="") if args.num += 1 else print(f'--num "{args.num}" must be greater than 0')



# --------------------------------------------------
if __name__ == "__main__":
    main()
