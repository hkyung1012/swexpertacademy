"""
https://2jinishappy.tistory.com/127
Quick Select를 진행하면서 선정한 pivot이 너무 작거나 크다면,
partitioning이 제대로 이루어지지 않아 Worst-Case에 O(n²)이 소모됨을 확인했다
그렇기 때문에, Quick Select의 성능은 'good pivot을 얼마나 빨리 찾아내느냐'에 달려있다
이번에 다룰 Median of Medians 알고리즘은 good pivot을 worst-case O(n)에 찾아내는 알고리즘이다.
"""

