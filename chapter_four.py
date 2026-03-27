'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

pizzas = ['Neapolitan', 'Pepperoni', 'Cheese']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")    

for rep in reps:
    print(f"A {rep.title()} would make a great pet.")
print("All of these are reptials and can serve as a pet.")
reps = ['aligator', 'snake', 'lizard']

# range of numbers
for num in range(1, len(reps) + 1):
    print(num)

# list from a range method
nums = list(range(1, 6))
print(nums)

# step by 5
nums = list(range(0, 100, 5))
print(nums)

# squares
squares = []
for num in range(1, 11):
    squares.append(num ** 2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
'''

squares = [value**2 for value in range(1, 11)]
print(squares)