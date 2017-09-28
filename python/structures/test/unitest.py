class WeirdArithmetic:
    n = 11

    @classmethod
    def add_weirdly(cls, n1, n2):
        '''Special way to add'''
        return n1 + n2 + WeirdArithmetic.n


import unittest


class TestWeirdArithmetic(unittest.TestCase):
    def setUp(self):
        self.n1 = 144441
        self.n2 = 255552

    def test_weird_add(self):
        self.assertEqual(400004,
                         WeirdArithmetic.add_weirdly(self.n1, self.n2))
