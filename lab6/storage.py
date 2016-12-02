from unit import Unit
from common import check_instance


class Storage(Unit):

    def __init__(self, tag, limit):
        check_instance(limit, int, 'expected an integer limit')

        super(Storage, self).__init__(tag)
        self._limit = limit
        self._requests = []

    def __str__(self):
        return 'Storage {0}: {1}/{2}'.format(self._tag, self.size, self._limit)

    @property
    def limit(self):
        return self._limit

    @property
    def requests(self):
        return self._requests

    @property
    def size(self):
        return len(self._requests)

    def can_take_request(self):
        return len(self._requests) < self._limit

    def take_request(self, request):
        super(Storage, self).take_request(request)
        self._requests.append(request)

    def can_send_request(self):
        return len(self._requests) > 0

    def try_send_request(self, dst_unit):
        if super(Storage, self).try_send_request(dst_unit):
            dst_unit.take_request(self._requests[0])
            self._requests.__delitem__(0)
            return True
        return False
