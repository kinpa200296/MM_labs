from unit import Unit
from common import BaseRandom, check_instance


class Channel(Unit):

    def __init__(self, tag, rand):
        check_instance(rand, BaseRandom, 'rand should be an instance of BaseRandom')
        
        super(Channel, self).__init__(tag)
        self._rand = rand
        self._request = None
        self._start_time = 0
        self._end_time = 0

    def __str__(self):
        return 'Channel {0}: {1}'.format(self._tag, self.get_state())

    @property
    def rand(self):
        return self._rand

    @property
    def request(self):
        return self._request

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    def get_state(self):
        if self._request is None:
            return 0
        if self._end_time > self._model.time:
            return 1
        return 2

    def can_take_request(self):
        return self._request is None

    def take_request(self, request):
        super(Channel, self).take_request(request)
        self._request = request
        self._start_time = self._model.time
        self._end_time = self._model.time + self._rand.rand()

    def can_send_request(self):
        return self._request is not None and self._end_time <= self._model.time

    def try_send_request(self, dst_unit):
        if super(Channel, self).try_send_request(dst_unit):
            dst_unit.take_request(self._request)
            self._request = None
            return True
        return False
