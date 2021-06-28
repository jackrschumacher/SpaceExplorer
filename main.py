from intro import *

def game_start():
    user_input = str(input("What would you like to do?"))
    alive = True

    while alive == True:
        if user_input == "Help" or user_input == "help" or user_input == "hlp":
            print('''
            List of Space Explorer Commands
            -Travel
            -Supplies
            -Buy Ship
            -Planet (Generate a list of planets)
            -Mine
            ''')
        elif user_input == "Travel" or user_input == "travel" or user_input == "trvl":
            print("You have chosen to travel")
            trvl_to = str(input("Where do you wish to travel? (Type List for a list of avaliable planets"))
            if trvl_to == "list" or trvl_to == "List" or trvl_to == "lst":
                print('''
                Listing of Possible Space Explorer Planets:
                -Earth (Base Planet)
                -Mars
                -The Moon
                -Pluto
                -Venus(Not explorable by humans-probes needed)
                -Jupiter(Not explorable by humans-probes needed)
                
                ''')
                start_planet = "Earth"
            elif user_input == "Earth" or user_input == "earth":
                print("Your charachter Begins on Earth...")
                user_input = str(input("Would You like to replenish your ship, shop for a new one, or more"))
                if user_input == "skip" or user_input == "Skip":
                    print("You have chosen to skip")
                elif user_input == "rep" or user_input == "Rep" or user_input == "Replenish" or user_input == "replinish":
                    print("=========")
                    print("You have chosen to replenish your ship")
                    print("=========")
                elif user_input == "shop" or user_input == "Shop" or user_input == "shp" or user_input == "Shp":
                    print("=========")
                    print("You have chosen to shop for supplies.")
                    print("=========")
                    item = str(input("What Item do you wish to shop for"))
            else:
                print("y")
def main():
    intro()
    game_start()
