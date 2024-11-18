n=int(input())
for i in range(1, n+1):
    l=''.join(str(x) for x in range(1, i + 1))
    r=''.join(str(x) for x in range(i, 0, -1))
    print(l+' '*(2 * (n - i)) + r)
