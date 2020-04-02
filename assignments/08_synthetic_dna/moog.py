#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-03-30
Purpose: Maxpayyne is Programming
"""

import argparse
import random


# --------------------------------------------------

def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--outfile', type=argparse.FileType('wt'),
                        metavar='str',
                        help='Output filename', default='out.fa')

    parser.add_argument('-t', '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        choices='dna rna'.split(),
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=0.5)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return parser.parse_args()


# --------------------------------------------------

def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


def main():
    """The Core of the Program"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    outfile = args.outfile

    num = 0
    for _ in pool:
        num += 1
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = "".join(random.sample(pool, seq_len))
        print(f'>{num}\n{seq}', file=outfile)
        if num == args.numseqs:
            break
    print(
        f'Done, wrote {args.numseqs} {args.seqtype.upper()} '
        f'sequences to "{outfile.name}".'
    )


def test_create_pool():
    """" Test create_pool """

    state = random.getstate()

    assert create_pool(.5, 10, 'dna') == 'AAACCCGGTT'
    assert create_pool(.6, 11, 'rna') == 'AACCCCGGGUU'
    assert create_pool(.7, 12, 'dna') == 'ACCCCCGGGGGT'
    assert create_pool(.7, 20, 'rna') == 'AAACCCCCCCGGGGGGGUUU'
    assert create_pool(.4, 15, 'dna') == 'AAAACCCGGGTTTTT'
    random.setstate(state)


# --------------------------------------------------
if __name__ == '__main__':
    main()
