menu = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def usermoney():
    money = 0 
    money += int(input("How many quarters?")) * 0.25
    money += int(input("How many dimes?")) * 0.10
    money += int(input("How many nickles")) * 0.05
    money += int(input("How many pennies?"))* 0.01
    return (money)
def successfulTransaction(user_money,machine_cost):
    if user_money >= machine_cost : 
        change = round(user_money - machine_cost,2)
        global profit 
        profit += machine_cost 
        print(f" here is your {change}")
        return(True)
    else:
        print("Sorry you do not have enough money, money refunded")
        return(False)
def makeCoffee(chosenCoffee,coffeIngredient):
    for item in coffeIngredient:
        resources[item] -= coffeIngredient[item]
    print("Here is your coffee ☕️. Enjoy!")
def resourceCheck(coffeeIngredient):
    for item in coffeeIngredient:
        if coffeeIngredient[item] > resources[item]:
            print(f"Sorry their is not enough {item}")
            return(False)
    return(True)


isOn = True 

while isOn:
    userinput = input("What would you like? ($ 1.50 Espresso/ $2.50 Latte/ $3 Cappuccino) ").lower()
    if userinput == "off":
        isOn = False
    elif userinput == "report":
        print(f"{resources['water']}ml")
        print(f"{resources['milk']}ml")
        print(f"{resources['coffee']}g")
        print(f"Money profit: ${profit}")
    else:
        drink = menu[userinput]
        if resourceCheck(drink['ingredients']):
            money = usermoney()
            if successfulTransaction(money,drink["cost"]):
                makeCoffee(userinput,drink['ingredients'])



    

#resources["water"] -= espresso["water"]
#print(resources)






