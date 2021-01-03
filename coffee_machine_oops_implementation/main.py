from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Objects and boolean operators
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_working = True


while is_working:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice.lower() == "off":
        is_working = False
    else:
        user_order = menu.find_drink(user_choice)
        is_available = coffee_maker.is_resource_sufficient(user_order)
        if coffee_maker.is_resource_sufficient(user_order) and money_machine.make_payment(user_order.cost):
            coffee_maker.make_coffee(user_order)
