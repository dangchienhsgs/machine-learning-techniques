import numpy as np
from minepy import MINE
from scipy.stats import pearsonr


def correlation_between_feature():
    feature_x = [1, 2, 3, 4, 5]
    feature_y = [2, 4, 6, 8, 10]

    print " {0} \n {1} \n correlation --> {2}".format(feature_x, feature_y, pearsonr(feature_x, feature_y))

    feature_x = [1, 2, 3, 4, 5]
    feature_y = [1.1, 2.2, 3.0, 4.1, 4.9]
    print " {0} \n {1} \n correlation --> {2}".format(feature_x, feature_y, pearsonr(feature_x, feature_y))


def maximal_information_coeffcient():
    m = MINE()
    x = np.random.uniform(-1, 1, 1000)
    m.compute_score(x, x ** 2 + 2)
    print m.mic()

if __name__ == "__main__":
    print "-------------------- Experiment 1 -------------------"
    correlation_between_feature()
    print "-----------------------------------------------------\n"

    print "-------------------- Experiment 2 -------------------"
    maximal_information_coeffcient()
