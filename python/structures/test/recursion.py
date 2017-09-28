global given_list


def set_given_list(a_list):
    global given_list
    given_list = a_list


def index_of_an_amount(an_amount=0, a_begin=0, an_end=0):
    '''
    Intent: first index where an_amount occurs in sublist of given_list

    Pre1 (Segment legitimate): 0 <= a_begin <= an_end < len(given_list)
    Pre2 (List ordered): given_list[0] <= given_list[1] <= ...

    Post1 (Range): -1 <= returned_index < len(given_list)
    Post2 (Minimal): returned_index is minimal
    Post3 (Matches?):
    given_list[returned_index] == an_amount
    --OR--
    given_list[i] != an_amount for every i
    '''

    #### Objective 1: Post1 (Range) AND Post2 (Minimal)

    returned_index = -1

    #### [Objective 2] (1 element?):
    # EITHER a_begin < an_end
    # OR Post3 AND this has returned

    if a_begin == an_end:  # second part of EITHER-OR
        if given_list[a_begin] == an_amount:
            returned_index = a_begin
        return returned_index

    #### Objective 3: Post3

    midpoint = int((a_begin + an_end) / 2)  # Python: e.g., int(5.7) is 5
    # For minimality, consider left of midpoint even if an_amount = given_list[midpoint]
    if an_amount <= given_list[midpoint]:  # a match in left half if at all
        returned_index = index_of_an_amount(an_amount, a_begin, midpoint)  # minimal match index
        # recursion terminates: see * below
    else:
        returned_index = index_of_an_amount(an_amount, midpoint + 1, an_end)
    return returned_index


import unittest

class TestBinarySearch(unittest.TestCase):

    def test_ind_of_p1_in_given_list(self):

        # NOMINAL TESTS =============================
        # Test n1
        set_given_list([1, 3, 3, 3, 5, 8, 9, 9])
        self.assertEqual(1, index_of_an_amount(3, 0, 1))
        # Test n2
        set_given_list([1, 3, 3, 3, 5, 8, 9, 9])
        self.assertEqual(1, index_of_an_amount(3, 0, 7))
        # Test n3
        set_given_list([1, 3, 4, 4, 5, 5, 5, 9])
        self.assertEqual(4, index_of_an_amount(5, 0, 7))

        # CORNER TESTS ===============================
        # Test c1: default parameter values on trivial list
        set_given_list([1])
        self.assertEqual(-1, index_of_an_amount())  #absent when using default values
        # Test c2: lower = upper bound
        set_given_list([1, 3, 4, 4, 5, 5, 5, 9])
        self.assertEqual(3, index_of_an_amount(4, 3, 3))
        # Test c3: absent from lower = upper bound
        set_given_list([1, 3, 4, 4, 5, 5, 5, 9])
        self.assertEqual(-1, index_of_an_amount(14, 3, 3))
        # Test c4: all equal
        set_given_list([11, 11, 11, 11, 11, 11, 11, 11])
        self.assertEqual(3, index_of_an_amount(11, 3, 7))


if __name__ == '__main__':
     unittest.main()

