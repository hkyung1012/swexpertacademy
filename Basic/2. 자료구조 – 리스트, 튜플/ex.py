#시퀀스형: 순서를 가진 리스트,튜플

data_list = list(range(10, 60, 10))
print(data_list) #[10, 20, 30, 40, 50]

data = 20
print(data_list.index(data)) #1 -> 인덱스 반환

data_list1, data_list2 =[10, 20, 30], [40, 50]
print(data_list1 + data_list2) #[10, 20, 30, 40, 50] -> 이어붙이기
print(data_list2 * 3) #[40, 50, 40, 50, 40, 50]

# 값 추가
print(data_list1.append(50)) #None -> 반환값이 없음
print(data_list1) #[10, 20, 30, 50]

# index 위치에 값 추가
data_list1.insert(3, 40)
print(data_list1) #[10, 20, 30, 40, 50]

# list 형태로 값 추가
data_list1.extend([60, 70])
print(data_list1) #[10, 20, 30, 40, 50, 60, 70]

# list 항목을 추가
data_list1.append([80,90])
print(data_list1) #[10, 20, 30, 40, 50, 60, 70, [80, 90]]

