
data_str ="파이썬은 클래스를 이용해 객체를 생성하는 객체지향 프로그래밍 언어입니다."

#'객체' 단어 찾기
find_str = "객체"
print(data_str.find(find_str)) #return index> 14
print(data_str.find(find_str,15)) #return index> 23
print(data_str.rfind(find_str)) #return index> 23

print(data_str.find("객췌")) #-1

