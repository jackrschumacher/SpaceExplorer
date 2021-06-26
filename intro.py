import math
import time
from main import *
print('''
=========
SpaceExplorer
=========
''')

def intro():
    global user_name
    user_name = str(input("Please enter your username:"))
    print("Your username is:",user_name)

    print("You are the captian of a Nebula-Class starship known as the U.S.S. Endurance")
    print("=========")
    print("Your ship can travel at 2.1 Starspeed")
    print("=========")
    print("Type help for a list of game commands, planets, etc.")



def main():
    intro()
    game_start()



main()    