x,y,z = map(int, input().split())
tot_time = x*y
tot_avail_time = z * 1440
if tot_time <= tot_avail_time:
    print("YES")
else:
    print("NO")
