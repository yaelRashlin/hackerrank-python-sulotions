'''
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
'''
def fibonacci(n):
    return fib_cach(n)
    
def fib_cach(n, cach = {}):
    if n in cach:
        return cach[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    val = fib_cach(n - 1, cach) + fib_cach(n - 2, cach)
    cach.setdefault(n, val)
    return val
    

n = int(input())
print(fibonacci(n))
