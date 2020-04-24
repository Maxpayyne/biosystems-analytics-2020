#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-04-21
Purpose: To find ORFs in a given sequence
"""

import argparse
import os
import sys
from Bio import SeqIO
import itertools



# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Finding the Open Reading Frames (ORFs)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='Input nucleotide sequence or file')

    parser.add_argument('-s',
                        '--start',
                        help='CODON to start reading',
                        metavar='str',
                        type=str,
                        default='AUG')

    parser.add_argument('-m',
                        '--minlength',
                        help='The minimum length of an ORF',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='sys.stdout',
                        )

    args = parser.parse_args()

    if os.path.isfile(args.sequence):
        args.sequence = open(args.sequence).read().rstrip()
    if args.minlength < 20:
        parser.error(f'--minlength "{args.minlength}" must be greater than 20.')

    return args


# --------------------------------------------------
def main():
    """The Core of the Program"""

    args = get_args()
    seq = args.sequence.replace('T', 'U')

    cod__table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UTA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
        'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W',
    }


    k = 3
    proteins = []
    for codon in [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
        proteins.append((cod__table.get(codon, '?')))
    protein = ''.join(proteins)

    orf = ''
    for amino in protein[protein.index("M"):protein.index("_")]:
        orf += amino
    if len(orf) >= 20:
        print(f'>ORF 1\n{orf}')
        print(f'Found 1 ORFs with {len(orf)} amino acids')


#
# # --------------------------------------------------
# def test_rna():
#     """Test conversion of DNA to RNA"""
#
#     # assert




# --------------------------------------------------
if __name__ == '__main__':
    main()
