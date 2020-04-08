#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-04-08
Purpose: Maxpayyne is Programming
"""

import argparse
import os
import random
from Bio import SeqIO



# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probabalistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        default='',
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        help='Random seed value',
                        default=None,)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')
    args = parser.parse_args()

    if not 0 <= args.pct <= 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
    # if os.path.isfile(args.text):
    #     args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """The Core of the Program"""

    args = get_args()
    random.seed(args.seed)

    for i, fh in enumerate(args.text, start=1):
        basename = os.path.basename(fh.name)
        out_file = os.path.join(args.outdir, basename)
        print(f'{i:3}: {fh.name}')

        out_fh = open(out_file, 'wt')
        for rec in SeqIO.parse(fh, 'fasta'):
            if random.random() == args.pct:
                SeqIO.write(rec, out_fh, 'fasta')
                # print(rec)

        out_fh.close()
    print(f'Wrote {len(rec)} sequence{"" if len(rec) == 1 else "s"} '
          f'from {i} file{"" if i == 1 else "s"} to '
          f'directory "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
