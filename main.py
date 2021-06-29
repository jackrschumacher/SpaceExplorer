from intro import *

def game_start():
    global starcoin, water_amnt, food_amnt
    user_input = str(input("What would you like to do?"))
    alive = True

    if user_input == "Help" or user_input == "help" or user_input == "hlp":
                print('''
                List of Space Explorer Commands
                -Travel
                -Supplies
                -Buy Ship
                -Planet (Generate a list of planets)
                -Mine
                ''')
    while alive == True:
        
        if user_input == "Travel" or user_input == "travel" or user_input == "trvl":
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
            elif trvl_to == "Earth" or trvl_to == "earth":
                print("Your charachter Begins on Earth...")
                user_input = str(input("Would You like to replenish your ship, shop for a new one, or more"))
                if trvl_to == "skip" or trvl_to == "Skip":
                    print("You have chosen to skip")
                elif trvl_to == "rep" or user_input == "Rep" or user_input == "Replenish" or user_input == "replinish":
                    print("=========")
                    print("You have chosen to replenish your ship")
                    print("=========")
                elif user_input == "shop" or user_input == "Shop" or user_input == "shp" or user_input == "Shp":
                    print("=========")
                    print("You have chosen to shop for supplies.")
                    print("=========")
                    print("Type list for a list of store items")
                    starcoin = 1500
                    print("You have,",starcoin,"StarCoin")
                    item = str(input("What Item do you wish to shop for: "))
                    while quit == False and starcoin > 100:
                        if item == "list" or item == "List" or item == "lst" or item == "Lst":
                            print('''
                            List of Store items
                            =========
                            -Water
                            -Food
                            -HyperFuel
                            -Encoder
                            ''')
                            item = str(input("What Item do you wish to shop for: "))
                        elif item == "Water" or item == "water" or item == "wtr":
                            print("=========")
                            print("Water Costs 10 StarCoin")
                            water_amnt = int(input("How much water do you wish to buy:"))
                            print("You have chosen to buy:", water_amnt)
                            starcoin = starcoin - water_amnt * 10
                            print("You have:",starcoin,"Remaing")
                        elif item == "Food" or item == "food" or item == "fod":
                            print("=========")
                            print("Water cost 25 StarCoin per pound")
                            food_amnt = int(input("How much food you like purchase: "))
                            print("You have chosen to buy:", food_amnt)
                            starcoin = starcoin - food_amnt * 25
                            print("You have:",starcoin,"Remaing")
                            



                else:
                    print("y")
def main():
    intro()
    game_start()
