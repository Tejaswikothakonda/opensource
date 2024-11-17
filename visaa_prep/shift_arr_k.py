n=int(input())
arr=list(map(int,input().split()))
k=int(input())
k=k%n
rot = arr[-k:] + arr [:-k]
print(" ".join(map(str,rot)))
