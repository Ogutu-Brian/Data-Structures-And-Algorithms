import unittest
from sample_algorithms.algorithms import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """Class that tests insertion sort instances"""

    def test_sorted_list(self)->None:
        """Tests for the sorting of an already sorted list"""
        sorted_list = [1, 2, 3, 4]
        insertion_sort(sorted_list)
        self.assertEqual(sorted_list, [1, 2, 3, 4])

    def test_unsorted_list(self)->None:
        """Tests for sorting of unsorted list"""
        unsorted_list = [32, 2, 1, 56, 6, 13]
        insertion_sort(unsorted_list)
        self.assertEqual(unsorted_list, [1, 2, 6, 13, 32, 56])
