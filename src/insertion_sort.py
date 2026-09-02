class InsertionSort:
    """
    Class representing the insertion sort algorithm
    """

    def insertion_sort(self, lst):
        """
        Sorts a given list using the insertion sort algorithm
        :param lst: The list to sort
        :return: The sorted list
        """
        result = []
        for item in lst:
            inserted = False
            index = 0
            while not inserted and index < len(result):
                if item < result[index]:
                    result.insert(index, item)
                    inserted = True
                index += 1
            if not inserted:
                result.append(item)
        return result
