from time import time

# Decorator
def performance(fn):
    def wrapper(*args, **kwargs):
      time1 = time()
      result = fn(*args, **kwargs)
      time2 = time()
      print(f"took {time2 - time1} s")
      return result
    return wrapper

@performance
def long_time():
    for i in range(9):
        i * 5

long_time()


user = {
  "name": "James",
  "age": 29
}

def check_user(*args, **kwargs):
  print(args[0])

check_user(user)


