from utils import check_instance, check_integer
from matplotlib import pyplot as plt
import numpy as np
import math


class Sample(object):

    def __init__(self, data):
        check_instance(data, list, 'data should be a list of numbers')

        self._data = data

    @property
    def data(self):
        return self._data

    @property
    def size(self):
        return len(self._data)

    def hist(self, bins=10, density=True, **kwargs):
        return np.histogram(self._data, bins, density=density, **kwargs)

    def draw_hist(self, bins=10, normed=True, **kwargs):
        plt.hist(self._data, bins, normed=normed, **kwargs)

    @staticmethod
    def calc_math_expect(sequence):
        return 1.0 * sum(sequence) / len(sequence)

    @property
    def math_expect(self):
        return Sample.calc_math_expect(self._data)

    @staticmethod
    def calc_dispersion(sequence):
        m = Sample.calc_math_expect(sequence)
        return 1.0 * sum([(x - m)**2 for x in sequence]) / (len(sequence) - 1)

    @property
    def dispersion(self):
        return Sample.calc_dispersion(self._data)

    @staticmethod
    def calc_correlation(sequence1, sequence2):
        if len(sequence1) != len(sequence2):
            raise ValueError('both sequences should be of equal size')

        m1 = Sample.calc_math_expect(sequence1)
        m2 = Sample.calc_math_expect(sequence2)
        d1 = Sample.calc_dispersion(sequence1)
        d2 = Sample.calc_dispersion(sequence2)
        m12 = Sample.calc_math_expect([sequence1[i] * sequence2[i] for i in xrange(len(sequence1))])
        return (m12 - m1 * m2) / math.sqrt(d1 * d2)

    def correlation(self, other_sample):
        check_instance(other_sample, Sample, 'other_sample an instance of Sample')

        return Sample.calc_correlation(self._data, other_sample.data)

    def inner_correlation(self, step):
        check_integer(step, 'step should be integer')
        n = len(self._data)
        if not 0 < step < n:
            raise ValueError('step should be in range ({0}; {1})'.format(0, n))

        return Sample.calc_correlation(self._data[:-step], self._data[step:])
