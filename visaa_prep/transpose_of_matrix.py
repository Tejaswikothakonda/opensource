n = int(input())
mat=[]
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)
for i in range(n):
    for j in range(n):
        if j==n-1:
            print(mat[j][i])
        else:
            print(mat[j][i], end=' ')
