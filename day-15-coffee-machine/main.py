from art import logo
from data import MENU, resources

money = 0.00


#TODO: report, to print a report of all resources
def report(resources, money):
    """print a resources report"""

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


#TODO: check resources

def check_resources(resources, menue, drink):
    """Check for resources, returns true when enough resources"""
    enough_resources = True
    drink_water = menue[drink]['ingredients']['water']    
    drink_coffee = menue[drink]['ingredients']['coffee']

    if drink != 'espresso':
        drink_milk = menue[drink]['ingredients']['milk']
        if resources['milk'] < drink_milk:
            print("Sorry there is not enough milk.")
            enough_resources = False

    if resources['water'] < drink_water:
        print("Sorry there is not enough water.")
        enough_resources = False
    elif resources['coffee'] < drink_coffee:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    
    return enough_resources


#TODO: process coins
def process_money():
    """Takes Money from user and process it, returns full payment """

    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes    = int(input("how many dimes?: "))
    nickles  = int(input("how many nickles?: "))
    pennies  = int(input("how many pennies?: "))
    user_pay =  quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"You Paid {user_pay:.2f}")
    return user_pay


#TODO: check transaction is successful
def check_transaction(user_pay, menue, drink):
    """takes user payment, check if payment covers the cost of requested drink"""

    enough_pay = True
    global money
    drink_cost = menue[drink]['cost']
    change = 0.0
    print(f"{drink} costs ${drink_cost}")
    if user_pay < drink_cost :
        enough_pay = False
        print("Sorry that's not enough money. Money refunded.")
    else:
        money += drink_cost
        change = user_pay - drink_cost
        print(f"Here is ${change:.2f} in change.")

    return enough_pay


#TODO: make coffee and deduct from resources
def make_coffee(resources, menue, drink):
    """make a coffee and deduct from the resources"""

    resources['water'] -= menue[drink]['ingredients']['water']
    resources['coffee'] -= menue[drink]['ingredients']['coffee']
    
    if drink != 'espresso':
        resources['milk'] -= menue[drink]['ingredients']['milk']

    print(f"Here is your {drink}. Enjoy!")
    return resources

def refill_resources(resources):
    """refills machine's resources and return a resources dict"""
    resources['water'] += int(input(f"How much ml Water to refill?: "))
    resources['milk'] += int(input(f"How much ml Milk to refill?: "))
    resources['coffee'] += int(input(f"How much g coffee to refill?: "))
    return resources


def coffee_machine(resources, MENU):
    """connect all functionalies together to function as coffee machine"""
    is_machine_on = True
    print(logo)

    while is_machine_on:
        #TODO: print intro         
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        #TODO: off,  to exit
        if user_input == 'off':
            is_machine_on = False
            print("Goodbye!")       
        elif user_input == 'refill':            
            resources = refill_resources(resources)
        elif user_input == 'report':
            report(resources, money)    
        else:
            if MENU.get(user_input):
                if check_resources(resources, MENU, user_input):
                    user_pay = process_money()
                    if check_transaction(user_pay, MENU, user_input):
                        resources = make_coffee(resources, MENU, user_input)
            else:
                print("unknown option!")


coffee_machine(resources, MENU)

