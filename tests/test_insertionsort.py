import unittest
from sample_algorithms.algorithms import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """Class that tests insertion sort instances"""

    def test_sorted_list(self):
        """Tests for the sorting of an already sorted list"""
        sorted_list = [1, 2, 3, 4]
        result = insertion_sort(sorted_list)
        self.assertEqual(sorted_list, result)
