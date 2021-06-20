""" This code reads a request, checks a list of products, and creates a reciept.
to function two csv files are required:
    - products.csv, formatted: "Product #,Name,Price"
    - request.csv, formatted: "Product #,Quantity"

prints both a list of all products and a list of requested items with quantity and price
"""

import csv

def main():
    
    # here you put the correct file directory to access "products.csv"
    products = read_products("cs111/w09/products.csv") # <----
    
    # displays the dictionary of products for visualization
    print("Products")
    for p in products:
        print(f"{p} {products[p]}")
    print()

    # here you put the correct file directory to access "request.csv"
    process_request("cs111/w09/request.csv", products) # <----


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
        print("Requested Items") # starts with a title

        for i in request_list:
            prod_num = i[0] # ex. D150
            prod_quant = int(i[1]) # ex. 2

            if prod_num in products: # checks if the requested item is a real product
                prod_name = products[prod_num][0] # ex. "1 gallon milk"
                prod_price = float(products[prod_num][1]) # ex. 2.85

                # prints the product name, amount requested and the product price
                print(f"{prod_name}: {prod_quant} @ {prod_price}") # ex. "1 gallon milk: 2 @ 2.85"

            else: # if the requested product doesnt match with one on the list
                print(f"Input error: product {prod_num} not recognized")


if __name__ == "__main__":
    main()