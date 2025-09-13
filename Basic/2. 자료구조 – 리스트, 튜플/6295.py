
import sys
sys.stdin = open("ex_067_input.txt", "r")

row_col = [int(i) for i in input().split(',')] #행 ,열

data_list = list( [x*y for y in range(row_col[1])]
                       for x in range(row_col[0]))


print(data_list)
