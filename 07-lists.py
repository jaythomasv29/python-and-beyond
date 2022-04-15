# list of strings
from calendar import c


letters = ["a", "b", "c", "d"]

# 2d list
matrix = [[0, 1], [2, 3]]

# a list with 100 elements of 0
zeros = [0] * 100
print(zeros)

# combining two lists
combined = zeros + letters
print(combined)

# list with numbers from 0-14
numbers = list(range(15))
print(numbers)

chars = list('Hello World')
print(chars)
print(len(chars))

# accessing items in a list
print(numbers[-1])
print(numbers[0])
chars[0] = 'Z'
print(chars)

# slicing a string with a new copy (end NOT inclusive)
print(chars[0:5])

# step over
print(numbers[1::2])
print(numbers[0::1])
print(numbers[-1::-1])

# unpacking lists
first, *other, last = numbers
print(last)
print(other)

# looping over lists
for idx, char in enumerate(letters, 100):  # get a tuple
    print(idx, char)

letters.append('z')
print(letters)
# append(), pop(), insert()
letters.insert(-1, 'x')

# Remove at end or (at given index)
letters.pop()
print(letters)

letters.remove('c')  # first occurance of thing that is passed in
del letters[0]  # delete at a specific index

# delete a range of items
del letters[0:2]

# delete all items in a list
# letters.clear()

letters2 = ['a', 'b', 'c', 'd', 'a', 'f', 'a']
if 'a' in letters2:
    print(letters2.index('c'))

print(letters2.count('a'))

# sort in descending vs ascending
numbers = [3, 41, 2, 8, 6]
numbers.sort(reverse=True)
# sorted
print(sorted(numbers, reverse=True))


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 1),
]


def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)




