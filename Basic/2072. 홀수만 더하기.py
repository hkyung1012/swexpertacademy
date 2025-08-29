
import sys
sys.stdin = open("2072_input.txt", "r")
#  홀수만 더한 값을 출력

def func_sum(param):
    result = 0
    for x in param:
        if x % 2 != 0:
            result += x
    return result

T = int(input())
for test_case in range(1, T + 1):

    data_list = list(int(x) for x in input().split())
    sum = func_sum(data_list)

    print(f"#{test_case} {sum}")