#사용자가 어떤 table을 줬다.
#table=[[1,0],
#       [1,1]]
#implicant=0
#
#for i in range(len(table)):
#    for j in range(len(table[i])):
 #         if table[i][j]==1:
#               if table[i][j+1]==1: #오른쪽 것도 1이면
 #
  #        else:
  #             break

ans=[]
table=input().split() #수정하기

if table==[[0,0],
           [0,0]]:
     ans=[]

elif table==[[0,0],
             [0,1]]:
     ans=[[table[1][1]]]

elif table==[[0,0],
             [1,0]]:
     ans=[[table[1][0]]]

elif table==[[0,0],
             [1,1]]:
     ans=[[table[1][0],table[1][1]]]

elif table==[[0,1],
             [0,0]]:
     ans=[[table[0][1]]]

elif table==[[0,1],
             [0,1]]:
     ans=[ [table[0][1],table[1][1]] ]

elif table==[[0,1],
             [1,1]]:
     ans=[ [table[0][1],table[1][1]], [table[1][0],table[1][1]] ]

elif table==[[0,1],
             [1,0]]:
     ans=[ [table[0][1]], [table[1][0]] ]

elif table==[[1,0],
             [0,0]]:
     ans=[[table[0][0]]]

elif table==[[1,0],
             [0,1]]:
     ans=[ [table[0][0]], [table[1][1]] ]

elif table==[[1,0],
             [1,0]]:
     ans=[ [table[0][0],table[0][1]] ]

elif table==[[1,0],
             [1,1]]:
     ans=[ [table[0][0],table[1][0]], [table[1][0],table[1][1]] ]

elif table==[[1,1],
             [0,0]]:
     ans=[ [table[0][0],table[0][1]] ]

elif table==[[1,1],
             [0,1]]:
     ans=[ [table[0][0],table[0][1]], [table[0][1],table[1][1]] ]

elif table==[[1,1],
             [1,0]]:
     ans=[ [table[0][0],table[0][1]], [table[0][0],table[1][0]] ]

elif table==[[1,1],
             [1,1]]:
     list=[ [table[0][0],table[0][1],table[1][0],table[1][1]] ]

print(ans)