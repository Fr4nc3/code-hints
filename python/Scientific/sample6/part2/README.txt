# @Fr4nc3

classifier implements

* knn_classifier
* n_validator
* sort_dict
* get_label
* most_common
* euclidean_distance
* chunks
* synthetic_data
* labeled_synthetic_data
* read_data


- knn_classifier
 similar to part 1 this knn_classifier, calculates all the distances between
 the test and the training and stored it in a dictionary where key is
 the original index and value is the distance
 here we pass the get_label method which return a label

- get_label
  get the dictionary distances, and array with the same order with labels and k
  - first sort the dictionary distances in base of its values (distances)
  ex distances ={ 0: 1.54, 1: 3.5, 2: 0.3 ...}
  sort_dict return an array with
   [[2,0.3],[0,1.53],[1,3.5] ...]
   the sort is shortest distance first
  ie [[index,distance]]
  we get the training label which is in the same position of index
  and we added it to the label list

  here we pass this list of labels to most_common method

- most_common
 it returns the most common label (the one that repeat most).

- sort_dict
  distances ={ 0: 1.54, 1: 3.5, 2: 0.3 ...}
  return a list with each element is a new list with two element sorted from the
  smallest value to the greatest
  [[key,value]]
  I didn't convert back to a dictionary because I didn't find it necessary

- n_validator
  check if the args are passed and first element is k
  if the second args is passed merge two data
  after that random sort the rows in the the data


- read_data
each line looks like this:

842302,M,17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,
25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189

first element is ignored
second element is label where M is converted 0
and B in 1
so the data returned is like
[[17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,
25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189], 0
..]


- chuncks
  split a list in p groups

- synthetic_data
 it generated in base of the requirement given on the hw 6 part 1
 description.
 Class 1: mean = [2, 5.5], covariance = [[1, 1], [1, 2.5] ], 250 samples.
 Class 2: mean = [.5, 1], covariance = [[1, 0], [0, 1]], 250 samples


- labeled_synthetic_data
 it creates synthetic data and its label, also it has the same array structure
 than what read_data returns, so it is easy to use n_validator
 labeled class 1 as (1)B
 labeled class 2 as (0)M

- euclidean_distance
  I calculated manually the euclidean distance
  but also I tried
  return np.linalg.norm(np.array(a)-np.array(b))
  from scipy.spatial import distance
  return distance.euclidean(a, b)
  the second one(scipy) is very slow
  and they don't give me more accuracy than my manual euclidean distance
