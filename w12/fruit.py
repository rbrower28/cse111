
from typing import ForwardRef


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(fruit_list)

    fruit_list.append("orange")
    print(fruit_list)

    apple_index = fruit_list.index("apple")
    fruit_list.insert(apple_index, "cherry")
    print(fruit_list)

    banana_index = fruit_list.index("banana")
    fruit_list.pop(banana_index)
    print(fruit_list)

    d = fruit_list.pop()
    print(d)

    fruit_list.sort()
    print(fruit_list)
    
    fruit_list.clear()
    print(fruit_list)


main()