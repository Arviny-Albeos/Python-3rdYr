"""
Problem Statement: 
    Create a menu for a fastfood restaurant (using match-case) with a minimum of 3 choices
    and no max limit. Put a price for every item using float. Add a VAT of 12% on the total price.
    
    Needed Input: 
        Customer order/s
        Asks for membership for discount price 
        Asks for another order
        
    Example/Expected Results:
        Order List: S1, S2, S3
        Discount: Y/N
        
        Total Price: $159.99 

    Match Case; Loops (while loop); if-else statements
"""

order_no = 1
another = ""
VAT = 0.12
total_price = 0.00

while another.lower() != "n":
    print("Order No.", order_no)
    customer_order = input("Order List (S1/S2/S3): ")
    membership = input("Membership (Y/N): ")

    match customer_order: 
        case "S1": 
            if membership.lower() == "y":
                burger = 11.59
                coke = 7.59
            else:
                burger = 12.99
                coke = 8.99
            print("Order Details:")
            print("S1: Burger & Fries")
            print("Burger:$", burger)
            print("Coke:$", coke)
            total_price = (burger + coke) * (1 + VAT)
            print("Total Price:$", round(total_price, 2))

        case "S2":
            if membership.lower() == "y":
                nuggets = 10.59
                root_beer = 6.59
            else:
                nuggets = 11.59
                root_beer = 7.99
            print("Order Details:")
            print("S2: Nuggets and Root Beer")
            print("Nuggets:$", nuggets)
            print("Root Beer:$", root_beer)
            total_price = (nuggets + root_beer) * (1 + VAT)
            print("Total Price:$", round(total_price, 2))

        case "S3":
            if membership.lower() == "y":
                fried_chicken = 17.59
                coke = 7.59 
            else:
                fried_chicken = 18.99
                coke = 8.99
            print("Order Details:")
            print("S3: Fried Chicken & Coke")
            print("Fried Chicken:$", fried_chicken)
            print("Coke:$", coke)
            total_price = (fried_chicken + coke) * (1 + VAT)
            print("Total Price:$", round(total_price, 2))

        case _: 
            print("Invalid order!")

    another = input("Do you want to add another order? (Y/N): ")   
    if(another.lower() != "n"):
        order_no = order_no + 1

print("Thank you for ordering. Come again next time!")

            