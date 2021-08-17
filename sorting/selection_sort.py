import base_sorter as base

def selection(array): 
    start = 0
    comps = 0
    for i in range(len(array) - 1):
        minIdx = start
        for idx in range(start, len(array)):
            comps += 1
            if array[idx] < array[minIdx]:
                minIdx = idx
        array[start], array[minIdx] = array[minIdx], array[start]
        start += 1
        yield array, comps

array = base.provide_array()
base.display(array, "Selection Sort", selection(array))