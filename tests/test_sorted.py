from SortMethods.quick_sort import QuickSort
from SortMethods.buble_sort import BubleSort
from utils.utils import get_random_list
import numpy as np


def test_random_list():
    shuffled_list = get_random_list(20)
    sorted_list = shuffled_list.copy()
    sorted_list.sort()
    assert not np.allclose(shuffled_list, sorted_list)


def test_buble_sort():
    shuffled_list = get_random_list(20)
    sorted_list = shuffled_list.copy()
    sorted_list.sort()
    buble_sort = BubleSort()
    bubled_sorted = buble_sort(input_list=shuffled_list)
    assert np.allclose(bubled_sorted, sorted_list)


def test_quick_sort():
    shuffled_list = get_random_list(20)
    sorted_list = shuffled_list.copy()
    sorted_list.sort()
    quick_sort = QuickSort()
    quicked_sorted = quick_sort(input_list=shuffled_list)
    assert np.allclose(quicked_sorted, sorted_list)
