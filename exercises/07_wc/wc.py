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
        help="Input file(s)",
        type=argparse.FileType("r"),
        nargs='*',
        default=None,
    )
    parser.add_argument('-n', '--num', metavar='int', help="Number of lines", default=10)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    total_lines, total_words, total_chars = 0, 0, 0

    for fh in args.file:
        num_lines = 0
        num_words = 0      #Or num_lines, num_words, num_char = 0, 0, 0
        num_chars = 0
        for line in fh:
            num_lines += 1
            words = line.split()
            num_words += len(words)
            num_chars += len(line)

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars

        print(f'{num_lines:4} {num_words:4} {num_chars:4} {fh.name}')
    if len(args.file) > 1:
        print(f'{total_lines} {total_words:4} {total_chars:4} total')

# --------------------------------------------------
if __name__ == "__main__":
    main()
