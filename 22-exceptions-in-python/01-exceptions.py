from distutils.log import error


numbers = [1, 2]
try:
    print(numbers[3])  # index error, because it is out of range
except IndexError:
    print('Number does not exist at specific index')

# exceptions - handling exceptions continue with execution to prevent crashing

# ^ execution is terminated


def get_age():
    age = ''
    while not age:
        try:
            age = int(input("Age: "))

        except (ValueError, ZeroDivisionError):
            print("You did not enter a valid age")
        else:
            return age


print(get_age())
