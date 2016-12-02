from func import FuncRandom
from common import check_integer
from math import log


class GammaRandom(FuncRandom):
    def __init__(self, seed, param, cnt):
        super(GammaRandom, self).__init__(seed)
        check_integer(cnt, 'cnt should be integer')
        if not param > 0:
            raise ValueError('param should be greater than 0')
        if not cnt > 0:
            raise ValueError('cnt should be greater than 0')

        self._param = param
        self._cnt = cnt

    @property
    def param(self):
        return self._param

    @property
    def cnt(self):
        return self._cnt

    def func(self):
        s = sum([log(self._rand_obj.rand()) for _ in xrange(self._cnt)])
        return -1.0 / self._param * s
