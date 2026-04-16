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

# 8-3 T-Shirt
def make_shirt(size, message, material):
    print(f""" 
        Shirt
        * Price: FREE
        * Shipping: $2.67
        * Custom?: Yes
        * Size: {size}
        * Message: {message} 
        * Made In: {material} 
    """)

make_shirt(
    'XL', 
    'Walk in the spirit and you shall put off the flesh',
    'Cotton')

make_shirt(
    message='Walk in the spirit and you shall put off the flesh',
    size='L', 
    material='Cotton')