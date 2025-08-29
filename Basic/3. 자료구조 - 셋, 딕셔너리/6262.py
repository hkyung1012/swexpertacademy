text = "abcdefgabc"
dict_data = {}

for x in text:
    if x not in dict_data:
        dict_data[x] = 1
    else:
        dict_data[x] += 1

print(dict_data)
