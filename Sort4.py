#! /usr/local/bin/python3

def sort4(a1,a2,a3,a4):    
    # simple logic for sorting all four will go here

    # find min of first two
    # a2 is min
    if a1 < a2:
        a1,a2 = a2,a1

    # find min of last two
    # a4 is min
    if a3 < a4:
        a3,a4 = a4,a3

    # now a2 and a4 are min now find min of these two
    # a4 is min of all four
    if a2 < a4:
        a2,a4 = a4,a2

    # now find out second last min in all four elements    

    # compare any remaining two and find min
    # a3 is min
    if a2 < a3:
        a2,a3 = a3,a2
    
    # now compare result(a3) with last(a1) elem
    
    # a3 is third last min out of four
    if a1 < a3:
        a1,a3 = a3,a1

    # fourth last
    if a1 < a2:
        a1,a2 = a2,a1
    
    return a4,a3,a2,a1

print(sort4(11,2,13,4));
print(sort4(1,0,100,4));
