# Ternary operator
print('Hot' if 10 > 3 else 'Cold')

age = 22
# if age >= 18:
#   print('Eligible')
# else:
#   print('Not Eligible')

message = 'Eligible' if age >= 18 else 'Not Eligible'
print(message)

high_income = True
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not qualified")


if 18 <= age < 65:
    print('In age range')

    print("bag" > "cat")

for n in range(5):
  print('Attempt', n)
  if(n > 2):
      print('reached higher than', n)
  else:
    print('less than target')


