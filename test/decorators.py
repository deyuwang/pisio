
def tracel(fn):
    def warpped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return warpped

@tracel
def triple(x):
    return 3 * x

triple(12) #('->', <function triple at 0x020DECB0>, '(', 12, ')')