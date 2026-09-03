import pytest
from insertion_sort import InsertionSort
from merge_sort import MergeSort

@pytest.fixture
def insertion_sort():
    """
    Creates an InsertionSort object for testing.
    """
    return InsertionSort()

@pytest.fixture
def merge_sort():
    """
    Creates a MergeSort object for testing.
    """
    return MergeSort()