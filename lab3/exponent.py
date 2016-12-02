from func import FuncRandom
from math import log


class ExponentRandom(FuncRandom):

    def __init__(self, seed, param):
        super(ExponentRandom, self).__init__(seed)
        if not param > 0:
            raise ValueError('param should be greater than 0')

        self._param = param

    @property
    def param(self):
        return self._param

    def func(self):
        return -1.0 / self._param * log(1 - self._rand_obj.rand())
