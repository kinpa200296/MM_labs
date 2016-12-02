from common import RandomAnalyzer
from lab1 import BrvRandom
from matplotlib import pyplot as plt


if __name__ == '__main__':
    analyzer = RandomAnalyzer(BrvRandom(2017))
    plt.figure(1)
    analyzer.plot_analysis(range(1000, 10000, 10), 10000, range(1, 100))
    plt.figure(2)
    rand = BrvRandom(2017)
    rand.sample(100000).draw_hist(20)
    plt.show()
