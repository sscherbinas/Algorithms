def swap(list, i, min_index):
    tmp = list[i]
    list[i] = list[min_index]
    list[min_index] = tmp
    return list


class SelectionSort:
    list_to_sort = []
    swaps = 0
    comparisons = 0

    def __init__(self, list):
        self.list_to_sort = list

    def selection_sort(self):
        n = len(self.list_to_sort)
        for i in range(0, n - 1):
            min_index = i
            for j in range(i + 1, n):
                if self.list_to_sort[j].clients_number < self.list_to_sort[min_index].clients_number:
                    min_index = j
                    self.comparisons += 1
            self.list_to_sort = swap(self.list_to_sort, i, min_index)
            self.swaps += 1

        print("Comparisons: " + str(self.comparisons))
        print("Swaps: " + str(self.swaps))
        return self.list_to_sort
