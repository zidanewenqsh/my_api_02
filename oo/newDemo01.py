# class A:
#     def __new__(cls):
#         print("A new")
#         return object.__new__(cls)
#     def __init__(self):
#         print("A init")
#     def say(self):
#         print("hello A")

class A:
    def __new__(cls, obj=None):
        print("A2 new")
        if obj:
            return object.__new__(obj)
        return object.__new__(A)
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("B init")
    def say(self):
        print("hello B")

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print("C init")


class AA:
    def __new__(cls, obj=None):
        print("AA new")
        if obj:
            return object.__new__(obj)
        return object.__new__(A)


if __name__ == '__main__':
    a = A()
    print("*")
    b = B()
    print("*")
    c = A(B)
    # f1 = AA(A)
    # f1.say()
    # f2 = AA(B)
    # f2.say()
    # f3 = AA(C)
    # f3.say()
    # f4 = AA()
    # f4.say()