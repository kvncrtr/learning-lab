# Removing Whitespaces, var assignment, tabs new lines, and f-string 
name = 'There is no other name '
name = name.rstrip()
# print(f"{name.upper()}:\n\tPeter\n\tJohn\n\tThomas")

# Removing prefixes
nostarch_url = 'apostle_paul.com'
nostarch_url = nostarch_url.removeprefix('apostle')
# print(nostarch_url)

# Escaping a famous quote
quote = "Someone said \"The Earth is located the right distance from the Sun.\""
# print(f"{quote} -- {name}")
another_name = ' Andrew '
# print(another_name.rstrip())
# print(another_name.lstrip())
# print(another_name.strip())

file_name = 'python_notes.txt'
# print(file_name.removesuffix('.txt'))

# print(3 ** 2)

universe_age = 14_000_000_000
# print(universe_age)

MY_FAV_NUM = 7
# print(f"My favorite number is {MY_FAV_NUM}")

""" 
comms = 'yes this is my comment'
print(comms) 
"""

GE = ['milk', 'eggs', 'water', 'yogurt']
'''
for food in GE:
    print(food.title())
'''

# print("milk" in GE)
# print(len(GE))

# Chapter 3 
last_supper = ['john', 'peter', 'judas', 'nicodemus']

for disciple in last_supper:
    print(f"\n######### --- Message Sent @ 10:00AM 3/25/2026 \n\nHello, my dear beloved one {disciple.title()}\n\n")
# 
# Nico can't make it
print(f"\n@ @ @ @ @ --- Reply from {last_supper.pop(-1).title()} @ 10:46AM 3/25/2026 \n\nSorry brother can't make it tonight.\n\n")


# Nice, Andrew can make the last supper
last_supper.append('andrew')

# Found a bigger table message
for disciple in last_supper:
    print(f"\n######### --- Message Sent @ 11:00AM 3/25/2026 \n\nShalom Shalom {disciple.title()}, \n\nI was able to find a larger table for tonight. Let's break bread! \n\nPeace.\n\n")

# Inviting more guest to the last supper 
last_supper.insert(4, 'james')
last_supper.insert(5, 'philip')
last_supper.append('matthew')
print(last_supper)

# OOPS! the table wont be here
for disciple in last_supper:
    print(f"\n######### --- Message Sent @ 11:30AM 3/25/2026 \n\nHello {disciple.title()}, \n\nSorry about this but, I can only invite two of you over. \n\nCheers.\n\n")

while len(last_supper) > 2:
    del last_supper[-1]
    print(last_supper)

for disciple in last_supper:
    print(f"\n######### --- Message Sent @ 11:31AM 3/25/2026 \n\nThanks {disciple.title()} for coming tonight, see you there!\n\n")

# They came and had a good time for humanity, supper over
del last_supper[-1]
del last_supper[-1]
print(last_supper, "supper over, it's finished!")
