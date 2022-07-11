from functools import reduce


l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
# for ele in enumerate(l1):
#     print (ele)

# for n in range(12, 0, -1):
#   print(n)

my_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = reduce(lambda a, b: a + b, my_nums)
print(sum)

i = 0
while i < 10:
  print(i)
  i+=1