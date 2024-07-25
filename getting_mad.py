import sys
def getting_mad(arr):
    mad = sys.maxsize
    for number in arr:
        curr_num_index = arr.index(number)
        for i in range(len(arr)):
            if i == curr_num_index:
                continue
            curr_mad = abs(number - arr[i])
            if curr_mad < mad:
                mad = curr_mad
    return mad

print(getting_mad([-10, 0, -3, 1]))