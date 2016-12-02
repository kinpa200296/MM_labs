from unit import Unit
from process import Process
from storage import Storage


class Phase(Unit):

    def __init__(self, tag, storage_limit, channels_cnt, rand_func, seed_source):
        super(Phase, self).__init__(tag)
        self._storage = Storage(tag, storage_limit)
        self._process = Process(tag, channels_cnt, rand_func, seed_source)
        self.storage_stats = []
        self.channels_stats = [[0, 0, 0] for _ in xrange(channels_cnt)]

    def __str__(self):
        s = ['='*30, 'Phase {0}'.format(self.tag), str(self._storage), str(self._process), '='*30]
        return str.join('\n', s)

    @property
    def storage(self):
        return self._storage

    @property
    def process(self):
        return self._process

    def set_model(self, model):
        super(Phase, self).set_model(model)
        self._process.set_model(model)
        self._storage.set_model(model)

    def process_step(self):
        while self._storage.can_send_request() and self._process.can_take_request():
            self._storage.try_send_request(self._process)

    def collect_stats(self):
        self.storage_stats.append(self._storage.size)
        for i in xrange(len(self._process.channels)):
            self.channels_stats[i][self._process.channels[i].get_state()] += 1

    def can_take_request(self):
        return self._process.can_take_request() or self._storage.can_take_request()

    def take_request(self, request):
        super(Phase, self).take_request(request)
        if self._process.can_take_request():
            self._process.take_request(request)
            return
        if self._storage.can_take_request():
            self._storage.take_request(request)

    def can_send_request(self):
        return self._process.can_send_request()

    def try_send_request(self, dst_unit):
        if super(Phase, self).try_send_request(dst_unit):
            return self._process.try_send_request(dst_unit)
        return False
