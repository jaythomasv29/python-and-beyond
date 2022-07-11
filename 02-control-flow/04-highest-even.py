def highest_even(nums):
  even_nums = []
  for n in nums:
    if(n % 2 == 0): even_nums.append(n)
  return(sorted(even_nums)[-1])
# or you can use to find max value in iterable max()

print(highest_even([10, 2, 3, 4, 8, 11]))

# print(max(7,9,29))