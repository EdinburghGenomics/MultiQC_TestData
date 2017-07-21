#!/usr/bin/env python3

import unittest
import sys, os, re, math

# This line allows the tests to run if you just naively run this script.
# But the preferred way is to use run_tests.sh
sys.path.insert(0,'../MultiQC')

from multiqc.modules.bcl2fastq.bcl2fastq import MultiqcModule
from multiqc.modules.base_module import report

def slurp_file(fname):
    with open(os.path.dirname(__file__) + '/../data/modules/bcl2fastq/' + fname) as fh:
        return fh.read()

# Load the file of interest first
json1 = slurp_file('v2.18.0.12/Small_Stats/Stats.json')

class T(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

        report.files['bcl2fastq'] = []

    def test_rep1(self):
        """Test that Small_Stats/Stats.json parses as expected
        """
        mqm = MultiqcModule()

        f = dict( f = json1,
                  root = 'root',
                  fn = 'Stats.json' )
        mqm.parse_file_as_json( f )

        self.assertEqual(list(mqm.bcl2fastq_data.keys()), ['170303_ST-E00266_0192_BHGYKCALXX'])

if __name__ == '__main__':
    unittest.main()
