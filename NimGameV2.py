import random

def nim_minimal():
    return 1

# valid random number
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

    if legal_move % 4 == 0 or legal_move > left_sticks:
        nim_best(left_sticks)
    
    return legal_move

def nim_human(left_sticks):    
    while True:
        move = int(input("Enter your move: "))
    
        if  move > 0 and move <= 3 and move <= left_sticks:
            return move
        else:
            continue
            # this recursion is faulty when it returns then the caller points receives the old results i think due to stack clearing strategy
            # nim_human(left_sticks)
        
def get_player_names(choice):
    if choice == 1:
        return [input("Player 1 Name: "), input("Player 2 Name: ")]
    elif choice == 2:
        return ["Computer", input("Player 2 Name: ")]
    else:
        return ["Computer 1", "Computer 2"]
    
def is_over(heap):
    return len(heap) == 0

def execute_on_heap(heap, size):
    return heap[size:]

def get_moves(left_sticks, choice):
    if choice == 1:
        return nim_human(left_sticks)
    elif choice == 2:
        return nim_human(left_sticks) 
    elif choice == 3:
        return nim_best(left_sticks)

def game_controller():
    # via list comprehension
    heap = [1 for x in range(int(input("Enter Heap Size: ")))]
    # prompt
    print("Select corresponding digit for\n")
    print("1 for Human vs Human\n")
    print("2 for Computer vs Human\n")
    print("3 for Computer vs Computer\n")

    choice = int(input("Enter Your choice: "))
    players = get_player_names(choice)
    
    # who is playing currently
    current_turn = 0
    
    # run game
    while True:
        if len(heap) > 0:
            print("Total sticks %s and %s's turn %s" %(len(heap) , players[current_turn % 2], current_turn))
            
            if choice == 2 and (current_turn % 2) == 0:
                move = get_moves(len(heap), 3)
            else:
                move = get_moves(len(heap), choice)
            
            print("Sticks taken: %s" %move)
            
            heap = execute_on_heap(heap, move)
            
            print("Left sticks are: %s" %len(heap))

            if is_over(heap):  
                print("Hurry!! {} has WON!!!".format(players[current_turn % 2]))     
                return  
            # for next player
            current_turn += 1

print(game_controller())