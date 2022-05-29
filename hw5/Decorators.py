def cache(f):
    def wr(*a):
        if a in dicti:
            return dicti[a]
        res = dicti[a] = f(*a)
        return res
    dicti = {}
    return wr

def fib(n):
    if n in (0,1):
        return 1
    return fib(n-1) + fib(n-2)

print(cache(fib(10)))