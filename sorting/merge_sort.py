import base_sorter as base

def merge(array):
    wrapper = base.CompsWrapper()
    yield from merge_aux(array, wrapper, 0, len(array) - 1)

def merge_aux(array, wrapper, lb, ub):
    if ub <= lb:
        return
    elif lb < ub:    
        mid = (lb + ub) // 2
        yield from merge_aux(array, wrapper, lb, mid)
        yield from merge_aux(array, wrapper, mid + 1, ub)
        yield from join(array, wrapper, lb, mid, ub)
        yield array, wrapper.comps

def join(array, wrapper, lb, mid, ub):
    new = []
    i = lb
    j = mid + 1
    while i <= mid and j <= ub:
        wrapper.comps += 1
        if array[i] < array[j]:       
            new.append(array[i])
            i += 1
        else:
            new.append(array[j])
            j += 1
            
    if i > mid:
        while j <= ub:
            new.append(array[j])
            j += 1
    else:
        while i <= mid:
            new.append(array[i])
            i += 1
    for i, val in enumerate(new):
        array[lb + i] = val
        yield array, wrapper.comps
    
array = base.provide_array()
base.display(array, "Merge Sort", merge(array))