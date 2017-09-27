Fr4nc3

classifier implements


classifier
* knn_classifier
* n_validator
* sort_dict
* get_label
* most_common
* chunks
* synthetic_data
* labeled_synthetic_data
* read_data

distances
* mahalanobis_distance
* euclidean distance
* taxicab distance
* cosine distance


- knn_classifier
 similar to part 1 this knn_classifier, calculates all the distances between
 the test and the training and stored it in a dictionary where key is
 the original index and value is the distance
 here we pass the get_label method which return a label
 This version expects the variable dist_type and
 instead to use euclidean_distance, it uses the distance.cal_distance which
 uses the variable dist_type to discriminate which type of distance
 is uses.


- n_validator
  check if the args are passed and first element is k
  if a second element is passed is we associated with dist_type
  which is the type of distance we are using

  if a 3er args is passed merge two data
  after that random sort the rows in the the data

- distances
  using the library scipy I create two distances
  scipy.spatial.distance.mahalanobis
  scipy.spatial.distance.cosine

  I moved the euclidean_distance method which is a hand made method
  also taxicab distance was written without the need of any library

  mahalonobis from scipy is the slowest distance calculator and doesn't give
  more accuracy.

