def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print ("Added sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print ("Added fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor: str = "vanilla", size: str = "meduim" ):
    print(f"Here is yours {size} size ice cream with {flavor}")

get_ice_cream( size = "large", flavor = "orange")
