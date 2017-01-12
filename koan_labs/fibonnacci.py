def fibonacci(args):
    a=1
    b=1
    fibo = [0,1,1]
    while args >= len(fibo):
        c = a + b
        a=b
        b=c
        fibo.append(c)
    return tuple(fibo)

fibonacci(7)