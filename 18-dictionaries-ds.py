# A collection of key value pairs

# Examples: a phone book
# {name: 'number'}


phone_book = {"name": "James", "number": 4081231234}

point = dict(x=1, y=2)

print(point["x"])


print(point.get('a', 0))

del point['x']
print(point)

for contact in phone_book:
    print(phone_book)

# Dict comprehensions

# values = []
# for x in range(5):
#     values.append(x * 2)

# print(values)

# values_added = [ num*10 for num in range(5)] # list comprehension
print([num * 2 for num in range(5)])

# Using Dict Comprehensions

values = {x: x*2 for x in range(5)}
print(values) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}


