import random

# Strings
nums = '01234567'
word = "hello world"
weather = 'It\'s sunny'
print(weather)
# Formatted Strings
print(f"{word}, {weather}!!!!")

# Slicing Strings
print(word[-5:])


# Iterate String
for char in word:
  print(char)
  
# Reverse a string
print(nums[::-1])

# Every other char in string
print(word[::2])

print(len(nums))

nums2 = nums[:] + 'a'
print(nums2)
print(nums)

def guessNumber():
  age = input('What is your age?')
  guesses = 0
  
  while True:
    guess_age = random.randint(1, 100)
    guesses +=1
    if guess_age == int(age):
      return guesses
    
# print(f"it took {guessNumber()} tries to guess your age")

def passwordChecker():
  user_password = input('Enter a password: \n')
  return(f"Your password {'*' * len(user_password)} is {len(user_password)} characters long")

print(passwordChecker())