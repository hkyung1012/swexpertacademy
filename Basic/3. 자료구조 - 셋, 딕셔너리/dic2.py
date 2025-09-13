data_dic1 = {'hong':20, 'lee':11, 'kang':44}
# 변경
#data_dic1['kang'] = 40
#print(data_dic1)

#data_dic1.update({'hong':22, 'lee':10})
#print(data_dic1)

#제거
del data_dic1['hong']
print(data_dic1)

data_dic1.pop('lee')
print(data_dic1)

data_dic1.clear()