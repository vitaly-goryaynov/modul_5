import unittest
from homework_5_0 import *


class LengthArrayTestCase(unittest.TestCase):

    def test_length_array_10(self):
        len_1 = length([i for i in range(1, 11, 1)])
        self.assertEqual(len_1, 10)

    def test_length_array_100000(self):
        len_1 = length([i for i in range(1, 100001, 1)])
        self.assertEqual(len_1, 100000)

    def test_length_array_0(self):
        len_1 = length([])
        self.assertEqual(len_1, 0)

    def test_length_array_str(self):
        len_1 = length([23, 'text'])
        self.assertEqual(len_1, 2)


class FindMaxArrayTestCase(unittest.TestCase):

    def test_array_3_elem(self):
        result = find_max([2, 1, 4])
        self.assertEqual(result, (4, 2))

    def test_array_100_elem(self):
        result = find_max([i for i in range(0, 101, 1)])
        self.assertEqual(result, (100, 100))

    def test_array_1000_elem(self):
        result = find_max([i for i in range(0, 1001, 1)])
        self.assertEqual(result, (1000, 1000))

    def test_array_0_elem(self):
        result = find_max([])
        self.assertEqual(result, 0)


class ReverseArrayTestCase(unittest.TestCase):

    def test_reverse_0_elem(self):
        result = reverse([])
        self.assertEqual(result, 'Список пустой')

    def test_reverse_10_elem(self):
        result = reverse([i for i in range(0, 10, 1)])
        self.assertEqual(result, [i for i in range(9, -1, -1)])

    def test_reverse_1000_elem(self):
        result = reverse([i for i in range(0, 1000, 1)])
        self.assertEqual(result, [i for i in range(999, -1, -1)])

    def test_reverse_str_elem(self):
        result = reverse(['12', 'text'])
        self.assertEqual(result, ['text', '12'])

    def test_reverse_1_elem(self):
        result = reverse([1])
        self.assertEqual(result, [1])

class LianerSearchTestCase(unittest.TestCase):

    def test_index_target_str(self):
        result = lianer_search([1, 2, 4, -1, '1'], 1)
        self.assertEqual(result, 0)


    def test_index_target_1_elem(self):
        result = lianer_search([1, 2, 4, -1, '1'], '1')
        self.assertEqual(result, 4)

    def test_index_target_random_elem(self):
        result = lianer_search([1, 2, 4, -1, '1'], 7)
        self.assertEqual(result, -1)

#