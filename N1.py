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
    taken = int(input("There are sticks %s. How many do you take? Enter your move: " % n))

    if  taken in range(1, min(n,3)+1):
        return taken
    
    print("Illegal")
 
# list of functions/players
player_pool = [nim_minimal, nim, nim_best, nim_human]

player_pool = { p.__name__:p for p in player_pool }

# manager
def select_players():
    players = []
    
    while len(players) < 2:
        print("These are the players: %s ".join(player_pool.keys()))
        p = input("Name one: ")
        if p not in player_pool.keys():
            print("not a valid player. select again")
            continue
        players.append(p)
    
    print("Player %s begins, player %s, second player ", tuple(players))
    return players


# controller
def game():
    # Get input from user
    while True:
        n = int(input("Heap size? \n"))
        if n > 0 : break
    
    # get who is going to play
    current, other = tuple(select_players())

    # now run the game
    while n > 0 :

        print("Heap has %d sicks." %n)
        taken = player_pool[current](n)
        
        print("%s takes %d sticks.\n" %(current, taken))
        
        n -= taken
        
        current, other = other, current

    print("%s has lost." % current)

game()