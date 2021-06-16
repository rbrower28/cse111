"""Computes the storage efficiancy of a variety of can sizes"""
print()
from math import pi

def main():

    with open("cans.csv") as database:

        database.readline()
        names = []
        cost_efficiencies = []
        storage_efficiencies = []

        for line in database:
            line = (line.strip()).split(",")

            name = line[0]
            radius = float(line[1])
            height = float(line[2])
            cost = float(line[3].replace("$", ""))

            volume = cylinder_volume(radius, height)
            surface_area = cylinder_surface_area(radius, height)
            stor_efficiency = calc_storage_efficiency(volume, surface_area)
            cost_efficiency = calc_cost_efficiency(volume, cost)

            names.append(line[0])
            cost_efficiencies.append(cost_efficiency)
            storage_efficiencies.append(stor_efficiency)

            print(f"{name}")
            print(f"Storage efficiency: {stor_efficiency:.1f}")
            print(f"Cost efficiency: {cost_efficiency:.1f}")

        cost_index = cost_efficiencies.index(max(cost_efficiencies))
        name_cost_efficient = names[cost_index]
        storage_index = storage_efficiencies.index(max(storage_efficiencies))
        name_storage_efficient = names[storage_index]

        print()
        print(f"The most cost efficient can is {name_cost_efficient} with an efficiency of {max(cost_efficiencies):.1f}.")
        print(f"The most storage efficient can is {name_storage_efficient} with an efficiency of {max(storage_efficiencies):.1f}.")

def cylinder_volume(radius, height):
    return pi * radius ** 2 * height

def cylinder_surface_area(radius, height):
    return 2 * pi * radius * (radius + height)

def calc_storage_efficiency(volume, surface_area):
    return volume / surface_area

def calc_cost_efficiency(volume, cost):
    return volume / cost

main()
print()