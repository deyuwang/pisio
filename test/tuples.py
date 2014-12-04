#SICP [2.2.2~2.3.6)

from operator import getitem

pair = (1,2)

x, y = pair
print x, y

x = pair[0]
y = pair[1]

x = getitem(pair, 0)
y = getitem(pair, 1)

def makePair(x, y):
    def dispatch(m):
        if(m == 0):
            return x
        elif m == 1:
            return y
    return dispatch

def getitemPair(p, i):
    return p(i)

p = makePair(0, 1)
x = getitemPair(p, 0)
y = getitemPair(p, 1)

#Nested Pairs
p = ((1,2), (3,4))
print len(p)

#Recursive Lists
p = (1, (2, (3, None)))
print len(p)

emptyRlist = None
def makeRlist(first, rest):
    return (first, rest)

def first(s):
    return s[0]
def rest(s):
    return s[1]

def lenRlist(s):
    length = 0
    while s != emptyRlist:
        s = rest(s)
        length += 1
    return length


digits = (1, 8, 2, 8)
print digits[0:2] #(1,8)
print digits[1:] #(8, 2, 8)
