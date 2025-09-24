# 다시 해보긴ㅁ
import sys
from collections import deque

sys.stdin = open('input.txt')


# 좌우상하 토마토 익힌다

def bfs(good):
    # 익힌 토마토 큐가 빌때까지 반복
    while good:

        sti, stj = good.popleft()

        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = sti + i, stj + j
            if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                tomato[ni][nj] = tomato[sti][stj] + 1
                good.append([ni, nj])


M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]
# deque로 받아준다. 시간효율 up
good = deque([])
res = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            good.append([i, j])

bfs(good)
for i in tomato:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
            # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작날짜를 1로 표현했으니 1을 빼준다.
print(res - 1)