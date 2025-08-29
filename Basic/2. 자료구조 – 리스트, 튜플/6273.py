#6273. [파이썬 프로그래밍 기초(2) 파이썬의 기본 응용] 2. 자료구조 -리스트, 튜플 1

# 국어, 수학 점수 -> 튜플로 저장
stu1 = (90, 80)
stu2 = (85, 75)
stu3 = (90, 100)
stu_list = [stu1,stu2,stu3]

for stu in stu_list:
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(stu_list.index((stu))+1, sum(stu), sum(stu)/2))


