# Sets - no order, contains only unique, they can perform operations
# can check (n in num) , but not access using numbers[1] (using an index)

numbers = [1, 1, 2, 1, 3, 4]

first = set(numbers)

second = {1, 4}


print(first | second) # union of two sets

print(first & second) # inner section, all items in BOTH sets

print (first - second) # the difference between two sets

print(first ^ second) # symmetric difference in the first OR second set, both not in BOTH
