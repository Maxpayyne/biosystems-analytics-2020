#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-04-10
Purpose: Maxpayyne is Programming
"""

import argparse
import os
import sys
import re
from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file fom CD-HIT (clustered protein)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True,
                        )

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required=True,
                        default=None
                        )

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default="unclustered.fa"
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The Core of the Program"""

    args = get_args()
    num = 0
    for line in args.cdhit:
        num += 1
        match = re.search(r'>(\d+)', line)
        id = match.group(1)
        print(id)
        # if num == 100:
        #     break

    print(f'Wrote {num} of unclustered proteins'
          f' to "{args.outfile.name}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
