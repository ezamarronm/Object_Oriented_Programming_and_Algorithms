import time
import sys
sys.setrecursionlimit(1000000)

def iterative_factorial(n):
    ans = 1

    while n > 1:
        ans *=n
        n -=1
    return ans

def recursive_factorial(n):
    if n==1:
        return 1
    return n * recursive_factorial(n-1)

if __name__ == '__main__':
    n = 20000
    start = time.time()
    iterative_factorial(n)
    end = time.time()
    total = end - start
    print(total)

    start = time.time()
    recursive_factorial(n)
    end = time.time()
    total = end - start
    print(total)

