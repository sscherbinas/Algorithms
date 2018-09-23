import time

from Bank import Bank
from QuickSort import QuickSort
from SelectionSort import SelectionSort

if __name__ == "__main__":
    banks_list = []
    name_pos = 0
    clients_pos = 1
    credits_pos = 2
    file = open('banks_list.csv')
    for line in file:
        values = line.split(',')
        bank = Bank(values[name_pos], int(values[clients_pos]), int(values[credits_pos][:-1]))
        banks_list.append(bank)

    print("Selection sort:")
    selection_sort = SelectionSort(banks_list)
    start_time = time.clock()
    selection_sort.selection_sort()
    print("Time: " + str(time.clock() - start_time))
    for bank in banks_list:
        print(bank)

    print("\nQUICK sort:")
    quick_sort = QuickSort(banks_list)
    start_time = time.clock()
    quick_sort.quick_sort()
    print("Time: " + str(time.clock() - start_time))
    for bank in banks_list:
        print(bank)