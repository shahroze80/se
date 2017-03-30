# recursive implementation of nth fibionachi numbers
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)


# print first 10 fibionachi numbers
for i in range(1,10):
	print fib(i);


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print sum_digits(123);