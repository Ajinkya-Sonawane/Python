"""
    Find the problem here : https://www.hackerrank.com/challenges/list-comprehensions/problem
"""
from itertools import product
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    X = list(range(0,x+1))
    Y = list(range(0,y+1))
    Z = list(range(0,z+1))
    m = [X,Y,Z]
    solution = []
    m = list(product(*m))
    for i in m:
        if sum(i) != n:
            solution.append(list(i))

    print(solution)
