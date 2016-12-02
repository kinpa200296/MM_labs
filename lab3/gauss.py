from func import FuncRandom
from common import check_integer
from math import sqrt


class GaussRandom(FuncRandom):

    def __init__(self, seed, exp_val, std_dev, cnt):
        super(GaussRandom, self).__init__(seed)
        check_integer(cnt, 'cnt should be integer')
        if not std_dev > 0:
            raise ValueError('std_dev should be greater than 0')
        if not cnt > 0:
            raise ValueError('cnt should be greater than 0')

        self._exp_val = exp_val
        self._std_dev = std_dev
        self._cnt = cnt

    @property
    def exp_val(self):
        return self._exp_val

    @property
    def std_dev(self):
        return self._std_dev

    @property
    def cnt(self):
        return self._cnt

    def func(self):
        s = sum([self._rand_obj.rand() for _ in xrange(self._cnt)])
        s -= self._cnt / 2.0
        return self._exp_val + self._std_dev * sqrt(12.0 / self._cnt) * s
