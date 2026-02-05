# raw_input = input("input - ")
#
# inch = int(raw_input)
# cm = inch * 2.54
#
# print(cm)


format_a = "{}만원".format(5)
format_b = "{} {} {}".format(1,2,3)
print((format_a))
print((format_b))


format_c = "{:d}".format(50)
format_d = "{:5d}".format((100))
format_e = "{:10d}".format((100))

print((format_c))
print((format_d))
print((format_e))

format_c = "{:05}".format(55)
format_d = "{:05}".format(-55)
print((format_c))
print((format_d))

format_e = "{:g}".format((52.000)) # 소수점 제거
print((format_e))


data = ['a','2', 'M', 'YYYYY']
print("""name: {}, age : {}, lo: {}, year: {}""".format(*data)) #전개연산자
