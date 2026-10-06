"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a product.
# 2. Process:Store the product information in a dictionary, read it, change the price, remove the country field, and display every field with its value.
# 3. Out: The product information after the changes.
# 4. My object, my five fields, and why those: My object is a battery. My five fields are name, price, supplier, country, and stock. These fields are useful for identifying the product, its cost, its supplier, its origin, and its available quantity.

# Your code below

name = "Battery"
price = 120
supplier = "ABC Company"
country = "France"
stock = 500

print ("Name: " + name)
print ("Price: " + str(price))
print ("Supplier: " + supplier)
print ("Country: " + country)
print ("Stock: " + str(stock))

product = { "name": name, "price": price, "supplier": supplier, "country": country, "stock": stock}

print("Product dictionary: ", product)

# update the price field
product["price"] = 180

# remove the country field
country = product.pop("country")

print("Product dictionary after removing country field: ", product)
print("Removed country")

# display every field with its value

for key,value in product.items(): # 遍历
    print(key, ":", value)

print(product.get("weight", "Field not found"))