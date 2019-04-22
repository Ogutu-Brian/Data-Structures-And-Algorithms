import unittest
from sample_algorithms.algorithms import (
    insertion_sort,
    euclideanAlgorithm
)


class TestInsertionSort(unittest.TestCase):
    """Class that tests insertion sort instances"""

    def test_sorted_list(self):
        """Tests for the sorting of an already sorted list"""
        sorted_list = [1, 2, 3, 4]
        insertion_sort(sorted_list)
        self.assertEqual(sorted_list, [1, 2, 3, 4])

    def test_unsorted_list(self):
        """Tests for sorting of unsorted list"""
        unsorted_list = [32, 2, 1, 56, 6, 13]
        insertion_sort(unsorted_list)
        self.assertEqual(unsorted_list, [1, 2, 6, 13, 32, 56])

    def test_sorted_revsersed_list(self):
        """Tests for a sorted list but in reverse order"""
        sorted_list = [10, 3, 2, 1]
        insertion_sort(sorted_list)
        self.assertEqual(sorted_list, [1, 2, 3, 10])

    def test_negative_values(self):
        """Tests for the negative values"""
        unsorted_list = [-1, -0.893, -2, -10]
        insertion_sort(unsorted_list)
        self.assertEqual(unsorted_list, [-10, -2, -1, -0.893])

    def test_mix_sorted_unsorted_list(self):
        """Tests for a mix of unsorted and sorted list"""
        unsorted_mix = [1, 2, -20, 1, -4.4]
        insertion_sort(unsorted_mix)
        self.assertEqual(unsorted_mix, [-20, -4.4, 1, 1, 2])


class TestEuclideanAlgorithm(unittest.TestCase):
    """
    Tests Euclidean Algorithm
    """

    def test_ecuclidean_algorithm(self):
        """
        Tests euclidean algorithm in descending order
        """
        numbers = (60, 24)
        expected_result = 12
        actual_result = euclideanAlgorithm(*numbers)
        self.assertEqual(expected_result, actual_result)

    def test_eculid_reversed(self):
        """
        Tests euclodean algorithm with values inserted in reversed order
        """
        numbers = (24, 60)
        expected_result = 12
        actual_result = euclideanAlgorithm(*numbers)
        self.assertEqual(expected_result, actual_result)

    def test_ecuclid_with_zero(self):
        """
        Tests euclidean algorithm with a zero
        """
        numbers = 34, 0
        reversed_numbers = 0, 34
        self.assertEqual(34, euclideanAlgorithm(*numbers))
        self.assertEqual(34, euclideanAlgorithm(*reversed_numbers))
