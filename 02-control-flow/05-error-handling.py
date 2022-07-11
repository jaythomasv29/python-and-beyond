# Error Handling
while True:
  try:
    age = int(input("What is your age? \n Age: "))
    print(10/age)
  except ValueError:
    print('Error, enter a valid age...')
  except ZeroDivisionError:
    print('Error, age cannot be 0...')
  else: 
    print('thank you')
    break