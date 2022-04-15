products = [
    ('shoe', 9),
    ('cap', 5),
    ('jeans', 60),
    ('socks', 3),
    ('jacket', 55)
]

filtered = filter(lambda item: item[1] > 5, products)
filtered = list(filtered)
print(filtered)

# list comprehension
# [expression for product in products if expression]
# [expression for product in products ]

prices_filtered = [product for product in products if product[1] > 5] # list comprehension for filter
prices = [product[1]+10 for product in products] # list comprehension for map

print(prices)

