import os
import random
import time

def start_game():
    check_if_new_player()
    

def check_if_in_options(var1, options):
    try:
        var1 = int(var1)
        if var1 in options:
            return True
        else:
            return False
    except:
        return False
    
def check_player_name_in_names(name):
    with open('Python\Game.py\char_names.txt', 'r') as file:
            names = file.read()
            if name in names:
                return True             
            else: 
                return False    
    
#Sees if the player is a new player, if new calls "new_player_intro_messege", if not new search "char_names" file for the player name, if found, stars game and reads infos.
def check_if_new_player(): 
    put = input("Are you a new player?\n(1) - YES  (2) - NO\n> ")
    print()
    options = (1,2)
    if check_if_in_options(put, options):
        put = int(put)
    else:
        print("Something wrong with your input")
        check_if_new_player()
        
    if put == 1:
        new_player_intro_messege()
    else:
        player_name = input(("What is your character's name?\n> ")).strip()
        print()
        if check_player_name_in_names(player_name):
            print("I found you!")
            begin(player_name)
        else: 
            print(f"There is no {player_name}")
            create = input("Would you like to create a new one?\n(1) - YES (2) - NO\n> ")
            opt = (1,2)
            check_if_in_options(create, opt)
            if check_if_in_options:
                int(create)
                if create == 1:
                    get_new_player_name()
                else:
                    print("Then let's try again...\n")
                    check_if_new_player()

#If the player is new, shows the intro and calls function to get his name.
def new_player_intro_messege():
    print("Hello new adventurer!")
    print("Welcome to THE GAME.py")
    print("Are you ready for this new and exciting adventure?")
    print("This is a procedural RPG.")
    print("I will tell you what is happening and you will chose one of the option I give by inputting it's number.")
    new_player_start()

#If a new player, explains how game works.
def new_player_start():
    start = 0
    while start != 1:
        start = input("Do you understand?\n(1) - YES  (2) - NO\n> ")
        options = (1,2)
        if check_if_in_options(start, options):
            start = int(start)            
            print()
        else:
            print("Something wrong with your input")
            new_player_start()
            
        if start == 1:
            get_new_player_name()
            # with open('Python\Game.py\char_names.txt', 'a') as namelist:
            #     namelist.append()
        elif start == 2:
            print("I will explain again!")
            print("This is a procedural RPG.")
            print("I will tell you what is happening and you will chose one of the option I give by inputting it's number.")
            continue
        else:
            print("I think you didn't understand... ")
            print("You can only input one of the options I give you. In this case, (1) for YES or (2) for NO")
            continue
        
#gets the name of this new player
def get_new_player_name():
    player_name = input(("What should I call you?\nYour name: ")).strip()
    print()
    
    while player_name == "":
        player_name = input("Please, chose a name: ").strip()
        
    if check_player_name_in_names(player_name.upper()):
        print(f"This name already exists. Would you like to play as {player_name} ?")
        play_as = input("(1) - YES (2) - NO\n> ")
        print()
        options = (1,2)
        
        if check_if_in_options(play_as, options):
            play_as = int(play_as)
        
        if play_as == 1:
            begin(player_name)
        else: 
            print("Then you will have to choose a different name!")
            get_new_player_name()
    else:
        print(f'Its very nice to meet you {player_name}')
        with open('Python\Game.py\char_names.txt', 'a+') as file:
            file.write(f'\n{player_name}')
    begin(player_name)

#A tragic ending to this uncomplete game.
def game_end():
    time.sleep(2)
    print("This is as far as the games goes for now...")
    print("Stay tuned for more content!")
    print("Thank you for playing THE GAME.py!")
    exit()


#the begining of the game. It all starts here.
def begin(player_name):
    print(f"Let's Begin {player_name}")
    print()
    game_end()




start_game()