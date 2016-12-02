class Model(object):

    def __init__(self, time_step):
        self._time = 0.0
        self._units = []
        self._time_step = time_step

    @property
    def time(self):
        return self._time

    @property
    def units(self):
        return self._units

    @property
    def time_step(self):
        return self._time_step

    def add_unit(self, unit):
        unit.set_model(self)
        self._units.append(unit)

    def get_unit(self, ind):
        return self._units[ind]

    def make_step(self):
        self._time += self._time_step

    def run(self):
        phase_cnt = len(self._units) - 2
        inp = self._units[0]
        out = self._units[phase_cnt + 1]
        while inp.rejected + out.exited < inp.max_gen:
            for i in xrange(phase_cnt, 0, -1):
                phase = self._units[i]
                res = True
                while res and phase.can_send_request():
                    res = phase.try_send_request(self._units[i + 1])
                phase.process_step()
            if inp.can_send_request():
                inp.try_send_request(self._units[1])
            for i in xrange(phase_cnt, 0, -1):
                phase = self._units[i]
                phase.collect_stats()
            self.make_step()
