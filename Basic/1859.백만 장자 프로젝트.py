
import sys
sys.stdin = open("1859input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    result = 0

    N = int(input())
    n_list = list(int(x) for x in input().strip().split())
    maxidx_list = []

    i = 0
    while i < len(n_list):
        maxidx = n_list.index(max(n_list[i:]), i)
        maxidx_list.append(maxidx)
        i = maxidx + 1

    idx = 0

    if len(maxidx_list) > 0 :
        for j in range(0, len(n_list)):
            max_val = n_list[maxidx_list[idx]]
            if max_val == n_list[j]:
                idx += 1
                continue
            else:
                res = (max_val - n_list[j])
                if res > 0 :
                    result += (max_val - n_list[j])

    print(f"#{test_case} {result}")