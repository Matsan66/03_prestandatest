import pytest
from insertion_sort import InsertionSort


@pytest.fixture
def insertion_sort():
    """
    Creates a InsertionSorter object for testing.
    """
    return InsertionSort()