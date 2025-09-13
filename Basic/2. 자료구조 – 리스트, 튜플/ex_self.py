# 데이터 반환. index
data_list = list(range(10,60, 10))
#print(data_list.index(22)) #ValueError: 22 is not in list
print(data_list.index(20)) #1

#추가
data_list1 = list(range(1,6))
print(data_list1)
data_list1.append(6)
print(data_list1)
data_list1.insert(4,4)
print(data_list1)
data_list1.extend([7,8])
print(data_list1)
data_list1.append([9,10])
print(data_list1)


#제거
data_list2 = list(range(1,6))
idx = data_list2.index(2)
del data_list2[idx] # 2를 삭제
print(data_list2)

data_list2.remove(4)
print(data_list2)
data_list2.clear()
del data_list2[:]
print(data_list2)


#변경
data_list3 = list(range(10,60,10))
data_list3.reverse()
print(data_list3)
data_list3[3] = 100

#데이터 확인

print(data_list3.count(30))

# comprehens

data = list(data for data in data_list3 if data % 3 == 0)
print(data)

