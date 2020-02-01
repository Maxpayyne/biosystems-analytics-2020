#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-01-30
Purpose: Maxwell's First Assignment
"""

import argparse



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find position of vowel in string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel',
                        metavar='vowel',
                        help='A vowel to look for',
                        choices=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    parser.add_argument('text',
                        metavar='text',
                        help='The text to search')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Determine if there is a vowel in the text"""

    args = get_args()
    vowel = args.vowel
    text = args.text
    if vowel[0] in text:
        index = text.index(vowel)
        print(f'Found "{vowel}" in "{text}" at index {index}.')
    else:
        print(f'"{vowel}" is not found in "{text}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
