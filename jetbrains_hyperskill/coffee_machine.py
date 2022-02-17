WATER = 200
MILK = 50
COFFEE_BEANS = 15
WATER_COUNT = 400
MILK_COUNT = 540
COFFEE_BEANS_COUNT = 120
CUPS = 9
MONEY = 550


def print_info():
    print(
        """
The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money
""".format(
            WATER_COUNT, MILK_COUNT, COFFEE_BEANS_COUNT, CUPS, MONEY
        )
    )


def buy():
    while True:
        coffee_type = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "
            "\n> "
        )
        global WATER_COUNT, MILK_COUNT, COFFEE_BEANS_COUNT, CUPS, MONEY
        if coffee_type == "1":
            if WATER_COUNT < 250:
                print("Sorry, not enough water!")
                break
            if COFFEE_BEANS_COUNT < 16:
                print("Sorry, not enough coffee!")
                break
            if CUPS < 1:
                print("Sorry, not enough cups!")
                break
            else:
                print("I have enough resources, making you a coffee!")
            WATER_COUNT -= 250
            COFFEE_BEANS_COUNT -= 16
            CUPS -= 1
            MONEY += 4
            break
        elif coffee_type == "2":
            if WATER_COUNT < 350:
                print("Sorry, not enough water!")
                break
            if MILK_COUNT < 75:
                print("Sorry, not enough milk!")
                break
            if COFFEE_BEANS_COUNT < 20:
                print("Sorry, not enough coffee!")
                break
            if CUPS < 1:
                print("Sorry, not enough cups!")
                break
            else:
                print("I have enough resources, making you a coffee!")
            WATER_COUNT -= 350
            MILK_COUNT -= 75
            COFFEE_BEANS_COUNT -= 20
            CUPS -= 1
            MONEY += 7
            break
        elif coffee_type == "3":
            if WATER_COUNT < 200:
                print("Sorry, not enough water!")
                break
            if MILK_COUNT < 100:
                print("Sorry, not enough milk!")
                break
            if COFFEE_BEANS_COUNT < 12:
                print("Sorry, not enough coffee!")
                break
            if CUPS < 1:
                print("Sorry, not enough cups!")
                break
            else:
                print("I have enough resources, making you a coffee!")
            WATER_COUNT -= 200
            MILK_COUNT -= 100
            COFFEE_BEANS_COUNT -= 12
            CUPS -= 1
            MONEY += 6
            break
        if coffee_type == "back":
            break


def take():
    global MONEY
    print(
        """
    I gave you ${}
    """.format(
            MONEY
        )
    )
    MONEY -= MONEY


def fill():
    global WATER_COUNT, MILK_COUNT, COFFEE_BEANS_COUNT, CUPS, MONEY
    add_water = int(input("Write how many ml of water do you want to add: \n> "))
    WATER_COUNT += add_water
    add_milk = int(input("Write how many ml of milk do you want to add: \n> "))
    MILK_COUNT += add_milk
    add_coffee_beans = int(
        input("Write how many grams of coffee beans do you want to add: \n> ")
    )
    COFFEE_BEANS_COUNT += add_coffee_beans
    add_cups = int(
        input("Write how many disposable cups of coffee do you want to add: \n> ")
    )
    CUPS += add_cups


while True:
    action = input("Write an action: (buy, fill, take, remaining, exit)\n> ")
    if action == "buy":
        buy()
    elif action == "take":
        take()
    elif action == "fill":
        fill()
    elif action == "remaining":
        print_info()
    else:
        break
