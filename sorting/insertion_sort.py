import base_sorter as base

def insertion(array): 
    comps = 0
    for i in range(1, len(array)):
        pos = i - 1
        comps += 1
        while array[pos] > array[i] and pos >= 0:
            comps += 1
            pos -= 1
        pivot = array[i]
        array.pop(i)
        array.insert(pos + 1, pivot)
        yield array, comps

array = base.provide_array()
base.display(array, "Insertion Sort", insertion(array))