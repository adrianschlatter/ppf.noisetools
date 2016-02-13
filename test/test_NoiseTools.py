# -*- coding: utf-8 -*-
"""
Unit tests for NoiseTools

@author: Adrian Schlatter
"""

import sys
sys.path.append('..')
import unittest
import NoiseTools as nt
import numpy as np


class TestNoiseTools(unittest.TestCase):

    def test_crop2power2(self):
        x = np.arange(3)
        self.assertTrue(np.all(nt.crop2power2(x) == np.array([0, 1])))

    def test_centercrop2power2(self):
        x = np.arange(6)
        self.assertTrue(np.all(nt.centercrop2power2(x) == x[1:-1]))
        x = np.arange(5)
        self.assertTrue(np.all(nt.centercrop2power2(x) == x[0:-1]))


if __name__ == '__main__':
    unittest.main()
