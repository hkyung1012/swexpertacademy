data_str = "산 하늘 강 바다 하늘 강 들"

data_list = data_str.replace(" ",",").split(',')
data_list_new = []

for i in data_list:
    if i not in data_list_new:
        data_list_new.append(i)

print(','.join(sorted(data_list_new)))