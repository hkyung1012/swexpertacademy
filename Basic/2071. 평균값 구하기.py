
import sys
sys.stdin = open("2071_input.txt", "r")
#10개의 수를 입력 받아, 평균값을 출력 (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
for test_case in range(1, T + 1):
    data_list = list( int(x) for x in input().split())
    avg_val =sum(data_list) / len(data_list)

    print(f"#{test_case} {avg_val:.0f}")