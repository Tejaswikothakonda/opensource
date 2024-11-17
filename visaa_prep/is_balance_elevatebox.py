n = int(input())
arr=list(map(int, input().split()))
tot_sum = sum(arr)
left_weight = 0
Bal = []
for i in range(n):
    right_weight = tot_sum-left_weight-arr[i]
    Bal.append(abs(left_weight - right_weight))
    left_weight += arr[i]
print(*Bal)
    
