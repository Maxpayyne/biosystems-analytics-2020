#!/usr/bin/env python3
"""Tests for orf_finder.py"""

import argparse
import os
import sys
import re
import string
from subprocess import getstatusoutput

prg = './orf_finder.py'

# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput( '{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)

# --------------------------------------------------
def test_exists():
    """exists"""

# --------------------------------------------------