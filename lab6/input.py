from unit import Unit
from request import Request


class Input(Unit):

    def __init__(self, tag, rand, max_gen):
        super(Input, self).__init__(tag)
        self._rand = rand
        self._max_gen = max_gen
        self._generated = 0
        self._rejected = 0
        self._next_request = 0.0

    def __str__(self):
        return 'Input: {0}. Rejected: {1}. Next: {2}'.format(self._generated, self._rejected, self._next_request)

    @property
    def rand(self):
        return self._rand

    @property
    def max_gen(self):
        return self._max_gen

    @property
    def generated(self):
        return self._generated

    @property
    def rejected(self):
        return self._rejected

    def can_send_request(self):
        return self._generated < self._max_gen and self._model.time >= self._next_request

    def try_send_request(self, dst_unit):
        if super(Input, self).try_send_request(dst_unit):
            dst_unit.take_request(self._gen_request())
            return True
        self._gen_request()
        self._rejected += 1
        return False

    def _gen_request(self):
        r = Request(self._model.time)
        self._generated += 1
        self._next_request = self._model.time + self._rand.rand()
        return r
