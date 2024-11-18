def myFun(**kwargs):
    print(kwargs.get("firstname"))
    print(kwargs.get("secondname"))
    print(kwargs.get("thirdname"))
    print(kwargs.values())

    for v in kwargs.values():
        print(v)


myFun(firstname="Mahesh", secondname="Babu", thirdname="Rampatruni")


def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


example_function(name="Alice", age=30, city="New York")
