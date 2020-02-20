#!/usr/bin/env python3
"""
Author : Maxpayyne
Date   : 2020-02-15
Purpose: What I do on different week days
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="What to do on each day",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("day", metavar="str", nargs="+", help="Days of the week")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The place where the printing works"""

    args = get_args()
    day = args.day
    week_day = {
        "Monday": "On Mondays I never go to work",
        "Tuesday": "On Tuesdays I stay at home",
        "Wednesday": "On Wednesdays I never feel inclined",
        "Thursday": "On Thursdays, it's a holiday",
        "Friday": "And Fridays I detest",
        "Saturday": "Oh, it's much too late on a Saturday",
        "Sunday": "And Sunday is the day of rest",
    }

    for word in day: print(week_day.get(word, f'Can\'t find "{word}"'))


# --------------------------------------------------
if __name__ == "__main__":
    main()
