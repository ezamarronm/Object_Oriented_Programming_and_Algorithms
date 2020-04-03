def f(x):
    ans = 0
    for i in range(1000):
        ans +=1
    for i in range(x):
        ans +=x
    for i in range(x):
        for j in range(x):
            ans +=1
            ans +=1
    return ans
        
# This algorithm has a complexity of 2x**2 + x + 1002
# similar to O(x**2)