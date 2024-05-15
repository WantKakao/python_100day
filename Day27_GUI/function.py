def func1(a, b=2, c=3):
    print(a, b, c)


func1(1)
func1(1, 5)


def func2(*args):
    for a in args:
        print(a)


func2(3, 5, 6)


def func3(n, *args, t=7):
    print(type(args))
    for a in args:
        print(n+a)


func3(3, 5, 6, 1)


def func4(n=5, **kwargs):
    print(type(kwargs))
    print(kwargs)


func4(a=4)

my_dict = {"a":1, "b":2}
print(my_dict.get("a"))
print(my_dict.get("c"))
print(my_dict["a"])
