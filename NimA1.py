import random
heap = [1,1,1,1,1,1,1,1,1,1,1]

# produce legal move
def nim(left_sticks):    
    if len(left_sticks) > 0:
        return random.randint(1,3)

print(nim(heap))