from cgi import print_form
import math

print('my first python line of code')
print("*" * 20)

rating = 4.99
is_published = False
course_name = "Python Programming"
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
# copy of original name
course_name_copy = course_name[:]
print(course_name_copy)

first = "James"
last = "Vongampai"

full_name = f"{first} {last}"
print(full_name)


# string methods
print(first.upper())  # returns a new string, does not change original
print(course_name.title())  # capitalizes
print(first)

print(course_name.split(" "))
print(course_name.find("m"))
print("P" in course_name)
print("ga" not in course_name)

# integers and floats
x = 1.1
print(x)
print(10 / 3)
print(10 // 4)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x += 3
print(x)

# round to closest num
print(round(2.9))
# abs val
print(abs(-3))


print(math.sqrt(9))
factorial = math.factorial(4)
print(factorial)


# inputs
x = input("x: ")
# type conversion int(x) float(x) bool(x)
y = int(x) + 1
print(y)

print(type(x) == 'str')


# Falsy
# "" - False
# 0 - False
# None - False (empty value)
print(0 == False)
print(bool(1))
print(bool(" ")) # True

# primitive - number, bool, string
fruit = "Apple"
print(fruit[1])

