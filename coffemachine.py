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
    "total": 0
}


# print report of all resources in machine when "report' input.
def report():
    monies = resource['total']
    for key, value in resource.items():
        coffee_resources = resource
        print(f"{key}: {value}")


# checks resources needed to make the coffee.
def make_coffee(selected):

    coffee_ingredient = MENU[selected]["ingredients"]

    # Espresso
    if user_input == 'espresso':
        if coffee_ingredient["water"] <= resource["water"]:
            if coffee_ingredient["coffee"] <= resource["coffee"]:
                resource["water"] -= coffee_ingredient["water"]
                resource["coffee"] -= coffee_ingredient["coffee"]
                print("processing")
                payment()
            else:
                print('sorry there is not enough coffee')
        else:
            print('sorry the is not enough water.')

    # Latte
    elif user_input == 'latte':
        if coffee_ingredient["water"] <= resource["water"]:
            if coffee_ingredient["coffee"] <= resource["coffee"]:
                if coffee_ingredient["milk"] <= resource["milk"]:
                    print("processing...")
                    resource["water"] -= coffee_ingredient["water"]
                    resource["coffee"] -= coffee_ingredient["coffee"]
                    resource["milk"] -= coffee_ingredient["milk"]
                    payment()
                else:
                    print('sorry the is not enough Milk.')
            else:
                print('sorry the is not enough coffee.')
        else:
            print('sorry the is not enough water.')

    # Cappuccino
    elif user_input == 'cappuccino':
        if coffee_ingredient["water"] <= resource["water"]:
            if coffee_ingredient["coffee"] <= resource["coffee"]:
                if coffee_ingredient["milk"] <= resource["milk"]:
                    print("processing...")
                    resource["water"] -= coffee_ingredient["water"]
                    resource["coffee"] -= coffee_ingredient["coffee"]
                    resource["milk"] -= coffee_ingredient["milk"]
                    payment()
                else:
                    print('sorry the is not enough Milk.')
            else:
                print('sorry the is not enough coffee.')
        else:
            print('sorry the is not enough water.')

    print("_____________")
    print(f"Enjoy your {user_input}\n")



# display and process payment of coffee choice.
def payment():
    cost = MENU[user_input]['cost']

    print(f"{user_input}: ${cost}")
    print("Please insert coins.")

    quarter_insert = int(input("How many Quarters?: "))
    dime_insert = int(input("How many Dimes?: "))
    nickle_insert = int(input("How many Nickles?: "))
    penny_insert = int(input("How many Pennies?: "))
    print("__________")

    quarters = quarter_insert * 0.25
    dimes = dime_insert * 0.10
    nickles = nickle_insert * 0.05
    pennies = penny_insert * 0.01

    total = (quarters + dimes + nickles + pennies)

    if total == cost:
        print(f"Payment confirmed, Making {user_input}:")
        resource["total"] += cost
    elif total > cost:
        change = total - cost
        print(f"Please take your change: ${round(change, 2)}")
        print(f"Payment confirmed, Making {user_input}:")
        resource["total"] += cost
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
