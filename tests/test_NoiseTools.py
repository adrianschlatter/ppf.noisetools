# -*- coding: utf-8 -*-
"""
Unit tests for NoiseTools

@author: Adrian Schlatter
"""

import unittest
import ppf.NoiseTools as nt
import numpy as np


class TestHelpers(unittest.TestCase):

    def test_crop2power2(self):
        x = np.arange(3)
        self.assertTrue(np.all(nt.crop2power2(x) == np.array([0, 1])))

    def test_centercrop2power2(self):
        x = np.arange(6)
        self.assertTrue(np.all(nt.centercrop2power2(x) == x[1:-1]))
        x = np.arange(5)
        self.assertTrue(np.all(nt.centercrop2power2(x) == x[0:-1]))


class TestSpectralTools(unittest.TestCase):

    def setUp(self):
        phi = np.arange(16.) / 16. * 2 * np.pi
        self.sig = np.cos(phi)
        self.spec = nt.spectrum(self.sig)
        self.sig_prime = nt.ispectrum(self.spec)
        self.pspec = nt.powerspectrum(self.sig)

    def test_spectrum(self):
        expected = np.zeros(16, dtype='float')
        expected[[1, -1]] = 0.5
        delta = self.spec - expected
        self.assertAlmostEqual(np.sum(delta**2), 0)

    def test_ispectrum(self):
        delta = self.sig_prime - self.sig
        self.assertAlmostEqual(np.sum(delta**2), 0)

    def test_powerspectrum(self):
        expected = np.abs(self.spec[:len(self.spec) // 2])**2
        delta = self.pspec - expected
        self.assertAlmostEqual(np.sum(delta**2), 0)


class TestADCNoise(unittest.TestCase):

    def test_ADCSNR(self):
        noise10bit = 10**(0.1 * nt.ADC_SNR(10))
        noise12bit = 10**(0.1 * nt.ADC_SNR(12))
        self.assertAlmostEqual(16 * noise10bit / noise12bit, 1)

    def test_ADC_NoiseFloor(self):
        noise100kHz = nt.ADC_NoiseFloor(10, 100e3)
        noise1MHz = nt.ADC_NoiseFloor(10, 1e6)
        self.assertAlmostEqual(noise100kHz - noise1MHz, 10)


if __name__ == '__main__':
    unittest.main()
