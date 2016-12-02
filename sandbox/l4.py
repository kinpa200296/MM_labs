from common import DistFunc
from lab3 import GaussRandom
from lab4 import DrvRandom
from matplotlib import pyplot as plt


if __name__ == '__main__':
    size = 500
    s1 = GaussRandom(2017, 0, 1, 12).sample(size)
    dist_func = DistFunc(s1)
    # print dist_func.probabilities
    # print dist_func.values
    # print dist_func.edges
    s2 = DrvRandom(2017, dist_func).sample(size)

    plt.figure(1)
    plt.subplot(1, 2, 1)
    s1.draw_hist(20)
    plt.subplot(1, 2, 2)
    s2.draw_hist(20)
    plt.figure(2)
    dist_func.draw()
    plt.show()
