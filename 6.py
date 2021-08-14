a=int(input())
b=[[None for i in range(a)]for j in range(a)]
for i in range(a):
    b[i][0]=1
for i in range(a):
    b[i][i]
for i in range(2,a):
    for j in range(a):
        b[i][j]=b[i-1][j-1]+b[i-1][j-1]
for i in range(a):
    for j in range(i+1):
        print(b[i][j],end="\t")
    print()
