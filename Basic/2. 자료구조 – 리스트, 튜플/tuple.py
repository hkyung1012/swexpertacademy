data_tuple = tuple(range(1, 6))
print(data_tuple)

data_tuple2 = tuple(range(0, 11, 2))

for data in data_tuple2:
    print(data, end = " ")

print()

for idx, value in enumerate(data_tuple2):
    print(idx,value)
