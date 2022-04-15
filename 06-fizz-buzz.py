# if input is divisible by 3 -> return Fizz

# if input is divisible by 5 -> return Buzz

# if input is divisible by both 3 && 5 -> return FizzBuzz


# for everything else return the number passed in as args

def fizzbuzz(num):
    if(num % 5 == 0 and num % 3 == 0):
        return 'FizzBuzz'
    elif(num % 5 == 0 and num % 3 != 0):  # divisible by 5 only
        return 'Buzz'
    elif(num % 3 == 0 and num % 5 != 0):  # divisible by 3 only
        return 'Fizz'
    return num


print(fizzbuzz(3))  # divisible by 3 only 'Fizz'
print(fizzbuzz(15))  # divisible by 3 && 5 'FizzBuzz
print(fizzbuzz(25))  # divisible by 5 only 'Buzz'
print(fizzbuzz(7))