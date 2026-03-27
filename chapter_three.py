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


# Sort method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
# print(cars)

print(f"\nHere is a list that is not sorted:\n{cars}\n\n")
print(f"Here is a list that is sorted:\n{sorted(cars)}\n\n")
print(f"Here is a list AFTER sort:\n{cars}")

# length of lists
print(len(cars))

# Places I would like to visit
vacay = ['the maldieves', 'london', 'japan', 'barcelona', 'vancouver']
print(vacay)
print(sorted(vacay))
print(vacay)
vacay.sort(reverse=True)
print(vacay)
vacay.sort(reverse=True)
print(vacay)
vacay.sort()
print(vacay)
vacay.sort(reverse=True)
print(vacay)

print(len(last_supper))