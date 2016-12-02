from common import BaseRandom
from lab1 import BrvRandom


class FuncRandom(BaseRandom):

    def __init__(self, seed, rand_class=BrvRandom):
        super(FuncRandom, self).__init__(seed)

        self._rand_obj = rand_class(seed)

    @property
    def rand_obj(self):
        return self._rand_obj

    def func(self):
        return self._rand_obj.rand()

    def _iter(self):
        self._value = self.func()
