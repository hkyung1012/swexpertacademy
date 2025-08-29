
data_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]

print([data for data in data_list if data % 2 ==0])


#6286
datas=[1,1]
list(datas.append(datas[i-1] + datas[i]) for i in range(1,9)) #None

print(datas)



#6288
"""
리스트 내포 기능을 이용하여 1부터 20사이의 숫자 중 3의 배수가 아니거나
5의 배수가 아닌 숫자들의 제곱 값으로 구성된 리스트 객체를 출력하는 프로그램을 작성하십시오.
"""

data_list = list( pow(i,2) for i in range(1,21) if (i % 3 !=0) | (i % 5 != 0))
print(data_list)

#6289
"""
사용자가 숫자를 입력하면 숫자의 각 자릿수의 합을 구해서 반환하는 프로그램을 작성하십시오.
예를 들어 123을 입력하면 1 + 2 + 3 = 6의 결과를 반환합니다.
"""

text = str(12345)
text_list = list(int(c) for c in text)
print(sum(text_list))




