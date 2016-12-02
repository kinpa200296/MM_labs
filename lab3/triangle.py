from func import FuncRandom, BrvRandom


class TriangleRandom(FuncRandom):
    def __init__(self, seed, left, right, align='left'):
        super(TriangleRandom, self).__init__(seed)
        if not (align == 'left' or align == 'right'):
            raise ValueError('align should be only \'left\' or \'right\'')

        self._left = left
        self._right = right
        self._align = align
        self._rand_obj1 = BrvRandom(self._rand_obj.new_seed())
        self._rand_obj2 = BrvRandom(self._rand_obj.new_seed())

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def align(self):
        return self._align

    @property
    def rand_obj1(self):
        return self._rand_obj1

    @property
    def rand_obj2(self):
        return self._rand_obj2

    def func(self):
        r = 0
        if self._align == 'left':
            r = min(self._rand_obj1.rand(), self._rand_obj2.rand())
        if self._align == 'right':
            r = max(self._rand_obj1.rand(), self._rand_obj2.rand())
        return self._left + (self._right - self._left) * r
