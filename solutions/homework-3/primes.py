def primes_less_than(n) :
    """ Given an integer n, returns the list of primes less than n. """
    if type(n) is not int or n < 3 : return []
    # We use a sieve algorithm to
    # elimiane all multiples of
    # numbers in increasing order
    primes = [2]
    sieve = list(range(3,n,2)) # all odds less than n
    # We will remove all elemnts of the form
    # prime*(prime + 2k) wheren k = 0,1,...
    while len(sieve) > 0 :
        prime = sieve.pop(0)
        primes.append(prime)
        for x in range(prime**2, n, 2 * prime) :
            if x in sieve :
                sieve.remove(x)
    return primes

def int_sqrt(n) :
    """ If n > 0, returns the larges x with x**2 <= n. """
    assert n > 0
    # smallest integer less than n
    if type(n) is not int :
        m = int(n//1)
    else :
        m = n
    # We use Newton's method for the function
    # f(x) = x^2 - n. We start with x_0 = int(n)+1, and apply
    # x_{k+1} = x_k - f(x_k)/f'(x_k) = (x_k + n/x_k)/2
    prev, curr = 0, m
    while True:
        prev, curr = curr, (curr + m // curr) // 2
        # Notice that (curr + n//curr) // 2 is at most
        # 1 less than (curr + n/curr)/2.
        # Thus, by convexity, the first time we are
        # f(curr) is negative, we have out answer
        if curr**2 <= m :
            return curr

def primes_less_than_v2(n) :
    """ Given an integer n, returns the list of primes less than n. """
    if type(n) is not int or n < 3 : return []
    # We start wil all odd numbers less than n
    candidates = set(range(3,n,2))
    # For odd number x = 3, 5, ..., int_sqrt(n), we will
    # remove x^2, x(x+2), x(x+4),... < n from candidates.
    # Notice that we are removing only the odd ones.
    # Why this works : assume y = a*b with 1 < a <= b
    # and y < n, then a < int_sqrt(n), so y will be eliminated.
    for i in range(3, int_sqrt(n) + 1, 2) :
        candidates.difference_update(range(i**2, n, 2*i))
    candidates.add(2)
    return sorted(candidates)
