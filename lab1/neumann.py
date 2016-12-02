from common import BaseRandom, check_integer

# Neumann method for generating pseudo-random numbers


class NeumannRandom(BaseRandom):

    def __init__(self, seed, size=4):
        super(NeumannRandom, self).__init__(seed)
        check_integer(size, 'size should be integer value')
        lower = 10**(size - 1)
        upper = 10**size - 1
        if seed < lower or seed > upper:
            raise ValueError('seed should be within range [{0}, {1}]'.format(lower, upper))
        if size % 2 == 1:
            raise ValueError('size should be even')

        self.size = size
        self._divisor = 10 ** (self.size / 2)
        self._modulus = 10 ** self.size

    @property
    def divisor(self):
        return self._divisor

    @property
    def modulus(self):
        return self._modulus

    def _iter(self):
        self._value = (self._value ** 2 / self._divisor) % self._modulus

    def rand(self):
        return (1.0 * super(NeumannRandom, self).rand()) / self._modulus

    def randint(self, max_int=None):
        m = (1 if max_int is None else self._modulus)
        return int((1.0 * super(NeumannRandom, self).randint(max_int)) / m)
