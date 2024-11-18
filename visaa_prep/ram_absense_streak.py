n=int(input())
att=list(map(int,input().split()))
curr_abs=0
max_abs=0
for x in att:
    if x == 0:
        curr_abs += 1
    else:
        max_abs=max(max_abs,curr_abs)
        curr_abs=0
max_abs=max(max_abs,curr_abs)
print(max_abs)
