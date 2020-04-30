#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-04-26
Purpose: Maxpayyne is Programming
"""

import argparse
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("text",
                        metavar="FILE",
                        type=argparse.FileType("r"),
                        default="",
                        help="SwissProt file")

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        nargs='+',
                        type=str,
                        default=None,
                        required=True)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        nargs='*',
                        metavar='taxa',
                        type=str,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The Core of the Program"""

    args = get_args()
    wanted_kw = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))

    num_skipped, num_taken = 0, 0
    for rec in SeqIO.parse(args.text, "swiss"):
        annots = rec.annotations

        taxa = annots.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip_taxa.intersection(taxa):
                num_skipped += 1
                continue

        keywords = annots.get('keywords')
        if keywords:
            keywords = set(map(str.lower, keywords))
            if wanted_kw.intersection(keywords):
                num_taken += 1
                SeqIO.write(rec, args.outfile, 'fasta')
            else:
                num_skipped += 1

    print(f'Done, skipped {num_skipped} and took {num_taken}. See '
          f'output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
