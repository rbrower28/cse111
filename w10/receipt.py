""" This code reads a request, checks a list of products, and creates a reciept.
to function two csv files are required:
    - products.csv, formatted: "Product #,Name,Price"
    - request.csv, formatted: "Product #,Quantity"

prints both a list of all products and a list of requested items with quantity and price
"""

import csv

def main():

    print()
    print("Welcome to Ryansons Grocery Store!")
    print()

    try:
        
        # here you put the correct file directory to access "products.csv"
        products = read_products("products.csv") # <----
        
        """ displays the dictionary of products for visualization.
        UNCOMMENT THE FOLLOWING LINES TO SEE ALL PRODUCTS IN THE TERMINAL"""
        # print("Here is a list of our products:")
        # for p in products:
        #     print(f"{p} {products[p]}")
        # print()

        # here you put the correct file directory to access "request.csv"
        process_request("request.csv", products) # <----

    except FileNotFoundError as error:
        error = str(error).strip().split()
        filename = error[len(error) - 1]

        print(f"The filename or directory of {filename} is incorrect.\nPlease adjust it and try again.")

    except PermissionError:
        print("You do not have access to this file.")

    except KeyError:
        print("Error: item missing from request file")


def read_products(products_file):
    """ Reads the csv file "products.csv" and returns a dictionary
    with the first item of each line as the key and a list of the
    remaining two items in the line as the value.
    skips the first line to avoid using the titles.

    Example:
    csv line -- "D150,1 gallon milk,2.85"
    resulting key-value pair -- {"D150": ["1 gallon milk", 2.85]}

    Returns the complete dictionary
    """
    product_dict = {}

    # opens the file and sets it to a variable, converts file to a list of each line
    with open(products_file, mode="rt") as product_file:
        product_list = csv.reader(product_file)

        next(product_list) # skips the first line for titles

        for i in product_list:
            prod_num = i[0] # ex. D150
            prod_name = i[1] # ex. "1 gallon milk"
            prod_price = float(i[2]) # ex. 2.85

            # adds each line's values to the dictionary "product_dict"
            product_dict[prod_num] = [prod_name, prod_price] # ex. "D150 ['1 gallon milk', 2.85]"

    # returns the entire dictionary
    return product_dict

def process_request(request_file, products):
    """ Uses the file "request.csv" to search through the dictionary
    created from "products.csv". skips the first line for titles and
    if the requested item is in the products dict, prints the item,
    quantity, and price.

    Example:
    request -- "D150,2"
    prints -- "1 gallon milk: 2 @ 2.85"

    Returns nothing
    """

    # opens the request file and sets it as a variable, converts file to a list of each line
    with open(request_file, mode="rt") as request_file:
        request_list = csv.reader(request_file)
        
        next(request_list) # skips the titles on the first line
        print("Your cart:") # starts with a title

        prod_total = 0 # sets the total amount of items
        subtotal = 0 # sets the subtotal

        for i in request_list:
            prod_num = i[0] # ex. D150
            prod_quant = int(i[1]) # ex. 2

            if prod_num in products: # checks if the requested item is a real product
                prod_name = products[prod_num][0] # ex. "1 gallon milk"
                prod_price = float(products[prod_num][1]) # ex. 2.85

                # adds the number of items to the item total
                prod_total += prod_quant

                # adds the item price for the desired quantity to the subtotal
                subtotal += prod_quant * prod_price

                # prints the product name, amount requested and the product price
                print(f"{prod_name}: {prod_quant} @ ${prod_price}") # ex. "1 gallon milk: 2 @ $2.85"

            else: # if the requested product doesnt match with one on the list
                print(f"Input error: product {prod_num} not recognized")

    print()

    # displays the total amount of items purchased
    print(f"Your cart contains {prod_total} items")

    # displays the subtotal (without tax) under the product list
    print(f"Your subtotal is: ${subtotal:.2f}")

    # calculates and prints the amount of tax at a 6% rate
    tax = subtotal * .06
    print(f"Tax: ${tax:.2f}")
    print()

    # calculates the total and prints
    total = subtotal + tax
    print(f"Your total is: ${total:.2f}")

    # displays a short message with the date and time
    print("Thank you for shopping with Ryansons!\n"
            f"Cashier: Ryan  -  {get_time()}")
    print()



def get_time():
    # Import the datatime module so that
    # it can be used in this program.
    from datetime import datetime

    # Call the now() method to get the current date and
    # time as a datetime object from the computer's clock.
    current_date_and_time = datetime.now()

    # Format and print the current date and time to include
    # only the day of the week, the hour, and the minute.
    return f"{current_date_and_time:%A, %b %d %I:%M %p}"


if __name__ == "__main__":
    main()