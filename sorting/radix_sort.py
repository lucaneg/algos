import base_sorter as base

def radix(array): 
    comps = 0
    buckets = dict()
    cap = max(array)
    bound = 0
    while cap != 0:
        cap //= 10
        bound += 1
    
    for exp in range(bound):
        for i in range(len(array)):
            comps += 1
            idx = (array[i] // 10**exp) % 10
            if not idx in buckets:
                buckets[idx] = list()
            buckets[idx].append(array[i])
        print('Radixes for ' + str(exp) + 'th position: ' + str(buckets), flush = True)
        yield array, comps
            
        pos = 0
        for k in sorted(buckets):
            for i in range(len(buckets[k])):
                array[pos] = buckets[k][i]
                pos += 1
                yield array, comps
        buckets.clear()

array = base.provide_array()
base.display(array, "Radix Sort", radix(array))