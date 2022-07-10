def my_decorator(func):
  def wrap_func(x):
    print('**' * 20 )
    func(x)
    print('**' * 20 )
  return wrap_func

@my_decorator
def hello(greeting):
  print(greeting)

# hello("hi James!")

# Example of decorators

user1 = {
    'name': 'Sorna',
    'valid': True
}
user2 = {
    'name': 'Viktor',
    'valid': False
}


def authenticated(func):
    def check_valid(*args, **kwargs):
        if args[0]['valid']:
            return func(*args, **kwargs)
        else:
            print('User not valid')

    return check_valid


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
message_friends(user2)