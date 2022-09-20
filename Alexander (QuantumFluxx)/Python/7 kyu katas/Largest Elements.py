def largest(n,xs):
    return sorted(sorted(xs, reverse=True)[:n])