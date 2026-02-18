#Decorator = a function that extends the behaviour of another function

def add_sprinkles(func):
    def wrapper(*argss, **kwargs):
        print("You add sprinkles")
        func(*argss, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*argss, **kwargs):
        print("You add fudge")
        func(*argss, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_icecream(flavour):
    print(f"Here is your {flavour} icecream")


get_icecream("vanila")