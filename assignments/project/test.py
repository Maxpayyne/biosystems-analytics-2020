#!/usr/bin/env python3
"""Tests for orf_finder.py"""

import os
import re
import random
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
def test_positional_argument():
    """A test"""

    rv, out = getstatusoutput(f'{prg}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search('the following arguments are required: DNA/RNA sequence', out)


# --------------------------------------------------
def test_empty_file():
    """A test"""

    rv, out = getstatusoutput('{} {}'.format(prg, input0))
    assert rv == 0
    assert out.rstrip() == 'There is no sequence here.'


# --------------------------------------------------
def test_bad_minlength():
    """die on bad minimum orf length"""

    bad = random.randint(1, 19)
    rv, out = getstatusoutput(f'{prg} -m {bad} {input1}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f'--minlength "{bad}" must be greater than 20', out)


# --------------------------------------------------

def test_good_input():
    """A test"""

    out_file = 'out.fa'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv, out = getstatusoutput('{} {}'.format(prg, input1))
        assert rv == 0
        expected = '\n'.join([
            'From this amino acid sequence', '',
            'NFCAKPESMVASLNDGCCNAPSSSLRSVHANPGRGSAACRARSAR_QASVRSVGAEVSAQDSRVDRAVRSRHPRGPGCSTGSLHQGLPCAWQFPRRQCV?YLAVPHRHQHGEELPGVPWKTAARQRCQLRGCGV?RRRSWPQGSRVPRALVVAG_NRRMCPSHHPATAQRPTHGLDPA_VRRAE?RRHCQCHAMSGGYRALSNLPRSGGHRQSPATFAAGN_',
            '', 'I found 2 ORFs, written to "out.fa".'
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
