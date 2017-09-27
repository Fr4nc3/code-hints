# *******************************************************
# @Fr4nc3
# 04/27/2013
# nn classifier module
# *******************************************************

import time
import classifier


def main():
    """Test Nearest Neighbor."""
    start_time = time.time()
    real_data = classifier.read_data('wdbc.data')
    # synthetic data last parameters is label 1 for B, 0 for M
    syn_data1 = classifier.labeled_synthetic_data([2, 5.5], [[1, 1], [1, 2.5]],
                                                  250, 1)
    syn_data2 = classifier.labeled_synthetic_data([.5, 1], [[1, 0], [0, 1]],
                                                  250, 0)

    #performance of real data
    results_real = classifier.n_validator(real_data, 10,
                                          classifier.nn_classifier)
    #performance of synthetic data
    results_synthetic = classifier.n_validator(syn_data1, 10,
                                               classifier.nn_classifier,
                                               syn_data2)

    print("Performance for real data %.3f " % results_real)
    print("Performance for synthetic data %.3f " % results_synthetic)

    print("--- %.6f seconds ---" % (time.time() - start_time))


main()