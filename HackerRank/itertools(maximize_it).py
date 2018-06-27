
from itertools import product
K,M = map(int,input().split())
if K not in range(1,8) or M not in range(1,1001):
    pass
else:
    X = []
    flag = False
    for i in range(0,K):
        N = input()
        if int(N[0]) not in range(1,8):
            flag = True
            break
        N = N.split()
        del(N[0])
        for j in range(0,len(N)) :
            N[j] = int(N[j])**2
        X.append(N)
    if flag:
        pass
    else:
        X_list =  list(product(*X))
        sums = [sum(i)%M for i in X_list]
        print(max(sums))
