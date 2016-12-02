from utils import check_instance
from rand import BaseRandom
from matplotlib import pyplot as plt


class RandomAnalyzer(object):

    def __init__(self, rand):
        check_instance(rand, BaseRandom, 'rand should be an instance of BaseRandom')

        self._rand = rand

    @property
    def rand(self):
        return self._rand

    def analyze_uniformity(self, requests):
        stats = [[], []]
        for size in requests:
            sample = self._rand.sample(size)
            stats[0].append(sample.math_expect)
            stats[1].append(sample.dispersion)
        return stats

    def analyze_dependency(self, size, steps):
        sample = self._rand.sample(size)
        stats = []
        for step in steps:
            stats.append(sample.inner_correlation(step))
        return stats

    def plot_analysis(self, requests, size, steps, math_expect=1.0/2, dispersion=1.0/12):
        tmp = self.analyze_uniformity(requests)
        plt.subplot(3, 1, 1)
        plt.plot(requests, tmp[0], 'r')
        plt.axhline(math_expect)
        plt.subplot(3, 1, 2)
        plt.plot(requests, tmp[1], 'g')
        plt.axhline(dispersion)
        tmp = self.analyze_dependency(size, steps)
        plt.subplot(3, 1, 3)
        plt.plot(steps, tmp, 'b')
