print()
from datetime import datetime

def main():
    name = input("Please enter your name: ")
    gender = input("Enter your gender (M/F): ")
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    weight_lb = int(input("Enter your weight (lbs): "))
    height_in = int(input("Enter your height (in): "))

    print()
    print(f"Age: {compute_age(birthday)}")
    # print(f"Weight (kg): {kg_from_lb(weight_lb):.2f}")
    # print(f"Height (cm): {cm_from_in(height_in):.1f}")
    print(f"Body mass index: {body_mass_index(kg_from_lb(weight_lb), cm_from_in(height_in)):.1f}")
    print(f"Basal metabolic rate (kcal/day): {basal_metabolic_rate(gender, kg_from_lb(weight_lb), cm_from_in(height_in), compute_age(birthday)):.0f}")

    print("\nResults recorded on fitness.txt.")
    with open("fitness.txt", "at") as fitness_database:
        print("", file=fitness_database)
        print(f"{name.title()}: {gender.capitalize()}, {birthday}", file=fitness_database)
        print(f"     {weight_lb} lbs, {feet_from_in(height_in)}, bmi: {body_mass_index(kg_from_lb(weight_lb), cm_from_in(height_in)):.1f}, bmr: {basal_metabolic_rate(gender, kg_from_lb(weight_lb), cm_from_in(height_in), compute_age(birthday)):.0f}", file=fitness_database)

def compute_age(birth):
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthday.year

    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years

def kg_from_lb(lb):
    return lb * .45359237

def cm_from_in(inch):
    return inch * 2.54

def body_mass_index(weight, height):
    return 10000 * weight / height ** 2

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == "m":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif gender.lower() == "f":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age
    return bmr

def feet_from_in(inches):
    feet = inches // 12
    inches_left = inches % 12
    return (f"{feet} ft {inches_left} in")

main()
print()