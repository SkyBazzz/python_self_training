MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}
profit = 0
resources = {
    "water": 200,
    "milk": 200,
    "coffee": 100,
}


# TODO: if not add method to supply resources
def is_resource_sufficient(order_ingredients):
    """Calculates ability to create a drink from resources"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"{item=} is not enough. Available {resources[item]=}")
            return False
    print("We have all resources")
    return True


def process_coins():
    """
    returns total calculated from coins inserted
    """
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if the payment is successful"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} in change")
        return True
    print("There is not enough money. Money refund")
    return False


is_on = True


def make_coffee(drink_name, order_ingredients):
    """Deduct e required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


while is_on:
    choice = input(
        f"What would you like to order {[ingredient for ingredient in MENU]}?"
    )
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(resources)
        print(f"${profit} profit")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
