class Dog(object):
    def __init__(self):
        self.name="旺财"
        print("Dog.__init__")
    def wangwang(self):
        print("wangwang")
class Person(object):
    def __init__(self):
        self.name="张三"
        print("Person.__init__")
    def __new__(cls, arg):
        print('__new__')
        ob = object.__new__(arg)
        ob.__init__()
        return ob
if __name__ == '__main__':

    p1 = Person(Dog)
    print(type(p1))
    # d1 = Dog()
    # d1.wangwang()
    p1.wangwang()
