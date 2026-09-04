# 28.
# Write a program that takes the price and quantity of a product and calculates the total cost.

# Display:

# Price: ...
# Quantity: ...
# Total: ...
# Use appropriate type conversion and an f-string.


product_name = input("Enter Your Product Name:")
product_price = float(input("Enter Product Price:"))
count = int(input("How Many Quantity You Want:"))
print(f"The Total Price You'll Pay Is {product_price * count}")