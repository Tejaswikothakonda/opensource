s=input()
ans=''
for i in s:
    if 97 <=ord(i)<=122:
        ans += chr(ord(i)-32)
    if 65 <=ord(i)<=90:
        ans += chr(ord(i)+32)
print(ans)
