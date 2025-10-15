#self 가 가리키는 객체의 필드 정보에 접근해 특정 목저의 기능을 수행하도록 정의된 메서드
#인스턴스 변수: 클래스 내에서 self 변수 형태를 가지는 변수
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} create".format(self.name))


    def __del__(self):
        print("{0} delete".format(self.name))

    def to_str(self): #Instance method
        return "{0},{1}".format(self.name, self.age)

members = [
    Person("lee", 20),
    Person("lee1", 21),
    Person("lee2", 22)
]

for member in members:
    print(member.to_str())


#lee create
#lee1 create
#lee2 create
#lee,20
#lee1,21
#lee2,22
#lee2 delete
#lee1 delete
#lee delete