#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-04-21
Purpose: To find ORFs in a given sequence
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Finding the Open Reading Frames (ORFs)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='DNA/RNA sequence',
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
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='out.txt',
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
    orf = find_orf(prot, startcod)
    # orfs = sort_orf(orf)

    num = 0
    for line in sort_orf(orf):
        if len(line) >= args.minlength:
            num += 1
            print(f'>ORF {num}\n{line}', file=args.outfile)
            print(f'Found ORF with {len(line)} amino acids.', file=args.outfile)

    if args.sequence == '':
        print(f'There is no sequence here.')
    elif not start_points(prot, startcod):
        print(f'There are no start codons.')
    elif not start_points(prot, '_'):
        print(f'There are no stop codons.')
    elif not sort_orf(orf):
        print(f'There is no ORF with a start and a stop codon.')
    else:
        print(f'From this amino acid sequence\n\n{prot}\n\nI found {num} ORF{"s" if num > 1 else ""}, '
              f'written to {args.outfile.name}.')


# --------------------------------------------------
def start_points(seq, start):
    """Get starting points"""
    # for ind in [m.start() for m in re.finditer(start, seq)]:
    # start_ind.append(ind)
    # return [m.start() for m in re.finditer(start, seq)]
    return [t[0] for t in enumerate(seq) if t[1] == start]


# --------------------------------------------------
def test_start_points():
    assert start_points('', 'A') == []
    assert start_points('ABCABD', 'A') == [0, 3]
    assert start_points('QWERTYQWERTY', 'Q') == [0, 6]
    assert start_points('QWERTYQWERTY', 'G') == []


# --------------------------------------------------
def find_orf(seq, startcod):
    """Finding the ORFs in a sequence"""
    starts = start_points(seq, startcod)
    ends = start_points(seq, '_')

    orfs = []
    for start in starts:
        for end in ends:
            if end > start:
                orfs.append(seq[start:end])
    return orfs


# --------------------------------------------------
def test_find_orf():
    assert find_orf('', '') == []  # test with nothing
    assert find_orf('_ABCM', 'M') == []  # the _ occurs before the M
    assert find_orf('MABC', 'M') == []  # an M but no _
    assert find_orf('ABC_', 'M') == []  # an _ but no M


# --------------------------------------------------
def sort_orf(orf_sequences):
    """Finding the ORFs in a sequence"""
    # line = []
    # for _ in orf_sequences:
    #     if '_' not in _:
    #         line.append(_)
    # return line

    return [line for line in orf_sequences if '_' not in line]


# --------------------------------------------------
def test_sort_orf():
    assert sort_orf(['MABC', 'MAFG', 'MAF_G', 'MAGE']) == ['MABC', 'MAFG', 'MAGE']
    assert sort_orf(['MABC_', 'MA_BC']) == []
    assert sort_orf(['MCAMAMB', 'MC_AB']) == ['MCAMAMB']


# --------------------------------------------------
if __name__ == '__main__':
    main()
