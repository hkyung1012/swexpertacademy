'''
리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
입력된 값 [10, 10, 20, 30, 40]의 평균은 22.0입니다.
'''

import sys
from sys import stdin

sys.stdin = open("ex_024_input.txt", "r")
data_list = [int(input()) for i in range(1,6)]

print('입력된 값 {0}의 평균은 {1:.1f}입니다.'.format(data_list, sum(data_list)/5))
