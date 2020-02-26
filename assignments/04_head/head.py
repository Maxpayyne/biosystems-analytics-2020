#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-20
Purpose: Howler Assignment
"""

import argparse

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

    parser.add_argument(
        "-n", "--num", metavar="int", type=int, help="Number of lines", default=10
    )
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num_lines = 0
    for line in args.file:
        num_lines += 1
        print(line, end="")
        if num_lines == args.num:
            break


# --------------------------------------------------
if __name__ == "__main__":
    main()
