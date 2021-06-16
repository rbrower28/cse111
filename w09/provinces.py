""" used to edit and sort the information on provinces.txt """

def main():
    
    provinces = read_file("provinces.txt")

    print(provinces)

    provinces.pop(0)
    provinces.pop()

    alberta_count = 0

    for province in provinces:
        if province == "AB":
            province = "Alberta"

        if province == "Alberta":
            alberta_count += 1

    print(f"\nAlberta appears {alberta_count} times in the modified list.")

def read_file(filename):

    provinces = []
    
    with open(filename, mode="rt") as province_file:

        for line in province_file:
            provinces.append(line.strip())

    return provinces

if __name__ == "__main__":
    main()