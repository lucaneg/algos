import base_sorter as base

def bubble(array): 
    swap = True
    bound = len(array) - 1
    comps = 0
    while swap:
        swap = False
        for i in range(bound):
            comps += 1
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
                yield array, comps
        bound -= 1

array = base.provide_array()
base.display(array, "Bubble Sort", bubble(array))