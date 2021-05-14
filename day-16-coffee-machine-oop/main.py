from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

def main():
    """connect all functionalies together to function as coffee machine"""
    is_machine_on = True
    print(logo)
    menue = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while is_machine_on:
        #TODO: print intro         
        user_input = input(f"What would you like? ({menue.get_items()}): ").lower()

        #TODO: off,  to exit
        if user_input == 'off':
            coffee_maker.off()
        elif user_input == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            user_drink = menue.find_drink(user_input)
            if user_drink:
                if coffee_maker.is_resource_sufficient(user_drink):
                    cost = user_drink.cost
                    if money_machine.make_payment(cost):
                        coffee_maker.make_coffee(user_drink)
            else:
                print("unknown option!")


if __name__ == "__main__":
    main()