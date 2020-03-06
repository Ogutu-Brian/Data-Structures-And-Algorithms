import unittest
from sample_algorithms.algorithms import (
    insertion_sort,
    euclideanAlgorithm,
    consucetive_integer_checking_algorithm
)
from primitive_types.primitives import PrimitiveTypes


class TestInsertionSort(unittest.TestCase):
    """
    Class that tests insertion sort instances
    """

    def test_sorted_list(self) -> None:
        """Tests for the sorting of an already sorted list"""
        sorted_list = [1, 2, 3, 4]
        insertion_sort(sorted_list)
        self.assertEqual(
            sorted_list,
            [1, 2, 3, 4]
        )

    def test_unsorted_list(self) -> None:
        """
        Tests for sorting of unsorted list
        """
        unsorted_list = [32, 2, 1, 56, 6, 13]
        insertion_sort(unsorted_list)
        self.assertEqual(
            unsorted_list,
            [1, 2, 6, 13, 32, 56]
        )

    def test_sorted_revsersed_list(self) -> None:
        """
        Tests for a sorted list but in reverse order
        """
        list_1 = [10, 3, 2, 1]
        list_2 = [5, 2, 4, 6, 1, 3]
        insertion_sort(list_1)
        insertion_sort(list_2)
        self.assertEqual(
            list_1,
            [1, 2, 3, 10]
        )
        self.assertEqual(
            list_2,
            [1,2,3,4,5,6]
        )

    def test_negative_values(self) -> None:
        """
        Tests for the negative values
        """
        unsorted_list = [-1, -0.893, -2, -10]
        insertion_sort(unsorted_list)
        self.assertEqual(
            unsorted_list,
            [-10, -2, -1, -0.893]
        )

    def test_mix_sorted_unsorted_list(self) -> None:
        """
        Tests for a mix of unsorted and sorted list
        """
        unsorted_mix = [1, 2, -20, 1, -4.4]
        insertion_sort(unsorted_mix)
        self.assertEqual(
            unsorted_mix,
            [-20, -4.4, 1, 1, 2]
        )


class TestEuclideanAlgorithm(unittest.TestCase):
    """
    Tests Euclidean Algorithm
    """

    def test_euclidean_algorithm(self) -> None:
        """
        Tests euclidean algorithm in descending order
        """
        numbers = (60, 24)
        expected_result = 12
        actual_result = euclideanAlgorithm(*numbers)
        self.assertEqual(
            expected_result,
            actual_result
        )

    def test_eculid_reversed(self) -> None:
        """
        Tests euclodean algorithm with values inserted in reversed order
        """
        numbers = (24, 60)
        expected_result = 12
        actual_result = euclideanAlgorithm(*numbers)
        self.assertEqual(
            expected_result,
            actual_result
        )

    def test_ecuclid_with_zero(self) -> None:
        """
        Tests euclidean algorithm with a zero
        """
        numbers = 34, 0
        reversed_numbers = 0, 34
        self.assertEqual(
            34,
            euclideanAlgorithm(*numbers)
        )
        self.assertEqual(
            34,
            euclideanAlgorithm(*reversed_numbers)
        )


class TestConsecutiveIntegerCheckingAlgorithm(unittest.TestCase):
    """
    Tests consucutive checking algorithm to find the gcd of numbers
    """

    def test_consucutive_integer_checking_algorithm(self) -> None:
        """
        Tests consucutive checking algorithm in descending order
        """
        numbers = (60, 24)
        expected_result = 12
        actual_result = consucetive_integer_checking_algorithm(*numbers)
        self.assertEqual(
            expected_result,
            actual_result
        )

    def test_consucutive_integer_checking_algorithm_reversed(self) -> None:
        """
        Tests consucutive chekcing algorithm in reversed order
        """
        numbers = (24, 60)
        expected_result = 12
        actual_result = consucetive_integer_checking_algorithm(*numbers)
        self.assertEqual(
            expected_result,
            actual_result
        )

    def test_consucutive_integer_checking_algorithm_with_zero(self) -> None:
        """
        Tests consucutive algorithm  with a zero
        """
        numbers = 34, 0
        reversed_numbers = 0, 34
        self.assertEqual(
            34,
            consucetive_integer_checking_algorithm(*numbers)
        )
        self.assertEqual(
            34,
            consucetive_integer_checking_algorithm(*reversed_numbers)
        )


class TestPrimitiveTypes(unittest.TestCase):
    """
    Tests primitive types
    """

    def test_count_num_bits(self) -> None:
        """
        Tests for the number of bits in a number
        """
        number = 12
        expected_bits = 4
        self.assertEqual(expected_bits, PrimitiveTypes.count_num_bits(number))
