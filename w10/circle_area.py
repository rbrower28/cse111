""" Calculates circle area w/ user input for multiple circles """

from math import pi


""" My solution:

def main():

    repeat = True
    while repeat:
        
        try:
            rad_circle = float(input("Please input a radius (enter any word to end): "))
            area_circle = calc_area_circle(rad_circle)

            print(f"The area of a circle with radius {rad_circle} is {area_circle:.2f}")

        except ValueError:
            repeat = False


def calc_area_circle(radius):
    return pi * radius ** 2

"""




""" Teacher solution: """

def main():

    num_of_circles = integer_input("How many circles are we working with? ")

    areas = []
    radiuses = []
    
    loop_for_circles(num_of_circles, areas, radiuses)

    display_areas(areas, radiuses)


def integer_input(msg):

    while True:
        try:
            answer = int(input(msg))
            break
        except ValueError:
            print("Please put an integer next time dummy")

    return answer


def loop_for_circles(number_of_circles, areas, radiuses):

    for _ in range(number_of_circles):

        r = integer_input("Please enter a radius: ")

        a = compute_circle_area(r)
        areas.append(a)
        radiuses.append(r)


def compute_circle_area(radius):
    return pi * radius ** 2


def display_areas(areas, radiuses):
    
    for i in range(len(areas)):
        print(f"The circle with the radius {radiuses[i]} has an area of {areas[i]:.2f}")



if __name__ == "__main__":
    main()