# Chapter 8 Functions
# git add .; git commit; git push;

# # Passing argument and functions definition
# def message(name):
#     print(f"""
#     ~~~~~~~~ Message ~~~~~~~~
#     Hey {name}, Im informing you that I am learning Python Crash Course 3rd Edition.
#     """)

# message('Jr')
# message('Jeri')
# message('Koren')
# message('Jesus')

# # 8-3 T-Shirt
# def make_shirt(material, size='L', message='I Love Python'):
#     print(f""" 
#         Shirt
#         * Price: FREE
#         * Shipping: $2.67
#         * Custom?: Yes
#         * Size: {size}
#         * Message: {message} 
#         * Made In: {material} 
#     """)

# make_shirt(
#     'Cotton',
#     'XL', 
#     'Walk in the spirit and you shall put off the flesh',
# )

# # 8-4 Large Shirts
# make_shirt(material='Cotton')
# make_shirt(size='M', material='Polyester')
# make_shirt(message='Touch the Heavans', material='Polyester')

# #8-5 Cities
# def describe_city(city, country='USA'):
#     print(f"""{city} is in {country}.""")

# describe_city('Barcelona', 'Spain')
# describe_city('New York')
# describe_city('Los Angeles')

# # 8-6 City Names
# def city_country(city, country):
#     return f"{city}, {country}"

# print(city_country('Destin', 'USA'))
# print(city_country('Queensland', 'Australia'))
# print(city_country('Oaxaca', 'Mexico'))

# # 8-7 Album
# def make_album(artist, title, number_of_songs=5):
#     data = {}
#     data['artist'] = artist
#     data['title'] = title
#     if number_of_songs >= 5:
#         data['number_of_songs'] = number_of_songs

#     return data

# print(make_album('Hillsong', 'Touch of Heaven', 1))
# print(make_album('Elevation', 'So Be It', 10))
# print(make_album('Red Rock Worship', 'Ascend', 19))

# # 8-9 Messages
# text = ['Love you too baby 💜', 'Babe I love you so much', 'Ok great', 'I got the email from Geico, also going to call around to 3 different credit unions to get some loan details']

# def show_message(messages):
#     for message in messages:
#         print(f"""Message sent: {message}
#         ________________________________
#               """)
        
# show_message(text[:])

# # 8-10 Messages
# wifey = ['Do they have a microwave?', 'Ahhh sorry baby', 'Maybe get something from the vending machine if they have any.']
# sent_messages = []

# def send_messages(text_messages):
#     while text_messages:
#         message = text_messages.pop(0)
#         print(f"""
#         Message Sent: 
#         {message}
 
#         ~~~~~~~~~~~~~~~~~~~~~~~~
#         """)
#         sent_messages.append(message)

# # send_messages(wifey[:])

# # 8-11 Archived Messages
# send_messages(wifey[:])
# print(wifey)

# # 8-12
# ordered = []

# def firehouse_subs(*contents):
#     ordered.append(contents)

# firehouse_subs('lettuce', 'ham', 'cheese')
# firehouse_subs('olive oil', 'pickels')
# firehouse_subs('salt', 'pepper', 'italian', 'smoke paprika', 'dry basil')
# print(ordered)

# # 8-13
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     print(user_info)
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# user_profile_me = build_profile('kevin', 'carter',
#                              location='atlanta',
#                              field='software engineering',
#                              married=True)
# print(user_profile_me)

# # 8-14
# def make_car(make, model, **car_specs):
#     car_specs['make'] = make
#     car_specs['model'] = model
#     return car_specs

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)