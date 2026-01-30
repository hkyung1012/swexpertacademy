num = list(range(11))  # 0 ~ 10

while True:
    try:
        index = int(input("배열의 인덱스를 입력하시오: "))
        print(num[index])

    except IndexError:
        print(-1)
    except value    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
        break
