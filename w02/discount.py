from datetime import datetime
print()

right_now = datetime.now()
weekday = right_now.isoweekday()
weekday = 3

discount = False

subtotal = float(input("Please enter the subtotal: "))
tax = subtotal * .06
print(f"Sales tax amount: {tax:.2f}")

total = subtotal + tax

print(f"Total: {total:.2f}")

if weekday in(2, 3) and subtotal >= 50:
    discount = total * 0.1
    print(f"Discount: {discount}")
