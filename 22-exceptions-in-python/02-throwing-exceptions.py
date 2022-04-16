def calculate_xfactor(age):
    if age <= 0:
      raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
	calculate_xfactor(-22)
except ValueError as error:
	print(error)


