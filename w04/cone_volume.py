"""Compute and print the volume of a right circular cone."""
print()
import math


def main():

    ex_radius = 2.8
    ex_height = 3.2
    ex_vol = cone_volume(ex_radius, ex_height)

    print("This program computes the volume of a right circular cone.")
    print(f"For example, if the radius of a cone is {ex_radius} and")
    print(f"the height is {ex_height}, then the volume is {ex_vol}")
    print()

    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    vol = cone_volume(radius, height)

    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:,.1f}")


def cone_volume(radius, height):
    volume = math.pi * radius**2 * height / 3
    return volume


main()