from math import prod


products = [
    ('shoe', 9),
    ('cap', 5),
    ('jeans', 60),
    ('socks', 3),
    ('jacket', 55)
]

prices = []

for product in products:
  prices.append(product[1])

# print(prices)

product_prices = sorted(list(map(lambda product: product[1], products)))
print(product_prices)

print(sorted(products, key=lambda key: key[1], reverse=True))


# Map with List comprehension  and sorted after
print('comp',sorted([product[1] for product in products], reverse=True))