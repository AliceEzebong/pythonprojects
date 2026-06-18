# Step 1: Store the prices
rice = 850
beans = 120
beef =  900
milk = 50
discount = 0.1


# Step 2:Calculate the total
total = rice + beans + beef + milk

# Step 3: Print each item price
print('SHOPPING LIST')
print(f'Rice:  ₦{rice}')
print(f'Beans:  ₦{beans}')
print(f'Beef:  ₦{beans}')
print(f'Milk:  ₦{milk}')
print(f'Discount: {discount * 100}%')

# Step 4: Print the total
print(f'Discount applied:   ₦{total * discount}')
print(f'your total purchase is  ₦{total}')


