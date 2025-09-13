data_tuple = ( ('lee',20), ('kim',45), ('kang',11) )
data_dic = dict(data_tuple)

data_list = [ ('lee',20), ('kim',45), ('kang',11) ]
data_dic = dict(data_list)

data_set = { ('lee',20), ('kim',45), ('kang',11) }
data_dic = dict(data_list)
print(data_dic) #{'lee': 20, 'kim': 45, 'kang': 11}

data_dic1 = {
    'lee' :20,
    'kim' : 45,
    'jang' : 35
}

print(f"{data_dic1['lee']}") #20

data_dic1['eun'] = 40
print(data_dic1)

#update함수에 dic 객체를 전달하면 새로운 항목으로 추가됨
data_dic1.update({'sin':11, 'won':23})
print(data_dic1) 


