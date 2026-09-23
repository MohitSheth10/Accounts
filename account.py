import random
import os
check=False
name=input("Enter your name:\n").title().strip()
print(f"Hello {name}! Welcome to the ATM")
folder_path = os.path.dirname(os.path.abspath(__file__))  # Save account files next to this script
file_path = os.path.join(folder_path, name + ".txt")  # Combine folder path and user input
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
def input_pin_with_check(prompt_text):
    while True:
        try:
            pin = int(input(f"{prompt_text}:\n"))
            pin_str = str(pin)
            if len(pin_str) == 6:
                return pin_str  # Return string for consistency in saving/reading
            else:
                print("Pin must be exactly 6 digits.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
def get_valid_pin():
    while True:
        pin = input_pin_with_check("Enter your 6 digit pin")       
        pin_confirm = input_pin_with_check("Confirm your 6 digit pin")
        if pin != pin_confirm:
            print("\nPins are not the same.\n")
        else:
            return pin
if os.path.isfile(file_path):
    print("A file with that name exists in the folder.")
    with open(file_path, "r") as playerfile:
        saved_pin=playerfile.read().strip()
    def inputpin():
        return input_pin_with_check("Enter your pin")
    userpin=inputpin()
    attempts = 3
    while userpin!=saved_pin and attempts>0:
        print("Incorrect pin")
        attempts-=1
        choice2=input("Do you wish to 1. Change your pin or 2. Retry pin:\n").lower().strip()
        if choice2 in ["1", "changepin", "change"]:
            check=True
            break
        else:
            userpin=inputpin()
    if check==True:
        newpin =  get_valid_pin()
        with open(file_path, "w") as nplayerfile:
            nplayerfile.write(newpin)
        print(f"{newpin} has been saved as your new pin. ")
        print("Relogin to enter account")
    elif attempts==0:
        print("Out of attempts.\nLogged out of account.")
    else:
        print("Correct pin you are in the account") #limit no of tries to enter pin   
else:
    print("No file with that name exists in the folder.")
    choice1=input("Do you wish to create an account? Yes or No? ").lower().strip()
    if choice1=="yes" or choice1=="y":
        newaccountpin=get_valid_pin()
        with open(file_path,"w") as playerfile:
            playerfile.write(newaccountpin)
        print(f"Congratulations {name} your account has been created.")

    else:
        print("Ok return to the ATM later. ")
