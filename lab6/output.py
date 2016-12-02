from unit import Unit


class Output(Unit):

    def __init__(self, tag):
        super(Output, self).__init__(tag)
        self._requests = []

    def __str__(self):
        return 'Output: {0}'.format(len(self._requests))

    @property
    def requests(self):
        return self._requests

    @property
    def exited(self):
        return len(self._requests)

    def can_take_request(self):
        return True

    def take_request(self, request):
        super(Output, self).take_request(request)
        request.set_exit_time(self._model.time)
        self._requests.append(request)
