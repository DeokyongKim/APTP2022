def get_3by3(t):
    did = [['yet', 'yet'],
           ['yet', 'yet'],
           ['yet', 'yet'],
           ['yet', 'yet']]
    ans = []

    for i in range(4):
        for j in range(2):
            if t[i][j] == 1 and did[i][j] == 'yet':
                did[i][j] = 'done'
                small_ans = [[i, j]]

                # 상하좌우
                if t[i - 1][j] == 1:
                    small_ans.append([i - 1, j])
                    did[i-1][j] = 'done'
                if t[i + 1][j] == 1:
                    small_ans.append([i + 1, j])
                    did[i+1][j] = 'done'
                if t[i][j - 1] == 1:
                    small_ans.append([i, j-1])
                    did[i][j - 1] = 'done'
                if t[i][j + 1] == 1:
                    small_ans.append([i, j+1])
                    did[i][j + 1] = 'done'

                ans.append(small_ans)

    return ans
