
text = '12, 34, 56, 78'

text = text.replace(' ', '')

text_list = list(text.split(','))
text_tuple = tuple(text.split(','))
print(text_list)
print(text_tuple)