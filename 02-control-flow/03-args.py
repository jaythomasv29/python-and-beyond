def multi_args(*args):
  '''
  A function that takes multiple arguments
  '''
  print(args)
  return sum(args)

print(multi_args(1,2,3,4,5))