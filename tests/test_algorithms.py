import unittest
from sample_algorithms.algorithms import (
    insertion_sort, euclideanAlgorithm, fibunacci, sieve_of_eratosthenese,
    is_prime, consucetive_integer_checking_algorithm, bubble_sort, selection_sort,
    selection_sort, merge_sort, quick_sort, binary_search
)
from primitive_types.primitives import PrimitiveTypes


class TestInsertionSort(unittest.TestCase):
    """
    Class that tests insertion sort instances
    """

    def test_sorted_list(self):
        """Tests for the sorting of an already sorted list"""
        sorted_list = [1, 2, 3, 4]
        insertion_sort(sorted_list)
        self.assertEqual(
            sorted_list,
            [1, 2, 3, 4]
        )

    def test_unsorted_list(self):
        """
        Tests for sorting of unsorted list
        """
        unsorted_list = [32, 2, 1, 56, 6, 13]
        insertion_sort(unsorted_list)
        self.assertEqual(
            unsorted_list,
            [1, 2, 6, 13, 32, 56]
        )

    def test_sorted_revsersed_list(self):
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
            [1, 2, 3, 4, 5, 6]
        )

    def test_negative_values(self):
        """
        Tests for the negative values
        """
        unsorted_list = [-1, -0.893, -2, -10]
        insertion_sort(unsorted_list)
        self.assertEqual(
            unsorted_list,
            [-10, -2, -1, -0.893]
        )

    def test_mix_sorted_unsorted_list(self):
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

    def test_euclidean_algorithm(self):
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

    def test_eculid_reversed(self):
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

    def test_ecuclid_with_zero(self):
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

    def test_consucutive_integer_checking_algorithm(self):
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

    def test_consucutive_integer_checking_algorithm_reversed(self):
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

    def test_consucutive_integer_checking_algorithm_with_zero(self):
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

    def test_count_num_bits(self):
        """
        Tests for the number of bits in a number
        """
        number = 12
        expected_bits = 4
        self.assertEqual(expected_bits, PrimitiveTypes.count_num_bits(number))


class TestsFibunacci(unittest.TestCase):
    """
    tests for fibunacci using dynamic programming
    """

    def test_for_zerp(self):
        self.assertEqual(0, fibunacci(0))

    def test_for_one(self):
        self.assertEqual(1, fibunacci(1))

    def test_for_seventh(self):
        self.assertEqual(13, fibunacci(7))


class TestsForSieveOfEratosthenes(unittest.TestCase):
    def test_for_first_25(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23],
                         sieve_of_eratosthenese(25))


class TestsForPrimeNumbers(unittest.TestCase):
    def test_for_non_prime(self):
        self.assertEqual(False, is_prime(10))

    def test_for_prime(self):
        self.assertEqual(True, is_prime(5))

    def test_for_large_non_prime(self):
        self.assertEqual(False, is_prime(1240))

    def test_for_large_prime(self):
        self.assertEqual(True, is_prime(419))

    def test_for_zero(self):
        self.assertEqual(False, is_prime(0))

    def test_for_two(self):
        self.assertEqual(False, is_prime(1))


class TestBubbleSort(unittest.TestCase):
    def test_for_empty_list(self):
        self.assertEqual([], bubble_sort([]))

    def test_bubble_sort_for_length_1(self):
        self.assertEqual([2], bubble_sort([2]))

    def test_for_sorted_two_values(self):
        self.assertEqual([1, 2], bubble_sort([1, 2]))

    def test_for_unsorted_two_values(self):
        self.assertEqual([1, 2], bubble_sort([2, 1]))

    def test_for_unsorted_list(self):
        self.assertEqual([1, 2, 4, 5, 8], bubble_sort([5, 1, 4, 2, 8]))


class TestSelectionSort(unittest.TestCase):
    def test_selection_sort_for_one(self):
        self.assertEqual([1], selection_sort([1]))

    def test_selection_sort_for_empty_array(self):
        self.assertEqual([], selection_sort([]))

    def test_selection_sort_for_large_array(self):
        self.assertEqual(selection_sort(
            [64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_for_unsorted_two_values(self):
        self.assertEqual([1, 2], selection_sort([2, 1]))

    def test_for_sorted_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6],
                         selection_sort([1, 2, 3, 4, 5, 6]))


class TestMergeSort(unittest.TestCase):
    def test_selection_sort_for_one(self):
        self.assertEqual([1], merge_sort([1]))

    def test_selection_sort_for_empty_array(self):
        self.assertEqual([], merge_sort([]))

    def test_selection_sort_for_large_array(self):
        self.assertEqual(merge_sort([64, 25, 12, 22, 11]), [
                         11, 12, 22, 25, 64])

    def test_for_unsorted_two_values(self):
        self.assertEqual([1, 2], merge_sort([2, 1]))

    def test_for_sorted_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], merge_sort([1, 2, 3, 4, 5, 6]))


class TestQuickSort(unittest.TestCase):
    def test_selection_sort_for_one(self):
        self.assertEqual([1], quick_sort([1]))

    def test_selection_sort_for_empty_array(self):
        self.assertEqual([], quick_sort([]))

    def test_selection_sort_for_large_array(self):
        self.assertEqual(quick_sort([64, 25, 12, 22, 11]), [
                         11, 12, 22, 25, 64])

    def test_for_unsorted_two_values(self):
        self.assertEqual([1, 2], quick_sort([2, 1]))

    def test_for_sorted_list(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], quick_sort([1, 2, 3, 4, 5, 6]))


class TestBinarySearch(unittest.TestCase):
    def test_for_empty_list(self):
        self.assertEqual(None, binary_search([], 30))

    def test_for_searching_for_single_array(self):
        self.assertEqual(30, binary_search([30], 30))

    def test_in_large_array(self):
        self.assertEqual(56, binary_search(
            [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 56))
