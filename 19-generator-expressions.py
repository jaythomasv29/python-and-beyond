# generator objects don't store items in memory to save space
# generator objects do not have length
from sys import getsizeof

values = [x * 2 for x in range(1000)]
# for x in values:
    # print(x)

print('gen: ', getsizeof(values))
