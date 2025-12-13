def add_sprinkels(func):
    def wrapper():
        func()
    return wrapper

@add_sprinkels
def get_ice_cream():
    print("here is your ice cream")

get_ice_cream()