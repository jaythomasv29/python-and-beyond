# for x in range(5):
#     for y in range(3):
#         print(f"{x} {y}")

# n = 99
# while n >= 0:
#     print(n)
#     n -= 1


# def greet(first_name, last_name=""):
#     print(f"hi {first_name} {last_name} welome to pyClub")


# greet('James')


def increment(num=2, by=3):
    return num + by


# xargs
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(2, 3, 4, 5))
