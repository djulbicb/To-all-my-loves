# TODO: Get user order espresso, latter, cappucino
# TODO: secret action 'report' and 'off'
# TODO: Check if enough resources
# TODO: Process coins
# TODO: Check transaction succesfull, if enough coins
# TODO: Make coffe, reduce resources

from math import floor, ceil
from data import MENU
from art import LOGO

allowed_commands = []
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def round_down(n, d=8):
    d = int('1' + ('0' * d))
    return floor(n * d) / d


def round_up(n, d=8):
    d = int('1' + ('0' * d))
    return ceil(n * d) / d


def get_allowed_command() -> str:
    commands = []
    for menuItem in MENU:
        commands.append(menuItem.lower())
    commands.append("report")
    commands.append("off")
    commands.append("refill")
    commands.append("exit")
    return commands


def get_user_command() -> str:
    user_command = ""
    while user_command not in allowed_commands:
        user_command = input("Enter command 'espresso', 'latte', 'cappuccino', 'exit': ").lower()
        if user_command not in allowed_commands:
            print("Info: Unknown command")
    return user_command


def refill():
    """
    Reffill all ingredients
    """
    for resource in resources:
        resources[resource] += 100


def report():
    print("-REPORT-----------------------------")
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Profit: {profit}$")
    print("------------------------------------")


def is_enough_ingredients(item_ingredients):
    for ingredient in item_ingredients:
        if resources[ingredient] < item_ingredients[ingredient]:
            return False
    return True


def take_ingredients(item_ingredients):
    for ingredient in item_ingredients:
        resources[ingredient] -= item_ingredients[ingredient]


def get_user_money() -> float:
    dollars = int(input('How many dollars?: '))
    quarters = int(input('How many quarters?: '))
    nickles = int(input('How many nickles?: '))
    return dollars * 1 + quarters * 0.25 + nickles * 0.05


def return_change(required_money, user_money) -> float:
    return round_up(user_money - required_money, 3)


def make_coffee(user_choice):
    global profit

    item = MENU[user_choice]
    print(item)

    required_ingredients = item['ingredients']
    if not is_enough_ingredients(required_ingredients):
        print(f'Info: There is not enough resources for this {user_choice}')
        return

    required_money = item['cost']
    user_money = get_user_money()
    is_enough_money = required_money <= user_money
    if not is_enough_money:
        print(f"Not enough money. {user_choice} costs {required_money}. Here is refund.")
        return

    take_ingredients(required_ingredients)
    change = return_change(required_money, user_money)
    profit += required_money

    print(f"Here is change {change}")
    print(f"{user_choice.title()} is made. Enjoy")


# MAIN
# --------------------------------------
allowed_commands = get_allowed_command()

enabled = True

while enabled:
    print(LOGO)
    running = True

    while running:
        command = get_user_command()

        if command == 'exit':
            print('Exit.')
            running = False
            pass
        elif command == 'off':
            print("ADMIN: Turning off machine.")
            running = False
            enabled = False
            print("ADMIN: Turned off.")
        elif command == 'report':
            print("ADMIN: Printing report")
            report()
        elif command == 'refill':
            print("ADMIN: Refilling ingredients.")
            refill()
        elif command in MENU:
            print(f"Making {command}")
            make_coffee(command)


