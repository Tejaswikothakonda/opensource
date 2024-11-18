n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
for i in range(n-2):
    if arr[i]<arr[i+1]+arr[i+2]:
        print(arr[i]+arr[i+1]+arr[i+2])
        break
else:
    print(-1)
