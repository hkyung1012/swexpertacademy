data_set = set(range(10, 21, 2))
print(data_set)

data_set1 = {1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 11}
data_set2 = {2, 3, 5, 9, 11, 12, 15}

print(data_set1 & data_set2) #교집합
print(data_set1 | data_set2) #합집합
print(data_set1 - data_set2) #차집합
print(data_set2 - data_set1) #차집합

print(data_set1.intersection(data_set2)) #교집합
print(data_set1.union(data_set2)) #합집합
print(data_set1.difference(data_set2)) #차집합
print(data_set2.difference(data_set1)) #차집합

"""
{11, 2, 3, 5}
{1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 15}
{1, 4, 6, 7}
{9, 12, 15}
"""


data_set = set(range(3))
data_set.add(4)
data_set.add(4)
print(data_set) #{0, 1, 2, 4}
data_set.update({4, 5, 6})
print(data_set) #{0, 1, 2, 4, 5, 6}

