# If Statements
cars = ['porche', 'maserati', 'tesla', 'lamborghini', 'mclaren']
print('tesla' in cars)
for car in cars:
    if len(car) >= 7:
        print('long')
    else:
        print('short')