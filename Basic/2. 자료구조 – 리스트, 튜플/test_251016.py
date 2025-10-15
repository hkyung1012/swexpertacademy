#List test
def reset():
    return [1, 2, 3, 4]

#list 의 index 범위!. 마지막 값은 실제 index 아님!!
dataList = [1,2,3,4]
dataList[1:3] = [33,44]
print(dataList) #[1, 33, 44, 4]

dataList = reset()
print(dataList)

