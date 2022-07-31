def divisors(n):
    return sum(1 for i in xrange(1, n + 1) if n % i == 0)