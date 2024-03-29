#! /usr/local/bin/python3

import random

def merge(left,right):    
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # copy the rest
    result.extend(left[left_index: ])
    result.extend(right[right_index: ])

    return result

def recursively_divide(list):
    if(len(list)) <= 1:
        return list
    
    mid =  int(len(list) / 2)
    left =  list[0 : mid]
    right =  list[mid : ]

    left_list = recursively_divide(left)
    right_list = recursively_divide(right)

    return merge(left_list, right_list)

list = [random.randint(1,20) for i in range(20)]

print(recursively_divide(list));

