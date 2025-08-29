
import sys
sys.stdin = open("ex_075_input.txt", "r")
#1, 2, 3, 4, 5

data_list = [ data for data in input().replace(" ","").split(',') if int(data) % 2 != 0 ]
print(', '.join(data_list))

#6298
tuple_list = (1,2,3,4,5,6,7,8,9,10)
mid = len(tuple_list) // 2

print(tuple_list[:mid])
print(tuple_list[mid:])

# 6300
input_list = [12, 24, 35, 70, 88, 120, 155]

data_list = list( data for data in input_list if input_list.index(data) % 2 != 0)
print(data_list)

#6302
remove_idx = [0, 4, 5]

data_list = list( data for data in input_list if input_list.index(data) not in remove_idx)
print(data_list)


#6303
list1 = [1, 3, 6, 78, 35, 55]
list2 = [12, 24, 35, 24, 88, 120, 155]

data_list = list( data for data in list1 if data in list2)
print(data_list)


#6305
list1 = [12,24,35,24,88,120,155,88,120,155]

def remove_dup(param_list):
    rtn_list = []
    list( rtn_list.append(data) for data in param_list if data not in rtn_list)
    return rtn_list

print(remove_dup(list1))

