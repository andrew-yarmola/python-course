import random

def binary_decimal(m,n) :
    """ Given integers 0 <= m <= n, n != 0, yields
    the (shortest) binary decimal expansion of m/n """
    assert ( isinstance(m, int) and isinstance(n, int) and 
             0 <= m <= n and n != 0 )
    rest = m
    while rest != 0 :
        rest *= 2
        coeff = rest // n
        yield coeff
        rest -= coeff * n
    

def biased_coin(m,n) :
    """ Using random.randint(0, 1) as a fair coin, this
    returns 1 with probablity m/n, where m,n must be
    non-negative integers with m <= n. """
    # binary_decimal checks m,n for us
    bin_dec = binary_decimal(m,n)
    for x in bin_dec :
        if x != random.randint(0, 1) :
            return x
    return 0 # if binary_decimal is exhausted

def shuffle_gen(start, stop) :
    """ A generator that yields a random permutation
    of the numbers start, start + 1, ..., stop -1. """
    n = stop - start
    scratch = dict()
    for remaining in range(n, 0, -1):
        i = random.randrange(remaining)
        # recall that scratch.get(i,i) = scratch[i]
        # if it is defined and scratch.get(i,i) = i otherwise
        yield scratch.get(i,i) + start
        scratch[i] = scratch.get(remaining - 1, remaining - 1)
        # we don't need to keep track of this anymore
        # note : we use `.pop` instead of `del` because
        # scratch[remaining - 1] may not be set
        scratch.pop(remaining - 1, None)
