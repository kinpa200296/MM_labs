from common import DistFunc, check_instance
from lab3 import FuncRandom
import numpy as np


# brv - discrete random variable generator

class DrvRandom(FuncRandom):
    def __init__(self, seed, dist_func):
        check_instance(dist_func, DistFunc, 'dist_func should be instance of DistFunc')

        super(DrvRandom, self).__init__(seed)
        self._dist_func = dist_func

    @property
    def dist_func(self):
        return self._dist_func

    def func(self):
        r = self._rand_obj.rand()
        return self._dist_func.get_value(r)
