print()
import math

# Here the calculations are defined beforehand
def calc_volume(width, asp_ratio, diameter):
    return (math.pi * (width ** 2) * asp_ratio * (width * asp_ratio + 2540 * diameter)) / 10000000

name = input("Welcome to the tire shop!\n\nPlease enter your name: ")

# Asks for a rewards account number
phone = False
rewards_done = False
while rewards_done == False:
    if_rewards = input(f"{name.capitalize()}, do you have a rewards account with us? (yes or no): ")
    if if_rewards.lower() == "yes":
        phone_number = input("Please enter your phone number: ")
        print("Rewards activated!")
        phone = True
        rewards_done = True

    elif if_rewards.lower() == "no":
        new_rewards = ""
        while new_rewards not in ("yes", "no"):
            new_rewards = input("Would you like to register one with us? (yes or no): ")
            if new_rewards.lower() == "yes":
                phone_number = input("Please enter your phone number: ")
                print("Rewards account created!")
                rewards_done = True
                phone = True
            elif new_rewards.lower() == "no":
                rewards_done = True
                phone_number = "(no number)"
            else:
                print("\nError: Unrecognized response.\n")
    else:
        print("\nError: Unrecognized response.\n")

# Asks for tire information
print("\nPlease answer the following about your tires:")
width = int(input("Tire width in mm (ex 205): "))
asp_ratio = int(input("Tire aspect ratio (ex 60): "))
diameter = int(input("Tire diameter in inches (ex 15): "))

# Uses the function to calculate tire volume
volume = calc_volume(width, asp_ratio, diameter)
print(f"\nThe approximate volume is {volume:,.1f} milliliters.")

# Allows you to change any tire variable
answer = True
while answer:
    change = input("\nWould you like to change a measurement? (yes or no): ")
    if change.lower() == "yes":
        which_change = input("Which would you like to change? The tire's WIDTH, aspect RATIO, or DIAMETER? ")
        if which_change.lower() == "width":
            width = int(input("What is the updated width? "))
        elif which_change.lower() == "ratio":
            asp_ratio = int(input("What is the updated aspect ratio? "))
        elif which_change.lower() == "diameter":
            diameter = int(input("What is the updated diameter? "))
        else:
            print("\nSorry, unrecognized input. Please try again.")

        if which_change.lower() in("width", "ratio", "diameter"):
            volume = calc_volume(width, asp_ratio, diameter)
            print(f"\nThe current approximate volume is {volume:,.1f} milliliters")
    elif change.lower() == "no":
        answer = False
    else:
        print("\nSorry, unrecognized input. Please try again.")

print(f"\nYour final volume is {volume:,.1f} ml")

# Checks if the user wants to purchase these tires
check_purchase = True
while check_purchase:
    buy_tires = input("Would you like to buy this size of tire? (yes or no): ")
    if buy_tires.lower() == "yes":
        if phone:
            print("Purchase added to your account.")
        else:
            phone_number = input("Please enter your phone number: ")
            print(f"Okay {name}, we'll reach out to you when these tires are in stock.")
        check_purchase = False
    elif buy_tires.lower() == "no":
        check_purchase = False
    else:
        print("\nError: Unrecognized input. Please try again.\n")

# Retrieves and stores the date for organizational purposes
from datetime import datetime
right_now = datetime.now()
now_str = str(right_now)
dates = (now_str.strip()).split(" ")
date = dates[0]

# Archives all information on a text file in this format:
# Name: Rewards number
#     Date, Tire width, Aspect ratio, Tire diameter, Tire volume
with open("volumes.txt", "at") as vol_file:
    print("", file=vol_file)
    print(f"{name}: {phone_number}", file=vol_file)
    print(f"     {date}, {width}, {asp_ratio}, {diameter}, {volume:,.1f}", file=vol_file)

print("\nYour information has been added to our records.\nThank you for coming to the tire shop!")
print()