from datetime import datetime


# username = input("Enter your user name")
def logger(func):
    """
    Wrapper

    it dynamically shows username

    """

    def wrapper(*args, **kwargs):
        print(f"{args[0]} has called {func.__name__} at {datetime.now()} ")
        func(*args, **kwargs)
        print(f"{args[0]} has ended hello at {datetime.now()} ")

    return wrapper


@logger
def hello(username):
    print("hello ", username)


@logger
def goodbye(username):
    print("bye bye ", username)


@logger
def login(username):
    print("User is tryna login ", username)


@logger
def logout(username):
    print("User is tryna logout ", username)


hello("kamal")


if __name__ == "__main__":
    goodbye("ram")
    print("__name__ is ", __name__)
