user = {
    'name': 'James',
    'age': 29,
    'color': 'Grey'
}

print(user.get('gender', 0))
print(user)

numbers = [9, 5, 3, 1, 4, 1, 6, 2, 4, 7, 9, 1]


def getMostFrequent(nums):
    count = {}
    most_repeated_num = nums[0]
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if(count.get(most_repeated_num, 0) < count.get(n, 0)):
            most_repeated_num = count.get(n, 0)
    return most_repeated_num


print(getMostFrequent(numbers))


# Dict methods
# print('gender' in user) # check if key exists in dict
# user.clear() # clears the dict in place
# user.copy() # copy a dict
# user.pop('color') # removes key/value in place
# user.update({'color': 'Blue'}) # update key/value
# user.keys()
# user.values() # grabs values
# user.items() #
