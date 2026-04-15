# CHAPTER 6
# git add .; git commit; git push;

# # Dictionary Def
# alien_0 = {'color':'green', 'points': 5}

# # Person I know
# koren = {
#     'first_name': 'Koren',
#     'last_name': 'Carter',
#     'age': 32,
#     'city': 'Atlanta'
# }

# for key, value in koren.items():
#     print(koren.get(key))

# # Favorite numbers
# favorite_numbers = {
#     'Koren': 7,
#     'Kevin': 3,
#     'Tina': 1,
#     'JR': 31,
#     'Leighton': 40
# }

# for name in favorite_numbers:
#     print(f"\n ~~~ Message ~~~ \nHey {name}, \n\nYour favorite number is {favorite_numbers[name]}\n")

# # Glossary
# gloss_data = {
#     'Multi-Paradigm': 'This is a fancy way of saying Python is flexible. It supports different "styles" of coding Object-Oriented (OOP) Organizing code into "objects" (great for large apps). Procedural:** Writing code as a sequence of steps (great for simple scripts). Functional:** Treating computation as the evaluation of mathematical functions.',
#     'Methods': 'Built-in functions that ship with the programming laguage that have predefined inputs that produce predictable outputs',
#     'Collections': 'A signle variable used to store multiple values e.g. list, sets, tuples',
#     'Loops': 'Most DSA problems require iterating through arrays, strings, or repeating until a condition is met.',
#     'Hash Maps': 'A way to store key → value, used for Countin, Lookups, Caching values'
# }

# for word, meaning in gloss_data.items():
#     print(
#         f"""
#         ~~~~~~~~ Definition ~~~~~~~~
#         - {word} noun
#         : {meaning}

#         | show {word} being used in a sentence.
#         """
#     )

# # Looping through all the Keys in a dictionary

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for name in sorted(favorite_languages.keys()):
#     print(name.title())

# # Looping through all values
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# for lang in sorted(favorite_languages.values()):
#     print(lang.title())

# # Nesting
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'purple', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien['color'])

# # People Nested

# koren = {
#     'first_name': 'Koren',
#     'last_name': 'Carter',
#     'age': 32,
#     'city': 'Atlanta'
# }

# kevin = {
#     'first_name': 'Kevin',
#     'last_name': 'Carter',
#     'age': 29,
#     'city': 'Atlanta'
# }
 
# tina = {
#     'first_name': 'Tina',
#     'last_name': 'Johnson',
#     'age': 58,
#     'city': 'Columbus'
# }

# people = [koren, kevin, tina]

# for person in people:
#     print(person)

# # Pets Nested
# dog = {
#     'type': 'Canidae',
#     'owner': 'Koren',
# }

# lizard = {
#     'type': 'Reptile',
#     'owner': 'Tina'
# }

# fish = {
#     'type': 'Nautical',
#     'owner': 'Kevin'
# }

# pets = [dog, lizard, fish]

# # 6-10 Favorite Numbers
# favorit_places = {
#     'kevin': ['church', 'business office', 'mexico'],
#     'koren': ['beach', 'shopping mall', 'church'],
#     'tina': ['church', 'coffee shop', 'shopping']
# }

# favorite_numbers = {
#     'Koren': [7, 11, 12],
#     'Kevin': [3, 8, 40],
#     'Tina': [1, 7, 12],
#     'JR': [31, 1, 3],
#     'Leighton': [40, 2, 4]
# }

# for person, nums in favorite_numbers.items():
#     print(f"""Hey {person},
#         your favorite numbers are:""")
#     for number in nums:
#         print(number)

# # 6-11 Cities
# cities = {
#     'manhattan': {
#         'country': 'United States',
#         'population': '1,664,214',
#         'fact': 'The island was purchased from the Lenape people in 1626 for goods worth roughly $1,200 today.',
#     },
#     'berlin': {
#         'country': 'Germany',
#         'population': '3,584,240',
#         'fact': 'Berlin has the highest population within city limits of any city in the European Union.',
#     },
#     'barcelona': {
#         'country': 'Spain',
#         'population': '1,620,000',
#         'fact': 'The Sagrada Familia, its most famous landmark, has been under construction for over 140 years.',
#     },
# }

# for city, info in cities.items():
#     num = info['population'].replace(',', '')
#     print(f"""
#     {city.title()}
#     * Found In: {info['country']}
#     * Population: {int(num)}
#     * {info['fact']}
#     """)