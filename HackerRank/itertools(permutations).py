from itertools import permutations as pt
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
    a = pt(b,r=k)

    for i in a:
        for j in i:
            print(j,end="")
        print()
