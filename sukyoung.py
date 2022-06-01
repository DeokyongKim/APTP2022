def get_2by2(table):
    ans = []

    if table == [[0, 0],
                 [0, 0]]:
        ans = []

    elif table == [[0, 0],
                   [0, 1]]:
        ans = [[[1, 1]]]

    elif table == [[0, 0],
                   [1, 0]]:
        ans = [[table[1][0]]]

    elif table == [[0, 0],
                   [1, 1]]:
        ans = [[table[1][0], table[1][1]]]

    elif table == [[0, 1],
                   [0, 0]]:
        ans = [[table[0][1]]]

    elif table == [[0, 1],
                   [0, 1]]:
        ans = [[table[0][1], table[1][1]]]

    elif table == [[0, 1],
                   [1, 1]]:
        ans = [[table[0][1], table[1][1]], [table[1][0], table[1][1]]]

    elif table == [[0, 1],
                   [1, 0]]:
        ans = [[table[0][1]], [table[1][0]]]

    elif table == [[1, 0],
                   [0, 0]]:
        ans = [[table[0][0]]]

    elif table == [[1, 0],
                   [0, 1]]:
        ans = [[table[0][0]], [table[1][1]]]

    elif table == [[1, 0],
                   [1, 0]]:
        ans = [[table[0][0], table[0][1]]]

    elif table == [[1, 0],
                   [1, 1]]:
        ans = [[table[0][0], table[1][0]], [table[1][0], table[1][1]]]

    elif table == [[1, 1],
                   [0, 0]]:
        ans = [[table[0][0], table[0][1]]]

    elif table == [[1, 1],
                   [0, 1]]:
        ans = [[table[0][0], table[0][1]], [table[0][1], table[1][1]]]

    elif table == [[1, 1],
                   [1, 0]]:
        ans = [[table[0][0], table[0][1]], [table[0][0], table[1][0]]]

    elif table == [[1, 1],
                   [1, 1]]:
        ans = [[table[0][0], table[0][1], table[1][0], table[1][1]]]

    return ans

print(get_2by2([[0,1],[1,1]]))


