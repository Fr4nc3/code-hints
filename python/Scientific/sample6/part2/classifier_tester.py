# *******************************************************
# @Fr4nc3
# 05/04/2013
# knn classifier module
# *******************************************************

import time
import classifier


def main():
    """Test KNearest Neighbor."""
    start_time = time.time()
    real_data = classifier.read_data('wdbc.data')
    # synthetic data last parameters is label 1 for B, 0 for M
    syn_data1 = classifier.labeled_synthetic_data([2, 5.5], [[1, 1], [1, 2.5]],
                                                  250, 1)
    syn_data2 = classifier.labeled_synthetic_data([.5, 1], [[1, 0], [0, 1]],
                                                  250, 0)
    k_results = {}
    for k in range(1, 17, 2):
        results_real = classifier.n_validator(real_data, 10,
                                              classifier.knn_classifier, k)
        print("Performance for k = %d real data %.3f " % (k, results_real))
        k_results[k] = results_real

    # this will sort the results from the smallest to the greatest so
    # last one will be the most accurate
    sorted_k_results = classifier.sort_dict(k_results)

    print("Best performance  k = %d  real data %.3f" % (
        sorted_k_results[-1][0], sorted_k_results[-1][1]))

    print("---")
    k_results_syn = {}
    for k in range(1, 17, 2):
        results_sync = classifier.n_validator(syn_data1, 10,
                                              classifier.knn_classifier, k,
                                              syn_data2)
        print("Performance for k = %d synthetic data %.3f " % (k, results_sync))
        k_results_syn[k] = results_sync

    # this will sort the results from the smallest to the greatest so
    # last one will be the most accurate
    sorted_k_syn_results = classifier.sort_dict(k_results_syn)

    print("Best performance  k = %d  data %.3f" % (
        sorted_k_syn_results[-1][0], sorted_k_syn_results[-1][1]))

    print("--- %.6f seconds ---" % (time.time() - start_time))


main()