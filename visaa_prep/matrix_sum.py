def res_arr(n,mat):
    res=[]
    for i in range(n):
        row_sum=sum(mat[i])
        col_sum=sum(mat[j][i] for j in range (n))
        res.append(row_sum+col_sum)
    print(" ".join(map(str,res)))
n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]
res_arr(n,mat)
        
