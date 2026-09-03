import pytest

@pytest.mark.unit
@pytest.mark.merge_sort
def test_merge_sort_unsorted_list(merge_sort):
    """
    Tests that the merge_sort function correctly sorts an unsorted list
    """
    # Arrange
    lst = [10, 8, 6, 4, 2, 0]

    # Act
    result = merge_sort.merge_sort(lst)

    # Assert
    assert result == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
@pytest.mark.merge_sort
def test_merge_sort_sorted_list(merge_sort):
    """
     Tests that the merge_sort function handles a sorted list
    """
    # Arrange
    lst = [0, 2, 4, 6, 8, 10]

    # Act
    result = merge_sort.merge_sort(lst)

    # Assert
    assert result == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
@pytest.mark.merge_sort
def test_merge_sort_single_element_list(merge_sort):
    """
    Tests that the merge_sort function handles a list with a single element
    """
    # Arrange
    lst = [10]

    # Act
    result = merge_sort.merge_sort(lst)

    # Assert
    assert result == [10]


@pytest.mark.unit
@pytest.mark.merge_sort
def test_merge_sort_empty_list(merge_sort):
    """
    Tests that the merge_sort function handles an empty list
    """

    # Arrange
    lst = []

    # Act
    result = merge_sort.merge_sort(lst)

    # Assert
    assert result == []