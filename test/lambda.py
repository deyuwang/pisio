from operator import add

foo = lambda b : 2 * b

print map(foo, range(1, 3))
print filter(lambda x: x % 2 == 0, range(1, 10))
print reduce(add, range(1, 4))