def count(list):
    list.pop()
    
    if len(list) == 0:
        return 1
    
    return  1 + count(list)

print(count([1,2,3,4,5]))