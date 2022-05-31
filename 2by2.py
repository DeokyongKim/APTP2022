# t 라는 list가 입력되었다고 간주
# 2 * 2 list임

def get_2by2(t):
    did = [['yet', 'yet'],
           ['yet', 'yet']]
    ans = []

    for i in range(2):
        for j in range(2):
            if t[i][j] == 1 and did[i][j] == 'yet':
                did[i][j] = 'done'
                small_ans = [[i, j]]

                # 상하좌우
                if t[(i-1+2) % 2][j] == 1:
                    if [(i-1+2) % 2, j] not in small_ans:
                        small_ans.append([(i-1+2) % 2, j])
                    did[(i-1+2) % 2][j] = 'done'
                if t[(i+1) % 2][j] == 1:
                    if [(i+1) % 2, j] not in small_ans:
                        small_ans.append([(i+1) % 2, j])
                    did[(i+1) % 2][j] = 'done'
                if t[i][(j-1+2) % 2] == 1:
                    if [i, (j-1+2) % 2] not in small_ans:
                        small_ans.append([i, (j-1+2) % 2])
                    did[i][(j-1+2) % 2] = 'done'
                if t[i][(j+1) % 2] == 1:
                    if [i, (j+1) % 2] not in small_ans:
                        small_ans.append([i, (j+1) % 2])
                    did[i][(j+1) % 2] = 'done'

                if len(small_ans) & (len(small_ans) - 1) == 0:
                    ans.append(small_ans)
                else:
                    while len(small_ans) & (len(small_ans) - 1) != 0:
                        index = small_ans.pop()
                        did[index[0]][index[1]] = 'yet'
                    if small_ans is not []:
                        ans.append(small_ans)

    return ans


print(get_2by2([[1, 1], [1, 0]]))
