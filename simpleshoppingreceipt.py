# This is a simple shopping receipt program that calculates the total cost of items bought and checks if it is within the customer's budget.
item_name1 = 'Rice '
item_name2 = 'Beans'
item_name3 = 'Yam/s' 
item_price1 = 1.50
item_price2 = 2.30
item_price3 = 3.00
quantities = 3
budget = 200.00
customer_name = 'Alice'
total = (item_price3 * quantities)
within_budget = False
shopping_summary = f'{customer_name} bought {quantities} {item_name3} at ${item_price3} each, totaling ${total}.'

#Arithemetic operations
foot_ball = 5
foot_ball += 1

soccer_ball = 15
soccer_ball -= 2

tennis_ball = 20
tennis_ball *= 2

orange_juice = 10
orange_juice /= 2

houses = 4
houses **= 2

chairs = 10
chairs %= 3



print('BEST PRICES SHOPPING LIST RECEIPT')
print(input('What is your name? '))
print(input('What is your budget? '))
print(input('Name of item/s bought: '))
print(input('Number of quantities bought: '))
print(input('Price per item: '))
print(within_budget)
print(f'Total cost: ${total}')
print(shopping_summary)


print(foot_ball)
print(soccer_ball)
print(tennis_ball)
print(orange_juice)
print(houses)
print(chairs)