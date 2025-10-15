#객체의 생성과 소멸, 그리고 self

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} created.".format(self.name))

    def __del__(self):
        print("{0} deleted.".format(self.name))

member = Person("lee", 30)


