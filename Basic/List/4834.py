"""
1. 숫자 카운트:
0부터 9까지의 숫자를 세기 위한 10개의 크기를 가진 리스트(또는 배열)를 생성합니다.
2. 입력 처리:
입력받은 숫자들을 순회하면서 해당 숫자 인덱스의 카운트를 1씩 증가시킵니다.
3. 최댓값 찾기:
카운트가 가장 높은 숫자를 찾습니다. 이 숫자가 가장 많이 나온 숫자입니다.
4. 출력:
가장 많이 나온 숫자와 그 개수를 출력합니다.
"""

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a=list(map(int, list(input())))
    cnt_list = [0 for i in range(10)]
    for i in a:
        cnt_list[i] += 1
    max_num = 0
    max_cnt = 0
    for i in range(9, -1, -1):
        if(cnt_list[i]>max_cnt): max_cnt = cnt_list[i]; max_num = i;
    print("#%d %d %d" %(test_case,max_num,max_cnt))