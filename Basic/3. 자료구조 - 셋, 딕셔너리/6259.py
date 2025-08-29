text = "hello world! 123"


DIGITS_cnt = 0
LETTERS_cnt = 0

for x in text:
    if x.isdigit():
        DIGITS_cnt += 1
    elif x.isalpha():
        LETTERS_cnt += 1


print(LETTERS_cnt)
print(DIGITS_cnt)



