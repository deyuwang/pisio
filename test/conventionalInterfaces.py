'''
SICP 2.3.7
@author: wdy
'''

def fib(k):
    prev, curr = 1, 1
    for _ in range(k - 1):
        prev, curr = curr, prev + curr
    return curr

def iseven(n):
    return n % 2 == 0

nums = (5, 6, -7, -8, -9)

print filter(iseven, nums)
print sum(map(abs, nums))

def sum_even_fibs(n):
    return sum(filter(iseven, map(fib, range(1, n+1))))

print sum_even_fibs(20)
