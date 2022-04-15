numbers = [1, 2, 3]

# unpacking operator
print(*numbers)

first, second, *numbers = numbers
print(first)


# values = list(range(5))
# conver to a list using unpack operator
values = [*range(5)]
print(values)


# Unpacking strings
chars = [*'Hello World']
print(chars)

# Unpacking and concatenating lists
first = [1, 2, 3]
second = [4, 5, 6]

third = [*first, *second]
print(third)
 
 # Unpacking and combining Dictionaries
firstDict = {"x": 1, "y": 2}
secondDict = {"z": 44}

combinedDict = {**firstDict, **secondDict, "a": 0}

print(combinedDict)