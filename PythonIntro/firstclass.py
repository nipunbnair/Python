class FirstClass:
    def __init__(self, value):
        self.value = value                                               # constructor

    def display(self):
        print(self.value)                                                # this pointer


v = FirstClass(3)
v.display()


def func():
    print("Hello")


class Myclass:
    """This is my second class"""
    a = 10


print(Myclass.a)
print(func())
print(Myclass.__doc__)
