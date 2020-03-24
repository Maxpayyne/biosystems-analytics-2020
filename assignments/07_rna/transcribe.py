#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-03-19
Purpose: Maxpayyne is Programming
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Argparse: Getting command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Transcribing DNA into RNA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "File",
        help="Input file(s)",
        metavar="FILE",
        nargs="+",
        type=argparse.FileType("r"),
    )
    parser.add_argument(
        "-o",
        "--outdir",
        help="Output directory",
        type=str,  # argparse.FileType('wt'),
        metavar="DIR",
        default="out",
    )

    args = parser.parse_args()

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The core of the Program"""

    args = get_args()
    out_dir = args.outdir

    num_files, tot_lin = 0, 0
    for f_h in args.File:
        num_files += 1
        out_file = os.path.join(out_dir, os.path.basename(f_h.name))
        out_f_h = open(out_file, "wt")
        lines, num_lines = [], 0
        for line in f_h:
            num_lines += 1
            lines.append(line.strip().replace("T", "U"))
        tot_lin += num_lines
        line_s = "\n".join(lines)  # or print(line, file=out_f_h)
        out_f_h.write(line_s)
        out_f_h.close()
    sequence = "sequence" if num_lines == 1 else "sequences"
    files = "file" if num_files == 1 else "files"

    print(
        f'Done, wrote {tot_lin} {sequence} in {num_files} {files} to directory "{args.outdir}".'
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
