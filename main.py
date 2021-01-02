#TODO: 1 check resources sufficient to make drink order.
#TODO: 2 print report of the resources available
#TODO: 3 check whether the transaction successful or not
#TODO: 4 return the refunded money after successful transaction

import os
from coffee_data import MENU,resources,profit

def clear():
    os.system('clear')


def update_resources(coffee_type,Money):
    resources['water'] -= coffee_type['ingredients']['water']
    resources['milk'] -= coffee_type['ingredients']['milk']
    resources['coffee'] -= coffee_type['ingredients']['coffee']
    Money += coffee_type['cost']
    global profit
    profit += Money


def check_report(coffee_type):
    if resources['water'] >= coffee_type['ingredients']['water']:
        if resources['milk'] >= coffee_type['ingredients']['milk']:
            if resources['coffee']>=coffee_type['ingredients']['coffee']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def process_coins():
    print("Please Insert Coins\n")
    total = int(input("how many quarter?: "))*0.25
    total += int(input("how many dime?: "))*0.1
    total += int(input("how many nickle?: "))*0.05
    total += int(input("how many pennies?: "))*0.01
    return total
def coffee(coffee_type,total):
    if MENU[coffee_type]["cost"] <= total:
        total = total - MENU[coffee_type]["cost"]

        if total > 0:
            print(f"Here is ${round(total,2)} in change.")
        print(f"Here is your {coffee_type} Enjoy !")
    else:
        print("Sorry that's not enough money.Money Refunded.")

is_working = True
while is_working:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        is_working = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        key = MENU[user_choice]
        user_deposit  = process_coins()
        is_available = check_report(key)
        update_resources(key,profit)
        if is_available:
            coffee(user_choice,user_deposit)
            #clear()




