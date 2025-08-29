data_set = set( range(1, 11))

data_set.remove(9)
data_set.remove(2)

print(data_set) #{1, 3, 4, 5, 6, 7, 8, 10}

data_set.pop()  # 첫번째 항목 제거
print(data_set) #{3, 4, 5, 6, 7, 8, 10}

data_set.clear() #전체 제거

data_set1 = {1, 2, 3, 4, 5}
data_set2 = {2, 3}

# a가 b를 전부 포함하는 집합인지
print(data_set1.issuperset(data_set2)) #True
# a가 b에 전부 포함되는 집합인지
print(data_set2.issubset(data_set1))   #True
