import random

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

    if legal_move % 4 == 0:
        nim_best(left_sticks)
    return legal_move

def nim_human():    
    move = int(input("Enter your move: "))

    if  move > 0 and move <= 3:
        return move
    else:
        nim_human()
        
def get_player_name_human():
  return [input("Player 1 Name: "), input("Player 2 Name: ")]

def is_over(heap):
    return len(heap) == 0

def execute_on_heap(heap, size):
    return heap[size:]

def game_controller():
    # via list comprehension
    heap = [1 for x in range(int(input("Enter Heap Size: ")))]
    # prompt
    print("Select corresponding digit for\n")
    print("1 for Human vs Human\n")
    print("2 for Computer vs Human\n")
    print("3 for Computer vs Computer\n")

    choice = int(input("Enter Your choice: "))
    players = get_player_name_human()
    
    # who is playing currently
    current_turn = 0
    
    # run game
    while True:
        if choice == 1 and len(heap) > 0:
            print(players[current_turn % 2]+"'s turn ")
            move = nim_human()
            heap = execute_on_heap(heap, move)
            
            if is_over(heap):  
                print(players[current_turn % 2]+" won!!!")     
                return  
            # for next player
            current_turn += 1

        print(heap)

print(game_controller())