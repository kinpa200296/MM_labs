from func import FuncRandom
from even import EvenRandom


class SimpsonRandom(FuncRandom):

    def __init__(self, seed, left, right):
        super(SimpsonRandom, self).__init__(seed)

        self._left = left
        self._right = right
        self._rand_obj1 = EvenRandom(self._rand_obj.new_seed(), left / 2.0, right / 2.0)
        self._rand_obj2 = EvenRandom(self._rand_obj.new_seed(), left / 2.0, right / 2.0)

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def rand_obj1(self):
        return self._rand_obj1

    @property
    def rand_obj2(self):
        return self._rand_obj2

    def func(self):
        return self._rand_obj1.rand() + self._rand_obj2.rand()
