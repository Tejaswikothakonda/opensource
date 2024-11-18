n=int(input())
mat=[]
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
for row in mat:
    print(' '.join(map(str, row[::-1])))
