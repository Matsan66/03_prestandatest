import pytest

@pytest.mark.unit
@pytest.mark.insertion_sort
def test_insertion_sort_unsorted_list(insertion_sort):
    """
    Tests that the insertion_sort function correctly sorts an unsorted list
    """
    #Arrange
    lst =  [10, 8, 6, 4, 2, 0]

    #Act
    result = insertion_sort.insertion_sort(lst)

    #Assert
    assert result == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
@pytest.mark.insertion_sort
def test_insertion_sort_sorted_list(insertion_sort):
    """
    Tests that the insertion_sort function correctly handles a sorted list
    """
    # Arrange
    lst = [0, 2, 4, 6, 8, 10]

    # Act
    result = insertion_sort.insertion_sort(lst)

    # Assert
    assert result == [0, 2, 4, 6, 8, 10]


@pytest.mark.unit
@pytest.mark.insertion_sort
def test_insertion_sort_single_element_list(insertion_sort):
    """
    Tests that the insertion_sort function correctly handles a single element list
    """
    #Arrange
    lst =  [10]

    #Act
    result = insertion_sort.insertion_sort(lst)

    #Assert
    assert result == [10]


@pytest.mark.unit
@pytest.mark.insertion_sort
def test_insertion_sort_empty_element_list(insertion_sort):
    """
    Tests that the insertion_sort function correctly handles an empty list
    """
    #Arrange
    lst =  []

    #Act
    result = insertion_sort.insertion_sort(lst)

    #Assert
    assert result == []



