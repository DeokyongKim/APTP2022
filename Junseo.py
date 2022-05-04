def is_impli_two(a, b):                                 #minterm 2개가 implicant인지 판별
    A8 = a // 8
    A4 = (a % 8) // 4
    A2 = (a % 4) // 2
    A1 = (a % 2) // 1

    B8 = b // 8
    B4 = (b % 8) // 4
    B2 = (b % 4) // 2
    B1 = (b % 2) // 1
    print(A8, A4, A2, A1, B8, B4, B2, B1)

    dif = abs(A8 - B8) + abs(A4 - B4) + abs(A2 - B2) + abs(A1 - B1)
    if dif == 1:
        return 1
    else:
        return 0

def get_minterm_4vari():                                #변수가 4개일 때 값이 1인 minterm 받기
    minterm = []                                        # 1인 minterm의 list
    impli = []                                           # implicant가 모여있는 list

    print("값이 1인 midterm을 차례대로 입력하시오(종료시 -1) :")
    while True:
        i = int(input())
        if i == -1:
            break
        elif (i < 0) or (i > 15):
            print("0~16"
                  "5값을 다시 입력하세요")
            continue
        minterm.append(i)
        impli.append(i)                                 # 1개만으로 이미 implicant이므로 바로 추가한다.


