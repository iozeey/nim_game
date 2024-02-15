#! /usr/local/bin/python3

import random
import pdb;

def show_Print(list):
    print(list)

def recursive_sort(list):
    print(list)
    if int(len(list)) == 2:
        if(list[0] > list[1]):
            return [list[1], list[0]]
        return list
    
    shrink_list =  list[0 : len(list) - 2]
    sorted = recursive_sort(shrink_list)
    print(list)
    

def sort4(a1,a2,a3,a4):    
    list  = [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11, 5, 18, 2, 10]
    # list = [random.randint(1,20) for i in range(20)]
    # [a1,a2,a3,a4]
    temp_list = recursive_sort(list)
    # do using recursion
    # for p_index, parent_item in enumerate(list):
    #     for c_index, current in enumerate(list):
    #         if(p_index != c_index):
    #             minimum = min(parent_item,current)
    #             print("parent, child and min %s %s is %s" %(parent_item, current, minimum))
    #     # print(minimum)
    #     temp_list.append(minimum)
    return temp_list
    # min_1_2 = min(a1,a2)
    # min_1_2 = min(min_1_2,a3)

print(sort4(11,2,13,4));
# out put of recursive calls for stack variable
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11, 5, 18, 2, 10]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11, 5, 18]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20]
# [12, 2, 1, 13, 5, 18, 13, 20]
# [12, 2, 1, 13, 5, 18]
# [12, 2, 1, 13]
# [12, 2]
# [12, 2, 1, 13]
# [12, 2, 1, 13, 5, 18]
# [12, 2, 1, 13, 5, 18, 13, 20]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11, 5, 18]
# [12, 2, 1, 13, 5, 18, 13, 20, 18, 20, 6, 14, 17, 11, 16, 11, 5, 18, 2, 10]