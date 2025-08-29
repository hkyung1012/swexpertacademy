data_list = [10, 20, 30, 40, 50, 50, 50]

# 리스트 객체 내 데이터 유무
if 50 in data_list:
    print("True")
elif 50 not in data_list:
    print("False")

# 리스트 객체 내 데이터 갯수
print(data_list.count(50)) #3
print(data_list.count(100)) #0

data_list = list(range(0, 11, 2))
print(data_list)

for data in data_list:
    print(data, end=" ")

print() #개행

# 리스트를 enumeration 객체로 변환
#for idx, val in enumerate(data_list):
    #print(idx, val)

# 내포
data_list = list(range(1, 5))
data_list2 = []

for data in data_list:
    if data % 2 == 0:
        data_list2.append(data)

#  -> List comprehension
data_list3 = [data for data in data_list if data % 2 == 0]

print(data_list2 == data_list3) #True

# [for 중첩]
data_list4 = []
for x in data_list:
    if x % 2 == 1:
        for y in data_list:
            if y % 2 == 0:
                data_list4.append(x * y)

# -> List comprehension
data_list5 = [x * y for x in data_list if x % 2 == 1
                    for y in data_list if y % 2 == 0]

print(data_list4 == data_list5)

str = "HelLo-!"
data_list6 = [c.lower() for c in str]
print(data_list6) #['h', 'e', 'l', 'l', 'o', '-', '!']


