#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-04-21
Purpose: To find ORFs in a given sequence
"""

import argparse
import os
import sys
import re


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
                        default=25)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        # metavar='outfile',
                        type=str,
                        default='',
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

    cod_table = {
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
        proteins.append((cod_table.get(codon, '?')))
    startcod = cod_table.get(args.start)

    prot = ''.join(proteins)
    # orf = find_orf(prot, startcod)

    print(''.join(proteins))
    # if len(orf) >= args.minlength:
    #     print(f'>ORF 1\n{orf}')
    #     print(f'Found 1 ORF with {len(orf)} amino acids')

    print(len(start_points(prot, startcod)))
    print(start_points(prot, startcod)[0])
    print(len(start_points(prot, '_')))
    for ind in start_points(prot, startcod):
        for m in start_points(prot, '_'):
            print(''.join(prot[ind:m]))


# --------------------------------------------------
def find_orf(seq):
    """Finding the ORFs in a sequence"""

    # begin = seq.index(start) if start in seq else -1
    # end = seq.index('_') if '_' in seq else -1
    # return ''.join(seq[begin:end]) if begin < end else ''


# --------------------------------------------------
def test_find_orf():
    assert find_orf('') == ''  # test with nothing
    assert find_orf('_ABCM') == ''  # the _ occurs before the M
    assert find_orf('MABC') == ''  # an M but no _
    assert find_orf('ABC_') == ''  # an _ but no M
    assert find_orf('MABC_') == 'MABC'  # M at the beginning
    assert find_orf('ABMC_') == 'MC'  # M in the middle
    assert find_orf('MCAMAMB_C_DMCAB_') == ['MCAMAMB', 'MAMB', 'MB', 'MCAB']


# --------------------------------------------------
def start_points(seq, start):
    """Get starting points"""
    start_ind = []
    for ind in [m.start() for m in re.finditer(start, seq)]:
        start_ind.append(ind)
    return start_ind

# --------------------------------------------------
def test_start_points():
    assert start_points('', 'A') == []
    assert start_points('ABCABD', 'A') == [0, 3]
    assert start_points('QWERTYQWERTY', 'Q') == [0, 6]
    assert start_points('QWERTYQWERTY', 'G') == []

# --------------------------------------------------


# --------------------------------------------------
if __name__ == '__main__':
    main()
