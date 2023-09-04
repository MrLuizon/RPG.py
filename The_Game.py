import os
import random
import time

def char_creation():
    ask_if_new_player()
    
# check if a given answer is within the list of possible answers.
def check_if_in_options(var1, options):
    try:
        var1 = int(var1)
        if var1 in options:
            return True
        else:
            return False
    except:
        return False
    
# Check if the given player name already exists in the player list.
def check_player_name_in_names(name):
    try:
        file.open('Python\Game.py\char_names.txt', 'x')
        file.close()
    except:
        pass
    
    with open('Python\Game.py\char_names.txt', 'r') as file:
            names = file.read()
            if name in names:
                return True             
            else: 
                return False    
    
#Sees if the player is a new player, loops unitl (1)YES or (2)NO. Return 1 or 2
def ask_if_new_player(): 
    put = input("Are you a new player?\n(1) - YES  (2) - NO\n> ")
    print()
    options = (1,2)
    if check_if_in_options(put, options):
        put = int(put)
        is_new_player(put)
        return put

    else:
        print("That is not one of the options")
        ask_if_new_player()

# If "YES" (is a new player) calls new_player_into_messege. If "NO" (is not new player) ask for char name: 
    # If char name exists, call begin(player_name). If doesn't exists ask if wanna create new char with that name: 
        # If YES(Want to create new char) call get_new_player_name. if NO(Don't wanna create new char) starts again
def is_new_player(put):
    if put == 1:
        new_player_intro_messege()
    else:
        player_name = input(("What is your character's name?\n> ")).strip()
        print()
        if check_player_name_in_names(player_name):
            print("I found you!")
            begin(player_name)
        else: 
            print(f"There is no character called {player_name}")
            create = input("Would you like to create a new one?\n(1) - YES (2) - NO\n> ")
            opt = (1,2)
            check_if_in_options(create, opt)
            if check_if_in_options:
                int(create)
                if create == 1:
                    get_new_player_name()
                else:
                    print("\nThen let's try again...\n")
                    ask_if_new_player()

# If new player, shows the intro, explain how game works and calls ask_if_understand_how_to_play.
def new_player_intro_messege():
    print("Hello new adventurer!")
    print("Welcome to THE GAME.py")
    print("Are you ready for this new and exciting adventure?")
    print("This is a procedural RPG.")
    print("I will tell you what is happening and you will chose one of the option I give by inputting it's number.")
    ask_if_understand_how_to_play()

# Loops until "YES" (Understand). Calls get_new_player_name. 
def ask_if_understand_how_to_play():
    start = 0
    while start != 1:
        start = input("Do you understand?\n(1) - YES  (2) - NO\n> ")
        options = (1,2)
        if check_if_in_options(start, options):
            start = int(start)            
            print()
        else:
            print("Something wrong with your input")
            ask_if_understand_how_to_play()
            
        if start == 1:
            print("Great!")
            get_new_player_name()
        elif start == 2:
            print("I will explain again...")
            print("This is a procedural RPG.")
            print("As the game progresses I will tell you what is happening with your charachter.")
            print("I will then give you option as to what you want to do/how you want to react.")
            print("You will then chose one of the option I give by inputting it's number.")
            print("The quistion below is an example of how to play. Type '1' for YES or '2' for NO.")
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
        
    if check_player_name_in_names(player_name):
        print(f"This name already exists. Would you like to play as {player_name} ?")
        play_as = input("(1) - YES (2) - NO\n> ")
        print()
        options = (1,2)
        
        if check_if_in_options(play_as, options):
            play_as = int(play_as)
        else:
            print("That is not one of the options")
            
        if play_as == 1:
            begin(player_name)
        else: 
            print("Then you will have to choose a different name!")
            get_new_player_name()
    else:
        print(f'Its very nice to meet you {player_name}')
        with open('Python\Game.py\char_names.txt', 'a+') as file:
            file.write(f'\n{player_name}')
        create_new_char_info_file(player_name)
    begin(player_name)

# Ask de player for a race for a new character
def get_player_race():
    race = input("What will be your character's race?\n(1)-Human (2)-Orc (3)-Elf (4)-Dwarf\n> ")
    print()
    options = (1,2,3,4)
    if check_if_in_options(race,options):
        pass
    else:
        print("That is not one of the options.")
        get_player_race()

    if race == "1":
        race = "human"
    elif race == "2":
        race = "orc"
    elif race == "3":
        race = "elf"
    elif race == "4":
        race = "dwarf"
    return race

# Ask de player for a classe for a new character
def get_player_cls():
    cls = input("And what will be your class?\n(1)-Tank (2)-Mage (3)-Archer (4)-Assassin (5)-Summoner\n> ")
    pass
    options = (1,2,3,4,5)
    if check_if_in_options(cls,options):
        print("ok")
    else:
        print("That is not one of the options.")
        get_player_cls()

    if cls == "1":
        cls = "tank"
    elif cls == "2":
        cls = "mage"
    elif cls == "3":
        cls = "archer"
    elif cls == "4":
        cls = "assassin"
    elif cls == "5":
        cls = "summoner"
    return cls

# Creates a .txt file for a new character with it's info like: Name, Level, Exp, Class and Race.
def create_new_char_info_file(name):
    with open(f'Python\Game.py\{name}_info.txt', 'w') as file:
        file.write(f"name = {name}\nlevel = 0\nexp = 0\nrace = {get_player_race()}\nclass = {get_player_cls()}")

#the begining of the game. It all starts here.
def begin(player_name):
    print(f"Let's Begin {player_name}")
    print()
    game_end()
   
#A tragic ending to this uncomplete game.
def game_end():
    time.sleep(2)
    print("This is as far as the games goes for now...")
    print("Stay tuned for more content!")
    print("Thank you for playing THE GAME.py!")
    exit()



char_creation()