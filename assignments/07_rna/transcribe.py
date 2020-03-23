#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-03-19
Purpose: Maxpayyne is Programming
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('File',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
    )
    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory', type=str,#argparse.FileType('wt'),
                        metavar='DIR', default='out',)

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(outdir)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    base = os.path.basename(args.File)
    out_dir = args.outdir
    os.path.join(out_dir, base)
    num_files = 0
    for fh in args.File:
        num_files += 1
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        num_lines = 0       # base = os.path.basename(fh.name)
        for line in fh:
            num_lines += 1
            line = line.replace('T', 'U').strip()
            #print(f'{num_lines} and {fh.name}')
    if num_lines == 1:
        sequence = 'sequence'
    else:
        sequence = 'sequences'
    if num_files == 1:
        files = 'file'
    else:
        files = 'files'
    # out_file = os.path.join(outdir, os.path.basename(fh.name))
    # out_fh = open(out_file, wt)
    # out_fh.write(line) #or print(line, file=out_fh)
    # out_fh.close()
    # print(os.path.isdir(outdir))
    print(f'Done, wrote {num_lines} {sequence} in {num_files} {files} to directory \"{args.outdir}\".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
