import random
heap = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def get_random_number():
    return random.randint(1,3)

# produce legal move
def nim(left_sticks):    
    if len(left_sticks) > 0:
        return get_random_number()

# produce legal optimal move
    # find out the best move if user take they will wins
    # After doing some exercise we found if a player(1 or 2) see 4 bars left on the second last step(before end of game) then the last player will win as he will have sticks(which is winning rule)
def nim_best(left_sticks):
    legal_move = get_random_number()

    if legal_move % 4 == 0:
        nim_best(left_sticks)
    return legal_move

def nim_human(left_sticks):
    
    while True:
        move = int(input("Enter your move"))

        if  move < len(left_sticks):
            return move
        

print(nim_human(heap))