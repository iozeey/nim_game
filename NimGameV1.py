#! /usr/bin/python3

import random

# valid random number
def get_random_number():
    return random.randint(1,3)

def nim_best(n):
    legal_move = get_random_number()

    if legal_move % 4 == 0:
        nim_best(n)
    
    return legal_move

def nim_minimal():
    return 1

def nim(n):
    return random.choice(range(1, min(n,3)+1))

def nim_human(n):    
    taken = int(input("There are sticks %s. How many do you take? Enter your move: " %(n)))

    if  taken in range(1, min(n,3)+1):
        return taken
    
    print("Illegal")
 
# list of functions(players)
player_pool = [nim, nim_best, nim_human, nim_minimal]

# update list with player name (function name) and its function body
player_pool = { p.__name__:p for p in player_pool }

# manager
def select_players():
    players = []

    while len(players) < 2:
        print("Available players: %s " %(','.join(player_pool.keys())))
        p = input("Type your player name: ")
        if p not in player_pool.keys():
            print("Its not in the list. Please select again\n")
            continue
        players.append(p)
    
    print("Player %s begins, player %s, second player ", tuple(players))
    return players


# controller
def game():
    # Get input from user
    while True:
        sticks = int(input("Heap size? \n"))
        if sticks > 0 : break
    
    # Get who is going to play
    current, other = tuple(select_players())

    # Now run the game
    while sticks > 0 :

        print("Heap has %d sicks." %sticks)
        taken = player_pool[current](sticks)
        
        print("%s takes %d sticks.\n" %(current, taken))
        
        sticks -= taken
        
        current, other = other, current

    print("%s has lost." % current)

game()