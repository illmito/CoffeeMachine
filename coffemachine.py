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
    }
}

resource = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
}

# print report of all resources in machine when "report' input.
def report():
    for key, value in resource.items():
        coffee_resources = resource
        print(f"{key}: {value}ml")
    print(f"total monies: ${float(monies)}")


# check resources / compare to make coffee.
def resource_remain():
    coffee_resources = []
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']
    coffee_resources.append(water)
    coffee_resources.append(coffee)
    coffee_resources.append(milk)
    return coffee_resources

# checks resources needed to make the coffee.
def make_coffee(selected):
    selected = user_input
    ingredients = []
    cost = MENU[selected]['cost']
    if selected == 'espresso':
        water = MENU[selected]['ingredients']['water']
        coffee = MENU[selected]['ingredients']['coffee']
        ingredients.append(water)
        ingredients.append(coffee)
    else:
        water = MENU[selected]['ingredients']['water']
        milk = MENU[selected]['ingredients']['milk']
        coffee = MENU[selected]['ingredients']['coffee']
        ingredients.append(water)
        ingredients.append(coffee)
        ingredients.append(milk)
    resource_ = resource_remain()

    if user_input == 'espresso':
        if ingredients[0] <= resource_[0]:
            if ingredients[1] <= resource_[1]:
                print("processing")
                payment()
            else:
                print('sorry there is not enough coffee')
        else:
            print('sorry the is not enough water.')

    elif user_input == 'latte' or 'cappuccino':
        if ingredients[0] <= resource_[0]:
            if ingredients[1] <= resource_[1]:
                if ingredients[2] <= resource_[2]:
                    print("processing...")
                    payment()
                else:
                    print('sorry the is not enough Milk.')
            else:
                print('sorry the is not enough coffee.')
        else:
            print('sorry the is not enough water.')

# display and process payment of coffee choice.
def payment():
    cost = cost = MENU[user_input]['cost']
    print(f"{user_input}: ${cost}")
    print("Please insert coins.")

    quarter_insert = int(input("How many Quarters?: "))
    dime_insert = int(input("How many Dimes?: "))
    nickle_insert = int(input("How many Nickles?: "))
    penny_insert = int(input("How many Pennies?: "))

    quarters = quarter_insert * 0.25
    dimes = dime_insert * 0.10
    nickles = nickle_insert * 0.05
    pennies = penny_insert * 0.01

    total = (quarters + dimes + nickles + pennies)

    if total == cost:
        print(f"Payment confirmed, Making {user_input}:")
        return total
    elif total > cost:
        change = total - cost
        print(f"payment confirmed, Making {user_input}:")
        print(f"Please take your change: ${round(change, 2)}")
        return total
    else:
        print("Sorry insufficient amount inserted, Refund processed.")


# total amount in the machine


machine_on = True
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()


    if user_input == 'espresso':
        make_coffee(user_input)
    elif user_input == 'latte':
        make_coffee(user_input)
    elif user_input == 'cappuccino':
        make_coffee(user_input)
    elif user_input == 'report':
        report()
    elif user_input == 'off':
        machine_on = False
        print("Turning off...")
        print("off")
    else:
        print(user_input)