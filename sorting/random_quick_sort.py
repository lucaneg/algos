import base_sorter as base
import random

def quick(array): 
    wrapper = base.CompsWrapper()
    yield from quick_aux(array, wrapper, 0, len(array) - 1)
  
def quick_aux(array, wrapper, low, high):
    if len(array) == 1:
        yield array, wrapper.comps
    else:
        wrapper.comps += 1
        if low < high:
            partition_index_wrapper = base.CompsWrapper()
            yield from partition(array, partition_index_wrapper, wrapper, low, high)
            yield from quick_aux(array, wrapper, low, partition_index_wrapper.comps - 1)
            yield from quick_aux(array, wrapper, partition_index_wrapper.comps + 1, high)

def partition(array, partition_index_wrapper, wrapper, low, high):
    rand = random.randrange(low, high)
    array[high], array[rand] = array[rand], array[high]
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        wrapper.comps += 1
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            yield array, wrapper.comps
    array[i + 1], array[high] = array[high], array[i + 1]
    yield array, wrapper.comps
    partition_index_wrapper.comps = i + 1

array = base.provide_array()
base.display(array, "Random Quick Sort", quick(array))