#Program Created By Manasvi Koppaka
#Introduction

import signup_login
while True:
    signup_login.hr3()
    print("1 - Signup")
    print("2 - Login")
    print("3- Exit")
    signup_login.hr3()
    option = int(input("Enter your option: "))
    if option == 1:
        signup_login.signup()
    elif option == 2:
        username = signup_login.login()
        if username != False:
            break
    elif option == 3:
        quit()
    else:
        print("Invalid Input")

print("_________________________________________")
print("_________________________________________")
print("           HOLI SHOP BY MANASVI          ")
print("_________________________________________")
print("_________________________________________")

#List of items
items = ["Colors", "Water Balloons", "Water Guns", "Return"]

#List of Items with their prices
colors = [["Red", 4], ["Yellow", 4], ["Orange",4], ["Blue", 3], ["Purple", 1], ["Pink",3]]
water_balloons = [["Small", 2], ["Medium", 4], ["Big", 6]]
water_guns = [["Small", 10], ["Medium", 15], ["Big", 20]]

#Variabes
org_total1 = 0
org_total2 = 0
org_total3 = 0
new_total = 0


#List of items the user wants to buy with their quantities will be stored in here.
user_list = []

#Added a While loop so user can buy again and again.
while True:
    print("Select the option you want to buy: ")

    print("------------------------------------------------")

    #List of items the user can buy will be displayed here.
    for i in range(len(items)):
        print(i+1, "-", items[i])

    print("0 - None of the above")
    print("------------------------------------------------")

    choice = input("Enter the number: ")

    if choice.isnumeric():
        choice = int(choice)
    else:
        print("Invalid Input")
        continue
    

    #Colors Process
    #list of items in the catogory will be displayed here.
    if choice == 1:
        print("------------------------------------------------")

        for i in range(len(colors)):
            print(i+1, "-", colors[i][0], ":    $", colors[i][1], "per packet")
        
        print("0 - None of the above")
        print("------------------------------------------------")


        #The NUMBER user want to purchase and the quantity will be stored in item and qty1
        item1 = int(input("Enter the number: "))
        
        if item1 == 0:
            print("Try something else")
            continue
        if item1 > len(colors):
            print("Invalid Input, Try Again")
            continue

        qty1 = int(input("Enter the quantity: "))
        print("------------------------------------------------")


        #The ITEM user want to purchase and the cost will be stored in price and product
        price = colors[item1-1][1]
        product = colors[item1-1][0]

        #The current item cost
        tempTotal1 = price*qty1


        print(qty1, "packet", product, "for $", tempTotal1) 
        print("------------------------------------------------")


        #Confirm and Order Checkout
        confirm = int(input("Click 1 to confirm and 0 to cancel: "))
        print("------------------------------------------------")
        if confirm == 1:
            confirm_list = ["Colors", colors[item1-1], qty1]
            user_list.append(confirm_list) 
            print("Added this item to your cart")
            print("------------------------------------------------")


            #acumilated total value
            org_total1 = org_total1+tempTotal1



#Water Balloon Process
    elif choice == 2:
        print("------------------------------------------------")

        for i in range(len(water_balloons)):
            print(i+1, "-", water_balloons[i][0], ":    $", water_balloons[i][1], "per packet")
        print("0 - None of the above")

        item2 = int(input("Enter the number: "))
        print("------------------------------------------------")


        if item2 == 0:
            print("Try something else")
            continue
        if item2 > len(water_balloons):
            print("Invalid Input, Try Again")
            continue
    
        qty2 = int(input("Enter the quantity: "))
        print("------------------------------------------------")
    

        price = water_balloons[item2-1][1]
        product = water_balloons[item2-1][0]

        #The current item cost
        tempTotal2 = price*qty2



        print(qty2, "packet", product, "for $", tempTotal2)
        print("------------------------------------------------")

        confirm = int(input("Click 1 to confirm and 0 to cancel: "))
        print("------------------------------------------------")

        if confirm == 1:
            confirm_list = ["Water Balloons", water_balloons[item2-1], qty2]
            user_list.append(confirm_list) 
            print("Added this item to your cart")
            print("------------------------------------------------")

        #acumilated total value
        org_total2 = org_total2+tempTotal2

#Water Guns Process

    elif choice == 3:
        print("------------------------------------------------")
        for i in range(len(water_guns)):
            print(i+1, "-", water_guns[i][0], ":    $", water_guns[i][1], "per packet")
        print("0 - None of the above")
        print("------------------------------------------------")

        item3 = int(input("Enter the number: "))

        if item3 == 0:
            print("Try something else")
            continue
        if item3 > len(water_guns):
            print("Invalid Input, Try Again")
            continue

        qty3 = int(input("Enter the quantity: "))
        print("------------------------------------------------")

        

        price = water_guns[item3-1][1]
        product = water_guns[item3-1][0]

        #The current item cost
        tempTotal3 = price*qty3

        print(qty3, "packet", product, "for $", tempTotal3)
        print("------------------------------------------------")

        confirm = int(input("Click 1 to confirm and 0 to cancel: "))
        print("------------------------------------------------")

        if confirm == 1:
            confirm_list = ["Water Guns", water_guns[item3-1], qty3]
            user_list.append(confirm_list) 
            print("Added this item to your cart")
            print("------------------------------------------------")        
            #acumilated total value
        org_total3 = org_total3+tempTotal3



    elif choice == 0:
        pass

    else:
        print("Invalid Input")
        continue
    #Finalizing the totals. 
    flag = 1
    new_total = org_total1+org_total2+org_total3
    while True:
        again = input("Do you want to buy anything else? Yes/No: ")
        print("------------------------------------------------")

        if again.lower() == "yes":
            break 
        elif again.lower() == "no":
            print("The total cost for your order would be: $", new_total)
            flag = 0
            break 
        else:
            print("Input is invalid. Do you want to try again? Yes/No")
            continue
    if flag == 0:
        break


#Total Bill
print()
print("_________________________________________")
print("                  Bill                   ")
print("_________________________________________")
for i in user_list:
    print(i[0], "--->", i[1][0], " X ", i[2], " : $", i[1][1]*i[2])

print("________________________________________")
print("Total Price : $", new_total)
print("Tax (10%) : $", new_total*0.1)
print("-----------------------------------------")
print("Grand Total : $", new_total+new_total*0.1)
print("_________________________________________")
print("                Thank You                ")
print("_________________________________________")

import shop
shop.insert(username, user_list)