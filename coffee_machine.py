menu = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True    

def resource_left(actual_resource, ordered_resource):
    for item in ordered_resource:
        actual_resource[item] -= ordered_resource[item]    

  
def process_coins(ordered_coffee):
    print("Insert Coins")
    total = int(input("quarters: ")) * 0.25
    total += int(input("quarters: ")) * 0.10
    total += int(input("quarters: ")) * 0.05
    total += int(input("quarters: ")) * 0.01
    if total < ordered_coffee:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        change = total - ordered_coffee
        global profit
        profit += (total - change)
        print(f"Here is ${round(change,2)} dollars in change")
        return True

profit = 0  

is_coffee_machine_on = True

while is_coffee_machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    elif user_input == "off":
        is_coffee_machine_on = False
    else: 
        ingredients_check = check_resources(menu[user_input]["ingredients"])
        if ingredients_check == True:
            transcation = process_coins(menu[user_input]["cost"])
            if transcation == True:
                resource_left(resources, menu[user_input]["ingredients"])
                print(f"Here is your {user_input}. Enjoy!")
        
    
        

        
            