from func import FuncRandom


class EvenRandom(FuncRandom):
    def __init__(self, seed, left, right):
        super(EvenRandom, self).__init__(seed)

        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def func(self):
        return self._left + (self._right - self._left) * self._rand_obj.rand()
