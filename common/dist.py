from sample import Sample
from utils import check_instance
from math import fabs
import numpy as np


class DistFunc(object):

    eps = 1e-9

    def __init__(self, sample=None, probabilities=None, values=None):
        if not (sample or (probabilities and values)):
            raise ValueError('provide a sample or manually enter probabilities and values')
        if sample:
            check_instance(sample, Sample, 'sample should be an instance of Sample')

            probabilities = [1.0 / sample.size for _ in xrange(sample.size)]
            values = sorted(sample.data)
        else:
            if fabs(sum(probabilities) - 1) > DistFunc.eps:
                raise ValueError('sum of probabilities should be equal to 1')

        self._sample = sample
        self._probabilities = probabilities
        self._values = values
        self._edges = np.cumsum(self._probabilities).tolist()

    @property
    def sample(self):
        return self._sample

    @property
    def probabilities(self):
        return self._probabilities

    @property
    def values(self):
        return self._values

    @property
    def edges(self):
        return self._edges

    def get_value(self, param):
        if not 0 < param <= 1:
            raise ValueError('param should be within range (0, 1]')

        for i in xrange(0, len(self._edges)):
            if param < self._edges[i] + DistFunc.eps:
                return self._values[i]

        raise RuntimeError('bad things happened :(')

    def draw(self):
        self._sample.draw_hist(self._sample.size, histtype='step', cumulative=True)
