v,c =  input().split()
if v not in {'R', 'P', 'S'} and c not in {'R', 'P', 'S'}:
    print("Enter valid input")
else:
    if (v=='R' and c == 'P') or (v=='P' and c=='S') or (v=='S' and c == 'R'):
        print("Charan")
    elif (c=='R' and v=='P') or (c=='P' and v=='S') or (c=='S' and v=='R'):
        print("Vignesh")
    else:
        print("NULL")
