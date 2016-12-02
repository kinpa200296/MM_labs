from model import Model
from request import Request
from common import check_instance


class Unit(object):

    id_cnt = 0

    def __init__(self, tag):
        self._id = Unit.id_cnt
        Unit.id_cnt += 1
        self._tag = tag
        self._model = None

    def __str__(self):
        return 'Unit {0} (id = {1})'.format(self._tag, self._id)

    @property
    def id(self):
        return self._id

    @property
    def tag(self):
        return self._tag

    @property
    def model(self):
        return self._model

    def set_model(self, model):
        check_instance(model, Model, 'expected an instance of Model')
        self._model = model

    def process_step(self):
        pass

    def collect_stats(self):
        pass

    def can_take_request(self):
        return False

    def take_request(self, request):
        check_instance(request, Request, 'expected an instance of request')
        if not self.can_take_request():
            raise RuntimeError('can\'t take any more requests')

    def can_send_request(self):
        return False

    def try_send_request(self, dst_unit):
        check_instance(dst_unit, Unit, 'Expected an instance of Unit')
        if not self.can_send_request():
            raise RuntimeError('can\'t send any more requests')

        if dst_unit.can_take_request():
            return True

        return False
