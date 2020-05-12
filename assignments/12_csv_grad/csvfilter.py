#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-05-04
Purpose: Maxpayyne is Programming
"""

import argparse
import sys
import re
import csv


# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('r'),
                        help='Input file',
                        default=None, )

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        required=True,
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        type=str,
                        metavar='delim',
                        help='Input delimiter',
                        default=',')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """The Core of the Program"""

    args = get_args()
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if args.col not in reader.fieldnames and args.col != '':
        print(f'--col "{args.col}" not a valid column!\nChoose from '
              f'{", ".join(reader.fieldnames)}', file=sys.stderr)
        sys.exit(1)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    if args.val and args.col:
        num_written = 0
        for rec in reader:
            if re.search(args.val, rec.get(args.col), re.I):
                num_written += 1
                writer.writerow(rec)
    else:
        num_written = 0
        for rec in reader:
            if re.search(args.val, str(rec.values()), re.I):
                num_written += 1
                writer.writerow(rec)

    print(f'Done, wrote {num_written} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
