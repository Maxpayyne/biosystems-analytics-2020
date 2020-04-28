#!/usr/bin/env python3
"""Tests for orf_finder.py"""

import os
import re
from subprocess import getstatusoutput

prg = './orf_finder.py'
input0 = './inputs/input0'
input1 = './inputs/input1'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_0():
    """A test"""

    rv, out = getstatusoutput('{} {}'.format(prg, input0))
    assert rv == 0
    assert out.rstrip() == 'There is no sequence here.'


# --------------------------------------------------
def test_1():
    """A test"""

    out_file = 'out.txt'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv, out = getstatusoutput('{} {}'.format(prg, input1))
        assert rv == 0
        expected = '\n'.join([
            'From this amino acid sequence', '',
            'NFCAKPESMVASLNDGCCNAPSSSLRSVHANPGRGSAACRARSAR_QASVRSVGAEVSAQDSRVDRAVRSRHPRGPGCSTGSLHQGLPCAWQFPRRQCV?YLAVPHRHQHGEELPGVPWKTAARQRCQLRGCGV?RRRSWPQGSRVPRALVVAG_NRRMCPSHHPATAQRPTHGLDPA_VRRAE?RRHCQCHAMSGGYRALSNLPRSGGHRQSPATFAAGN_',
            '', 'I found 2 ORFs, written to out.txt.'
        ])
        assert out.strip() == expected

        assert os.path.isfile(out_file)

        expected_contents = '\n'.join([
            '>ORF 1', 'MVASLNDGCCNAPSSSLRSVHANPGRGSAACRARSAR',
            'Found ORF with 37 amino acids.', '>ORF 2',
            'MSGGYRALSNLPRSGGHRQSPATFAAGN', 'Found ORF with 28 amino acids.'
        ])

        assert open(out_file).read().strip() == expected_contents.strip()
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
