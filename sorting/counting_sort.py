import base_sorter as base

def counting(array): 
    comps = 0
    counter = dict()
    for i in range(len(array)):
        comps += 1
        if array[i] in counter:
            counter[array[i]] += 1
        else:
            counter[array[i]] = 1
        print('Counting: ' + str(counter), flush = True)
        yield array, comps
            
    pos = 0
    for k in sorted(counter):
        for i in range(counter[k]):
            array[pos] = k
            pos += 1
            yield array, comps

array = base.provide_array()
base.display(array, "Counting Sort", counting(array))