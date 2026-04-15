# If Statements
cars = ['porche', 'maserati', 'tesla', 'lamborghini', 'mclaren']
print('tesla' in cars)
for car in cars:
    if len(car) >= 7:
        print('long')
    else:
        print('short')

# Conditional Test
car = 'Audi'
print(car.lower() == 'audi')

# Check inequality
requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print('Hold the anchovies')

# Numerical Comparison
age = 18
print(age == 18)

if age != 19:
    print('You are not 19yo, sorry.')

if age == 18 and isinstance(age, (int, float)):
    print('This is a number that\'s 18 and an integer NOT a string')

if age != 18 or isinstance(age, (int, float)):
    print('this is a number')
else:
    print('never got to the int')

# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapples']
print('mushrooms' in requested_toppings)
print('pepperonis' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'kevin'

if user not in banned_users:
    print(f"{user.title()} you can post on this page, if you wish.")

car = 'subaru'
print(f"Is {car == 'subaru'}? I predict True.")
print(car == 'subaru')

print(f"\nIs {car == 'audi'}? I predict false.")
print(car == 'audi')

# Chaining if else and if
age_0 = 12

if age_0 < 4:
    price = 0
elif age_0 < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# Usinf if statments with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for request in requested_toppings:
    if request == 'green peppers':
        print('Sorry, no more green peppers')
    else:
        print(f"Adding {request} to the pizza.")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print('Finihed making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!") 