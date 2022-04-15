## when '**' is used, you can pass multiple key/value pairs as parameter
def save_user(**user):
    # automatically packaged into a dictionary
    print(user)

# automatically passed as a dictionary as args
save_user(id=1, name="James", age=22)

