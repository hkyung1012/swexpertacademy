
"""
문제 해결 전략 (일반적인 접근 방식)
1. 정류장 배열 생성:
정류장의 위치를 나타내는 배열을 생성하고, 충전소의 위치를 표시합니다.
2. 최적 경로 탐색:
현재 위치에서 다음 충전 가능 지점까지 이동하면서, 충전을 최소화하는 방향으로 진행합니다.
3. "가장 멀리" 전략:
현재 위치에서 충전 가능한 최대 범위 내에 있는 충전소 중 가장 멀리 있는 충전소로 이동합니다. 이를 통해 충전 횟수를 최소화하고 종점까지 도달합니다.
4. 충전 횟수 계산:
이동 중 충전이 필요한 경우, 충전 횟수를 1 증가시킵니다.
5. 실패 조건:
현재 위치에서 다음 충전소까지 이동할 수 없는 경우, 즉 충전할 수 있는 정류장이 없으면 도달할 수 없습니다.
"""


import sys
sys.stdin = open("4831_input.txt", "r")
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

test_case = int(input())

def drive(K, N):
    car_bt = K
    cnt = 0
    current = 0
    for i in range(len(charge) - 1):
        distance = charge[i] - current
        current = charge[i]
        car_bt -= distance
        if charge[i + 1] - car_bt > current:
            cnt += 1
            car_bt = K

    return cnt


for tc in range(test_case):
    K, N, M = map(int, input().split())
    root = [0 for _ in range(N + 1)]

    charge = list(map(int, input().split()))
    charge.append(N)

    result = drive(K, N)

    for x in range(len(charge) - 1):
        if charge[x + 1] - charge[x] > K:
            result = 0

    print('#{} {}'.format(tc + 1, result))