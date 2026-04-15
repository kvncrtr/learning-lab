# Chapter 2
# Removing Whitespaces, var assignment, tabs new lines, and f-string 
name = 'There is no other name '
name = name.rstrip()
print(f"{name.upper()}:\n\tPeter\n\tJohn\n\tThomas")

# Removing prefixes
nostarch_url = 'apostle_paul.com'
nostarch_url = nostarch_url.removeprefix('apostle')
print(nostarch_url)

# Escaping a famous quote
quote = "Someone said \"The Earth is located the right distance from the Sun.\""
print(f"{quote} -- {name}")
another_name = ' Andrew '
print(another_name.rstrip())
print(another_name.lstrip())
print(another_name.strip())

file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))

print(3 ** 2)

universe_age = 14_000_000_000
print(universe_age)

MY_FAV_NUM = 7
print(f"My favorite number is {MY_FAV_NUM}")

""" 
comms = 'yes this is my comment'
print(comms) 
"""

GE = ['milk', 'eggs', 'water', 'yogurt']
'''
for food in GE:
    print(food.title())
'''

print("milk" in GE)
print(len(GE))
