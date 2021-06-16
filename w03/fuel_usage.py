print()

def main():
    start_miles = float(input("What is the starting odometer value? "))
    end_miles = float(input("What is the ending value? "))
    amount_gallons = float(input("How many gallons of gas were used? "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)

    print(f"You ran at {mpg:.1f} miles per gallon, or {lp100k:.2f} liters per 100km.")
    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    return (end_miles - start_miles) / amount_gallons

def lp100k_from_mpg(mpg):
    return 235.215 / mpg

main()

print()