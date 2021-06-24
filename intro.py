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

user_input = str(input("What would you like to do?"))

if user_input == "Help" or user_input == "help" or user_input == "hlp":
    print('''
    List of Space Explorer Commands
    -Travel
    -Supplies
    -Buy Ship
    -Planet (Generate a list of planets)
    -Mine
    ''')


def main():
    intro()



main()    