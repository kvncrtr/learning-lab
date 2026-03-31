# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# pizzas = ['Neapolitan', 'Pepperoni', 'Cheese']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")
# print("I really love pizza!")    

# for rep in reps:
#     print(f"A {rep.title()} would make a great pet.")
# print("All of these are reptials and can serve as a pet.")
# reps = ['aligator', 'snake', 'lizard']

# # range of numbers
# for num in range(1, len(reps) + 1):
#     print(num)

# # list from a range method
# nums = list(range(1, 6))
# print(nums)

# # step by 5
# nums = list(range(0, 100, 5))
# print(nums)

# # squares
# squares = []
# for num in range(1, 11):
#     squares.append(num ** 2)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# # list comprehension
# squares = [value**2 for value in range(1, 11)]
# print(squares)

# # counting by 12
# twelves = list(range(0, 20, 12))
# print(twelves)

# # count to 1 million 
# million = list(range(1, 1000001))
# print(million)
# print(min(million))
# print(max(million))
# print(sum(million))

# one_to_twenty = list(range(1, 21, 2))
# for odd in one_to_twenty:
#     print(odd)

# # list of three
# list_three = list(range(3, 31, 3))
# print(list_three)

# # power of cube 
# cube_list = list(range(1,11))
# for cube in cube_list:
#     print(cube ** 3)

# # list comprehension

# cube_comp = [cube**3 for cube in range(1, 11)]
# print(cube_comp)


# # Slicing a list
# my_foods = ['pizza', 'falafel', 'carrot cake', 'ramen', 'gyro', 'tacos']
# my_go_tos = my_foods[:3]
# print(my_go_tos)
# print(my_foods[2:4])
# print(my_foods[4:])

# Pizza Slices
my_pizza = ['peperoni', 'margarita', 'cheese', 'white sauced']
friends_pizza = my_pizza[:]
my_pizza.append('italian sausage')
friends_pizza.append('hawaiian')
for pizza in my_pizza:
    print(f"\nMy pizzas are {pizza}.\n\n")
for pizza in friends_pizza:
    print(f"\nMy friend's pizzas are {pizza}.\n\n")
