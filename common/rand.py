from utils import check_integer
from sample import Sample


class BaseRandom(object):

    def __init__(self, seed):
        check_integer(seed, 'seed should be integer value')

        self.seed = seed
        self._value = seed

    def _iter(self):
        raise NotImplementedError()

    def _next_value(self):
        self._iter()
        return self._value

    def rand(self):
        return self._next_value()

    def _expand_value(self, ratio):
        value = self._next_value()
        if ratio is None:
            return value
        return value * ratio

    def randint(self, max_int=None):
        return int(self._expand_value(max_int))

    def sample(self, size=10000):
        return Sample([self.rand() for _ in xrange(size)])

    def new_seed(self):
        [self.randint() for _ in xrange(7)]
        a = self.randint()
        [self.randint() for _ in xrange(11)]
        b = self.randint()
        [self.randint() for _ in xrange(13)]
        c = self.randint()
        return a * b % c
