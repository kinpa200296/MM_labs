from lab6 import Model, Phase, Input, Output
from lab3 import GaussRandom, SimpsonRandom, TriangleRandom, EvenRandom, ExponentRandom
from lab1 import BrvRandom
from common import Sample
from matplotlib import pyplot as plt


if __name__ == '__main__':
    phase_cnt = 5
    model = Model(0.01)
    seed_source = BrvRandom(2017)
    inp = Input('', ExponentRandom(seed_source.new_seed(), 1), 10000)
    out = Output('')
    model.add_unit(inp)
    model.add_unit(Phase('1', 3, 4, lambda seed: GaussRandom(seed, 5, 1, 12), seed_source))
    model.add_unit(Phase('2', 3, 3, lambda seed: SimpsonRandom(seed, 2, 5), seed_source))
    model.add_unit(Phase('3', 3, 5, lambda seed: TriangleRandom(seed, 3, 7, 'right'), seed_source))
    model.add_unit(Phase('4', 3, 4, lambda seed: GaussRandom(seed, 5, 1, 12), seed_source))
    model.add_unit(Phase('5', 3, 5, lambda seed: EvenRandom(seed, 3, 9), seed_source))
    model.add_unit(out)

    model.run()

    print 'Cooked.....'
    print model.time
    print inp
    print out
    o1 = out.requests[:-1]
    o2 = out.requests[1:]
    intervals = Sample([o2[i].exit_time - o1[i].exit_time for i in xrange(len(o1))])
    plt.figure(1)
    intervals.draw_hist()
    print 'intervals'
    print intervals.math_expect
    print intervals.dispersion
    duration = Sample([r.exit_time - r.enter_time for r in out.requests])
    plt.figure(2)
    duration.draw_hist()
    print 'duration'
    print duration.math_expect
    print duration.dispersion
    for i in xrange(phase_cnt):
        phase = model.get_unit(i + 1)
        print '=' * 30
        print "Phase", phase.tag
        print Sample.calc_math_expect(phase.storage_stats)
        for j in xrange(len(phase.process.channels)):
            s = sum(phase.channels_stats[j])
            print map(lambda x: 1.0 * x / s, phase.channels_stats[j])
        print '=' * 30

    plt.show()
