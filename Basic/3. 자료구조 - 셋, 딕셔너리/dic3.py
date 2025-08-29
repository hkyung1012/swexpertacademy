data_dict1 = {
    'lee':10,
    'kim':20,
    'hong':30
}

#딕셔너리 항목이 있는 지 검사
print("'lee' in data_dict1 => {0}".format('lee' in data_dict1)) #True
print(f"'lee' in data_dict1 => {'lee' in data_dict1}") #True

print(f"'jang' not in data_dict1 => {'jang' not in data_dict1}") #True


print(f"{type(data_dict1.items())} {data_dict1.items()}")
#-> 튜플로 구성
#<class 'dict_items'> dict_items([('lee', 10), ('kim', 20), ('hong', 30)])

print(f"{type(data_dict1.keys())} {data_dict1.keys()}")
#-> 문자열로 구성
#<class 'dict_keys'> dict_keys(['lee', 'kim', 'hong'])

print(f"{type(data_dict1.values())} {data_dict1.values()}")
#-> 정수로 구성
#<class 'dict_values'> dict_values([10, 20, 30])


for item in data_dict1.items():
    print(f"{item[0]}, {item[1]}")

for key, value in data_dict1.items():
    print(f"{key}, {value}")

