imp =

for i in range(2):
    for j in range(4):
        for k in range(4):
            if arr[i][j][k] == 1:
                if arr[i+1][j][k] == 1:

                if arr[i-1][j][k] == 1:

                if arr[i][j+1][k] == 1:

                if arr[i][j-1][k] == 1:

                if arr[i][j][k+1] == 1:





"""
# 길이,0:가로/1:세로,좌표
n = int(input())
for i in range(n):
  l, d, x, y = map(int, input().split())
  for j in range(l):#격자판 좌표 원점은 1,1 / 리스트 원점은 0,0 // d가 0이면 가로로 증가 1이면 세로로 증가
     if d == 0:
         m[x-1][y-1+j] = 1
     else:
         m[x-1+j][y-1] = 1

#격자판 출력
for i in range(h):
  for j in range(w):
    print(m[i][j], end=' ')
  print()
"""