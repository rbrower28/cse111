print()
import math

num_items = int(input("How many items are there? "))
per_box = int(input("How many will you pack per pox? "))

num_boxes = num_items / per_box
if num_items % per_box > 0:
    num_boxes = math.ceil(num_boxes)

print(f"For {num_items} items, packing {per_box} items in each box, you will need {num_boxes:.0f} boxes.")
print()