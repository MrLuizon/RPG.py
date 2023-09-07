import os
import random
import time



class Human:
    def __init__(self):
        strength = 3
        agility = 3
        intelligence = 5
        vitality = 3
        
class Orc:
    def __init__(self):
        strength = 5
        agility = 2
        intelligence = 2
        vitality = 5
        
class Elf:
    def __init__(self):
        strength = 2
        agility = 5
        intelligence = 4
        vitality = 3
        
class Dwarf:
    def __init__(self):
        strength = 4
        agility = 2
        intelligence = 3
        vitality = 5

class Tank:
    pass
class Mage:
    pass
class Archer:
    pass
class Assassin:
    pass
class Summoner:
    pass


def check_if_in_options(var1, options):# check if a given answer (var1) is within the list of possible answers(options). Return True or False
    try:
        var1 = int(var1)
        if var1 in options:
            return True
        else:
            return False
    except:
        return False

def check_player_name_in_names(name):# Check if the given player name already exists in the player list (char_names.txt). Return True or False
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

def ask_if_new_player(): #Ask if is a new player, loops unitl (1)YES or (2)NO. Return 1 or 2
    put = input("Are you a new player?\n(1)-YES  (2)-NO\n> ")
    print()
    options = (1,2)
    if check_if_in_options(put, options):
        put = int(put)
        is_new_player(put)
        return put
    else:
        print("That is not one of the options")
        ask_if_new_player()

def is_new_player(put):# Get's the answer if is new player and acts on it.
    if put == 1:        #If "YES" (Is new player)
        new_player_intro_messege()
        ask_if_understand_how_to_play()
    else:               #If "NO" (Is NOT new player) 
        player_name = input(("What is your character's name?\n> ")).strip().title()# Ask for the existing char's name
        print()
        if check_player_name_in_names(player_name): #If char name already exists 
            print("I found you!")
            begin(player_name)
        else:                                       #Didn't find the char name (Doesn't exist)
            print(f"There is no character called {player_name}")
            create = input("Would you like to create a new one?\n(1)-YES (2)-NO\n> ") # Ask if want to create new char
            opt = (1,2)
            check_if_in_options(create, opt)
            if check_if_in_options:
                int(create)
                if create == 1:# If YES (Want to create new char)
                    char_creation()
                else:          # If NO (Does't want to create new char) 
                    print("\nThen let's try again...\n")
                    ask_if_new_player()

def char_creation():# Creates a new plyable char
    def get_new_player_name(): #Ask for new char name
            player_name = input(("What should I call you?\nYour name: ")).strip().title()
            print()
            
            while player_name == "":
                player_name = input("Please, chose a name: ").strip()
                
            if check_player_name_in_names(player_name):
                print(f"This name already exists. Would you like to play as {player_name} ?")
                play_as = input("(1)-YES (2)-NO\n> ")
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

    def get_new_player_race():#Ask for new char race
        race = input("What will be your character's race?\n(1)-Human (2)-Orc (3)-Elf (4)-Dwarf\n> ")
        print()
        options = (1,2,3,4)
        if check_if_in_options(race,options):
            pass
        else:
            print("That is not one of the options.")
            get_new_player_race()

        if race == "1":
            race = "Human"
        elif race == "2":
            race = "Orc"
        elif race == "3":
            race = "Elf"
        elif race == "4":
            race = "Dwarf"
        return race
    
    def get_new_player_cls():#Ask for new char class
        cls = input("And what will be your class?\n(1)-Tank (2)-Mage (3)-Archer (4)-Assassin (5)-Summoner\n> ")
        pass
        options = (1,2,3,4,5)
        if check_if_in_options(cls,options):
            pass
        else:
            print("That is not one of the options.")
            get_new_player_cls()

        if cls == "1":
            cls = "Tank"
        elif cls == "2":
            cls = "Mage"
        elif cls == "3":
            cls = "Archer"
        elif cls == "4":
            cls = "Assassin"
        elif cls == "5":
            cls = "Summoner"
        return cls
    
    def create_new_char_info_file(name):#Creates a txt file with the char's info
        with open(f'Python\Game.py\{name}_info.txt', 'w') as file:
            file.write(f"name={name},level=0,exp=0,race={get_new_player_race()},class={get_new_player_cls()}")

    get_new_player_name()

def new_player_intro_messege():# Intro messege for new users to explain how the game works
    print("Hello new adventurer!")
    print("Welcome to THE GAME.py")
    print("Are you ready for this new and exciting adventure?")
    print("This is a procedural RPG.")
    print("I will tell you what is happening and you will chose one of the option I give by inputting it's number.")

def end_game_messege():# Messege to display whene the game ends
    print("This is as far as the games goes for now...")
    print("Stay tuned for more content!")
    print("Thank you for playing THE GAME.py!")

def new_player():# 
    pass

def begin(player_name):# The begining of the game. It all starts here.
    print(f"Let's Begin {player_name}")
    print()
    game_end()

def game_end():# A tragic ending to this uncomplete game.
    end_game_messege()
    time.sleep(2)
    exit()

def ask_if_understand_how_to_play():# Gives more detailed explanation (If needed). Loops until "YES" (Understand). Calls char_creation(). 
    start = 0
    while start != 1:
        start = input("Do you understand?\n(1)-YES  (2)-NO\n> ")
        options = (1,2)
        if check_if_in_options(start, options):
            start = int(start)            
            print()
        else:
            print("Something wrong with your input")
            ask_if_understand_how_to_play()
            
        if start == 1:
            print("Great!")
            char_creation()
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
            print("You can only input one of the options I give you. In this case, (1)fr YES or (2)fr NO")
            continue



ask_if_new_player()
