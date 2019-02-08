import unittest
from sample_algorithms.algorithms import (insertion_sort, swap_values)


class TestInsertionSort(unittest.TestCase):
    """Class that tests insertion sort instances"""

    def test_swap(self):
        """Tests for swapping of values"""
        a = 3
        b = 4
        result =swap_values(a, b)
        a=result[0]
        b=result[1]
        self.assertEqual((a, b), (4, 3))

    def test_sorted_list(self):
        """Tests for the sorting of an already sorted list"""
        sorted_list = [1, 2, 3, 4]
        result = insertion_sort(sorted_list)
        self.assertEqual(sorted_list, result)
