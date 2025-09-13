
# 변경]
data_list = [10, 20, 30, 40]

data_list[2] = 29
print(data_list)

#범위의 마지막 값은 실제 index 값이 아님
data_list[1:3] = [12, 15]
print(data_list)

data_list[1:3] = [12, 15, 20] #범위를 벗어난 값은 추가됨 -> 리스트 크기 변경됨
print(data_list)


#값 일부 제거
data_list = list(range(10, 110, 10))
print(data_list) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

del data_list[5:]
print(data_list) #[10, 20, 30, 40, 50]

data = data_list.pop(0)
print(data)      #10
print(data_list) #[20, 30, 40, 50]

data_list.remove(30)
print(data_list) #[20, 40, 50]

#값 전체 제거
data_list.clear()
del data_list[:]
