from lab3 import ExponentRandom, GaussRandom, EvenRandom, GammaRandom, TriangleRandom, SimpsonRandom
from matplotlib import pyplot as plt


def plot_hists(seed, rands, size=5000, bins=20):
    for i in xrange(len(rands)):
        plt.figure(i + 1)
        rand = rands[i](seed)
        rand.sample(size).draw_hist(bins)


if __name__ == '__main__':
    randoms = []
    randoms.append(lambda seed: EvenRandom(seed, -1, 1))
    randoms.append(lambda seed: GaussRandom(seed, 0, 0.2, 6))
    randoms.append(lambda seed: ExponentRandom(seed, 1))
    randoms.append(lambda seed: GammaRandom(seed, 1, 6))
    randoms.append(lambda seed: TriangleRandom(seed, 1, 6))
    randoms.append(lambda seed: TriangleRandom(seed, 1, 6, 'right'))
    randoms.append(lambda seed: SimpsonRandom(seed, 1, 6))

    plot_hists(2017, randoms, 10000)

    plt.show()
