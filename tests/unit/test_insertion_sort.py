import pytest

@pytest.mark.unit
def test_insertion_sort_unsorted_list(insertion_sort):
    """
    Tests insertion sort on unsorted list
    """
    #Arrange
    lst =  [10, 8, 6, 4, 2, 0]

    #Act
    result = insertion_sort.insertion_sort(lst)

    #Assert
    assert result == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
def test_insertion_sort_sorted_list(insertion_sort):
    """
    Tests insertion sort on sorted list
    """
    # Arrange
    lst = [0, 2, 4, 6, 8, 10]

    # Act
    result = insertion_sort.insertion_sort(lst)

    # Assert
    assert result == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
def test_insertion_sort_single_element_list(insertion_sort):
    """
    Tests insertion sort on single element list
    """
    #Arrange
    lst =  [10]

    #Act
    result = insertion_sort.insertion_sort(lst)

    #Assert
    assert result == [10]


@pytest.mark.unit
def test_insertion_sort_empty_element_list(insertion_sort):
    """
    Tests insertion sort on empty list
    """
    #Arrange
    lst =  []

    #Act
    result = insertion_sort.insertion_sort(lst)

    #Assert
    assert result == []



