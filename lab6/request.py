class Request(object):

    id_cnt = 0

    def __init__(self, model_time):
        self._id = Request.id_cnt
        Request.id_cnt += 1
        self._enter_time = model_time
        self._exit_time = 0

    def __str__(self):
        return 'Request #{0}. {1} - {2}'.format(self._id, self._enter_time, self._exit_time)

    @property
    def id(self):
        return self._id

    @property
    def enter_time(self):
        return self._enter_time

    @property
    def exit_time(self):
        return self._exit_time

    def set_exit_time(self, model_time):
        self._exit_time = model_time
