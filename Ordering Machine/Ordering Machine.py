order_Nihao={'jiaozi':5,'baozi':6,'noodles':10,'tea':3}
order_burger={'beef burger':8,'chicken burger':6,'fish burger':12,'coke':2}
order_lido={'latte':7,'cappucino':6,'choco':5,'tiramisu':11}
order_addon={'lettuce':1,'Bacon':2}
lst=list()
price=0


name=input("Which restaurant would you like? ")
print('\nWe have the following cuisines: ')
if name.lower()=='nihao':
    for k,v in order_Nihao.items():
        print(f" {k} at price of {v}")
    print("\n")

    order=input('What would you like to order? \n (Please key in your choice and divide by comma.\n eg: apple,apple,egg)\n')
    lst=order.split(",")
    for i in lst:
        if i in order_Nihao.keys():
            price+=order_Nihao[i]
    
    print(f"The total price is {price}")


elif name.lower()=='mr burger':
    for k,v in order_burger.items():
        print(f"{k} at price of {v}")
    print('\n You can also add the following ingredient in your burger:')
    for k,v in order_addon.items():
        print(f"{k} at price of {v}")
    print("\n")

    order=input('What would you like to order? \n (Please key in your choice and divide by comma.\n eg: apple,apple,egg)\n')
    lst=order.split(",")
    for i in lst:
        if i in order_burger.keys():
            price+=order_burger[i]
        elif i in order_addon.keys():
            price+=order_addon[i]
    
    print(f"The total price is {price}")

elif name.lower()=='lido':
    for k,v in order_lido.items():
        print(f"{k} at price of {v}")
    print("\n")

    for i in lst:
        if i in order_lido.keys():
            price+=order_lido[i]
    
    print(f"The total price is {price}")

else:
    print(f'/n error, please try again.')


