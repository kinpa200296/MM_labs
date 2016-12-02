from common import BaseRandom, check_integer, gcd

# brv - basic random variable generator

# my own assumption
# DEFAULT_MULTIPLIER = (1 << 14) - (1 << 12) - 1
# DEFAULT_MODULUS = 1 << 32

# minimal standard random number generator
DEFAULT_MULTIPLIER = 16807
DEFAULT_MODULUS = (1 << 31) - 1


class BrvRandom(BaseRandom):

    def __init__(self, seed, multiplier=DEFAULT_MULTIPLIER, modulus=DEFAULT_MODULUS):
        super(BrvRandom, self).__init__(seed)
        check_integer(multiplier, 'multiplier should be integer value')
        check_integer(modulus, 'modulus should be integer value')
        if gcd(multiplier, modulus) != 1:
            raise ValueError('multiplier and modulus must be relatively prime')

        self._multiplier = multiplier
        self._modulus = modulus

    @property
    def multiplier(self):
        return self._multiplier

    @property
    def modulus(self):
        return self._modulus

    def _iter(self):
        self._value = (self._value * self._multiplier) % self._modulus

    def rand(self):
        return (1.0 * super(BrvRandom, self).rand()) / self._modulus

    def randint(self, max_int=None):
        m = (1 if max_int is None else self._modulus)
        return int((1.0 * super(BrvRandom, self).randint(max_int)) / m)
