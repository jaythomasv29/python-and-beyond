products = [
    ('shoe', 9),
    ('cap', 5),
    ('jeans', 60),
    ('socks', 3),
    ('jacket', 55)
]

products.sort(key=lambda prod: prod[1], reverse=True)
print(products)


# basic example of a function to square
def square(num):
    return num*num


result = square(5)

a=lambda num: num*num


add = lambda a,b : a+b

result = add(5,6)
print(result)