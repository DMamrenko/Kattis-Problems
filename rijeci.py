def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
                return (c, d)
        else:
                return (d, c + d)
iterations = int(input())
answer = _fib(iterations-1)
print(answer[0], answer[1])

