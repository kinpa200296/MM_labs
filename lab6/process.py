from unit import Unit
from channel import Channel
from common import BaseRandom, check_instance


class Process(Unit):

    def __init__(self, tag, channels_cnt, rand_func, seed_source):
        check_instance(channels_cnt, int, 'channels count should be integer')
        check_instance(seed_source, BaseRandom, 'seed_source should be an instance of BaseRandom')

        super(Process, self).__init__(tag)
        self._channels = []
        for i in xrange(channels_cnt):
            self._channels.append(Channel(str(i), rand_func(seed_source.new_seed())))

    def __str__(self):
        c = '\n\t'.join(map(str, self._channels))
        return 'Process {0}:\n\t{1}'.format(self._tag, c)

    @property
    def channels(self):
        return self._channels

    def set_model(self, model):
        super(Process, self).set_model(model)
        for channel in self._channels:
            channel.set_model(model)

    def can_take_request(self):
        for channel in self._channels:
            if channel.can_take_request():
                return True
        return False

    def take_request(self, request):
        super(Process, self).take_request(request)
        for channel in self._channels:
            if channel.can_take_request():
                channel.take_request(request)
                return

    def can_send_request(self):
        for channel in self._channels:
            if channel.can_send_request():
                return True
        return False

    def try_send_request(self, dst_unit):
        if super(Process, self).try_send_request(dst_unit):
            for channel in self._channels:
                if channel.can_send_request():
                    if channel.try_send_request(dst_unit):
                        return True
        return False
