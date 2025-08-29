
text = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
remove_this = ('a','e','i','o','u')

print(''.join(list(c for c in text if c not in remove_this)))
# 리스트 a_comprehension은 각 문자가 따로 따로 떨어져있는 완성된 문장이 아니므로 join함수를 사용하여 서로 결합해 주어야됩니다.