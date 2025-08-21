"""
    This is a program that lets the user input his/her temperature, and thus 
    comparing it to the normal temperature of a human. 
    Depending on your temperature, it will display the appropriate message.
    The program asks the user if they want to be tested again using the prompt
    "Do you want to test again? Press [Y/y]-continue || [N/n]-exit."

    Aug 20, 2025
"""


temperature = 0.00
another_test = ""

while another_test.lower() != "n": #Checks if the user wants to stop testing/using the program
    temperature = float(input("\nEnter your temperature in celsius: ")) #Asks for user's temperature
    
    #Compares the user temperature and then checks what statement it is under and displays the appropriate message 
    if temperature < 37:
        print("Your temperature is normal.")
    else: 
        print("You have a fever.")
    another_test = input("\nDo you want to test again? \nPress [Y/y]-continue || [N/n]-exit: ")

#Program ending message
print("\nThank you for using the program.")
print("Program Ended.\n")