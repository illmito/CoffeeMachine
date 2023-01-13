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

# display payment of coffee choice.
def payment():
    cost = cost = MENU[user_input]['cost']
    print(f"{user_input} comes to ${cost}")


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