"""
https://www.youtube.com/watch?v=ymgm5ER6OuQ&list=PLsMufJgu5932XYejsOwcUDJ2F75f56nrl&index=8
* 선택 문제: n 개의 값 중에서 k 번째로 작은수 찾기
- Quick select O(N)
퀵 정렬 O(N \log N)과 유사한 아이디어를 사용하지만, 정렬을 모두 하지 않고 k번째 원소를
효율적으로 찾기 때문에 일반적으로 퀵 정렬보다 빠릅니다.
문제 해결의 핵심은 피벗(pivot)을 기준으로 데이터를 나누고,
피벗을 통해 k가 어느 위치에 있는지 파악하여 탐색 범위를 좁히는 것입니다.
 "비정렬된 리스트에서 $k$번째로 작은(혹은 큰) 원소 찾기"
탐색 과정:
피벗을 선택합니다.
피벗을 기준으로 데이터를 분할하여 피벗의 위치를 찾습니다.
만약 피벗의 위치가 k와 같다면 해당 값이 답입니다.
만약 피벗의 위치가 k보다 작다면, 피벗 오른쪽 부분에서 다시 k번째 원소를 찾습니다.
만약 피벗의 위치가 k보다 크다면, 피벗 왼쪽 부분에서 k번째 원소를 찾습니다.
이 과정을 재귀적으로 반복합니다.
11/09 다시 하기
"""


def quick_select(L, k):
    """
    Quick Select 알고리즘을 사용하여 리스트 L에서 k번째로 작은 원소를 찾습니다.
    k는 1부터 시작하는 순위입니다 (1 <= k <= len(L)).
    """

    # 1. 피벗 선택
    # 여기서는 리스트의 첫 번째 원소를 피벗으로 사용합니다.
    pivot = L[0]

    # 2. 리스트 분할 (Partition)
    A = []  # 피벗보다 작은 원소 (L: Less)
    M = []  # 피벗과 같은 원소 (E: Equal)
    B = []  # 피벗보다 큰 원소 (G: Greater)

    for x in L:
        if x < pivot:
            A.append(x)
        elif x == pivot:
            M.append(x)
        else:  # x > pivot
            B.append(x)

    # A와 M의 크기 계산
    len_A = len(A)
    len_M = len(M)

    # 3. k번째 원소 위치 확인 및 재귀 호출

    # Case 1: k번째 원소가 A에 있는 경우
    if k <= len_A:
        # A에서 k번째로 작은 원소를 찾기 위해 재귀 호출
        # (순위 k는 그대로 유지)
        return quick_select(A, k)

    # Case 2: k번째 원소가 M에 있는 경우 (피벗과 같은 경우)
    elif k <= len_A + len_M:
        # k번째 원소는 피벗(또는 피벗과 같은 값)임
        return pivot

    # Case 3: k번째 원소가 B에 있는 경우
    else:
        # B에서 (k - len_A - len_M) 번째로 작은 원소를 찾아야 함
        # 순위 k를 새로운 리스트 B에 맞게 조정
        new_k = k - len_A - len_M
        return quick_select(B, new_k)


# --- 예제 실행 ---
L = [3, 7, 8, 5, 2, 1, 9, 4, 6]
k = 4  # 4번째로 작은 원소
k_text = f"{k}번째"

# 알고리즘 실행
result = quick_select(L, k)
