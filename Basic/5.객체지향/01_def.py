# https://swexpertacademy.com/main/learn/course/lectureVideoPlayer.do

def create(name, age):
    return {"name":name, "age": age}


def to_str(person):
    return "{0},{1}".format(person["name"], person["age"])

#딕셔너리 객체 3개를 항목으로 가진 members 리스트 객체 생성
members= [
    create("lee", 23),
    create("kim",12)
]

for member in members:
    print(to_str(member))