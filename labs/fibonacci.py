def fib_w(n):
    a,b = 0,1
    while b < n:        
        print(b,end=' ')
        a,b = b, a + b
        print()

def fib_r(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a ,b = b, a+b
    return result