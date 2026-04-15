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

# Glossary
gloss_data = {
    'Multi-Paradigm': 'This is a fancy way of saying Python is flexible. It supports different "styles" of coding Object-Oriented (OOP) Organizing code into "objects" (great for large apps). Procedural:** Writing code as a sequence of steps (great for simple scripts). Functional:** Treating computation as the evaluation of mathematical functions.',
    'Methods': 'Built-in functions that ship with the programming laguage that have predefined inputs that produce predictable outputs',
    'Collections': 'A signle variable used to store multiple values e.g. list, sets, tuples',
    'Loops': 'Most DSA problems require iterating through arrays, strings, or repeating until a condition is met.',
    'Hash Maps': 'A way to store key → value, used for Countin, Lookups, Caching values'
}

for word, meaning in gloss_data.items():
    print(
        f"""
        ~~~~~~~~ Definition ~~~~~~~~
        - {word} noun
        : {meaning}

        | show {word} being used in a sentence.
        """
    )