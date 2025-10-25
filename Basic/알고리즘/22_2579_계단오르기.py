"""
https://www.acmicpc.net/problem/2579
점프 규칙: 계단은 한 번에 1칸 또는 2칸씩 오를 수 있습니다. (이것은 이전 문제와 동일합니다.)
연속 밟기 금지: 세 칸의 계단을 연속해서 밟을 수 없습니다.즉, $i$번째 계단을 밟았다면,
다음은 i+1 또는 i+2로 이동할 수 있지만, .., i-2, i-1, i 를 모두 밟는 것은 불가능합니다.
도착점 필수: 마지막 계단은 반드시 밟아야 합니다.

**"세 계단을 연속해서 밟을 수 없다"**는 제약 조건 때문에, i번째 계단을 밟았을 때 이전 상태가 무엇이었는지를 명확하게 구분
"""
import sys
sys.stdin = open("2579_input.txt", "r")

# 입력: 입력의 첫째 줄에 계단의 개수
# 출력: 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값

# 최대 점수를 계산하는 동적 계획법 함수 (단일 테스트 케이스 처리)
def solve_stair_climbing_case():
    try:
        n_line = sys.stdin.readline().strip()  # 입력의 첫째 줄
        if not n_line:
            return None # 더 이상 입력이 없으면 None 반환
        N = int(n_line)
    except:
        return None


    if N == 0:
        return 0

    # 계단점수 리스트
    scores = [0] + [int(sys.stdin.readline().strip()) for _ in range(N)]
            # for _ : **"반복 횟수는 필요하지만, 반복되는 동안의 각 순서(인덱스 또는 값)는 사용하지 않겠다"*

    # 예외처리 (N=1, N=2)
    if N == 1:
        return scores[1]

    if N == 2 :
        return scores[1] + scores[2]

    # --- DP 테이블 정의 및 초기화 ---
    # dp[0]은 사용하지 않음. dp[1] :1번째 계단의 최대 점수 정보 저장... dp[N]
    # dp[i][1]: i번째 계단을 밟았고, 직전에 1칸을 점프해 온 경우의 최대 점수
    # dp[i][2]: i번째 계단을 밟았고, 직전에 2칸을 점프해 온 경우의 최대 점수
    dp = [ [0] * 3 for _ in range(N + 1)]
         # [0, 0, 0] => 1 row  * (N+1) 
    
    #dp[i][0] 는 사용하지 않음. 의미상 1칸,2칸을 일치시키기 위해 [1][2]만 사용

    # 1번째 계단
    dp[1][1] = scores[1]
    dp[1][2] = scores[1]

    # 2번째 계단
    dp[2][1] = scores[2] + dp[1][1] # 1칸 점프: (1,2)
    dp[2][2] = scores[2]            # 2칸 점프: (2)

    # 점화식을 이용한 반복 계산 ( i =3 ~ N)
    for i in range(3, N + 1):
        # Case 1: i 번째 계단을 1칸 점프로 밟음 (i-1 -> i)
        # -> 연속 3칸 금지 규칙 때문에, i-1 은 반드시 i-3 에서 2칸 점프로 왔어야 함
        # (i-1 은 [2] 상태만 가능)
        dp[i][1] = scores[i] + dp[i-1][2]

        # Case 2: i번째 계단을 2칸 점프로 밟음 (i-2 -> i)
        # -> i-1을 건너뛰었으므로, i-2는 어떤 상태든 상관 없음.
        dp[i][2] = scores[i] + max(dp[i-2][1], dp[i-2][2])

    print(dp)
    return max(dp[N][1], dp[N][2])



solve_stair_climbing_case()