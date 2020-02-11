#!/usr/bin/env python3
"""
Author : maxpayyne
Date   : 2020-02-11
Purpose: Rock the Casbah
"""

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items alphabetically'



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    if args.sorted:
        items.sort()

    if len(items) == 1:
        print(f'You are bringing {items[0]}')
    elif len(items) == 2:
        print('You are bringing {}.'format(' and '.join(items)))
    else:
        items[-1] = 'and ' + items[-1]
        print('You are bringing {},' .format(', '.join(items)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
