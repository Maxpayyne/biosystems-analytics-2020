#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-03-12
Purpose: Maxpayyne is Programming
"""

import argparse
import os
import io

# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str', type=str,
                        help='DNA/RNA sequence', default=None)

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True
    )
    parser.add_argument('-o',
                        '--output',
                        help='Output filename', type=str,
                        metavar='FILE', default='out.txt')

    args = parser.parse_args()

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq
    out_fh = open(args.output, 'wt')
    gen_code = {line[0:3].upper(): line[4].upper() for line in args.codons}

    k = 3
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
        result = gen_code.get(codon.upper(), '-')
        out_fh.write(result.rstrip())
    print(f'Output written to \"{args.output}\".')

    file=open(args.outfile, 'wt')



# --------------------------------------------------
if __name__ == '__main__':
    main()
