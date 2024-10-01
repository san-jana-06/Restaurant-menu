#Define the menu of restaurant
menu={"pizza":100,"burgar":50,"sandwich":60,"pasta":80,"coffee":90}
#greet
print("welcome to our python restaurant")
print("pizza: Rs100\nburgar: Rs50\nsandwich: Rs60\npasta: Rs80\ncoffee: Rs90")

order_total = 0 
#50+100=150

item_1 = input("enter the name of item you want to order =  ")
if item_1 in menu:
    order_total += menu[item_1] #0+100=100
    print(f"your item {item_1} has been added to your order")
    
else:
    print(f"order item {item_1} is not avaialable yet!")
    
another_order=input("do you want to add another item?(YES/NO) ")
if another_order == "YES":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been  added to order")
        
    else:
        print(f"orderded item {item_2} is not available!")
        
    print(f" the total amount of items to pay is  {order_total}")