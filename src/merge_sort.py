class MergeSort:
    """
    Class representing the merge sort algorithm
    """
    def merge_sort(self, lst):
        """
        Sorts the given list using merge sort algorithm
        :param lst: The given list
        :return: list <= 1 result from merge sort algorithm
        """
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])

        return self.merge(left, right)


    def merge(self, left, right):
        """
        Merges the given lists into one list
        :param left: First list to merge
        :param right: Second list to merge
        :return: The merged lists
        """
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
