from itertools import combinations as cb
s = input()
s.upper()
a = s.split(" ")
k = int(a[1])

if k not in range(1,len(a[0])+1):
    pass
else:
    b = []
    for i in a[0]:
        b.append(i)
    b.sort()
    for num in range(1,k+1):
        a = cb(b,r=num)

        for i in a:
            for j in i:
                print(j,end="")
            print()
