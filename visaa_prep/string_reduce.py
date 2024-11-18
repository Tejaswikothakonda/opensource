string=input()
red_str=""
count=1
for i in range(1, len(string)):
    if string[i]==string[i-1]:
        count+=1
    else:
        red_str += string[i-1]+str(count)
        count=1
red_str += string[-1]+str(count)
print(red_str)
