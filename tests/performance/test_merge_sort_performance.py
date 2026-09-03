import pytest
from help_files import help_functions

@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_3000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 3000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(3000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)


@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_5000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 5000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(5000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)


@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_7000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 7000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(7000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)


@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_9000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 9000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(9000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)


@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_11000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 11000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(11000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)


@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_13000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 13000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(13000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)


@pytest.mark.performance
@pytest.mark.merge_sort
def test_insertion_sort_unsorted_random_list_15000_items(benchmark, merge_sort):
    """
    Tests benchmark of merge sort on a 15000 item unsorted list
    """
    # Arrange
    lst = help_functions.generate_random_list(15000, 100000)

    # Act
    result = benchmark(merge_sort.merge_sort, lst)

    # Assert
    assert result == sorted(lst)