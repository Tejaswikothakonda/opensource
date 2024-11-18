n=int(input())
arr=list(map(int,input().split()))
seen=set()
elem=[]
for x in arr:
    if x not in seen:
        elem.append(x)
        seen.add(x)
print(" ".join(map(str, elem)))
