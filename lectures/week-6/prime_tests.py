import random

def satisfies_fermat(n) :
    """ Returns True if the positive integer n
        satisfies the conclusion of Fermat's little
        theorem. False otherwise. """
    if type(n) is not int or n < 0 :
        raise ValueError("Input should be a positive integer.")
    # return for all even numbers
    if n == 2 : return True
    if n % 2 == 0 : return False
    # make a randomized list of tests
    tests = list(range(2,n))
    random.shuffle(tests)
    for x in tests :
        if pow(x, n-1, n) != 1 :
            return False
    return True

import math

def num_tests(n,prob) :
    """ Returns a number of tests needed to
        achieve probablity prob or more for
        n to be a Fermat pseudoprime. """
    if prob >= 1. :
        # since half of the numbers should be Fermat
        # witnesses, we return 1+(n-1)//2
        return 1+(n-1)//2
    else :
        # return k such that 1/2^k <= 1 - prob
        return -math.floor(math.log2(1-prob))

def probably_fermat_pseduoprime(n, prob) :
    """ Returns True if the positive integer n
        has probability `prob` (or more) of being
        a Fermat pseudoprime . """
    if type(n) is not int or n < 0 :
        raise ValueError("Input should be a positive integer.")
    # return for all even numbers
    if n == 2 : return True
    if n % 2 == 0 : return False
    k = num_tests(n, prob)
    tests = random.sample(range(1,n),k)
    for a in tests :
        if pow(a, n-1, n) != 1 :
            return False
    return True

def shuffle_gen(start, stop) :
    n = stop - start
    scratch = dict()
    for remaining in range(n, 0, -1):
        i = random.randrange(remaining)
        yield scratch.get(i,i) + start
        scratch[i] = scratch.get(remaining - 1, remaining - 1)
        # we don't need to keep track of this anymore
        # note : we use `.pop` instead of `del` because
        # scratch[remaining - 1] may not be set
        scratch.pop(remaining - 1, None)
    
def satisfies_fermat_fast(p) :
    if type(p) is not int or p < 0 :
        raise ValueError("Input should be a positive integer.")
    gen = shuffle_gen(2,p)
    for a in gen :
        if pow(a, p-1, p) != 1 :
            return False
    return True 

def mod_pow(a, power, n) :
    result = 1
    double = a
    while power > 0 :
        if power % 2 == 1 :
            result = (result * double) % n
            if result == 0 : break
        double = double**2 % n
        if double == 1 : break
        power //=2
    return result

# Miller-Rabin

def decompose_even_part(n) :
    """ Returns d,s such that n = d * (2**s). Assumes
    that n is a positive integer. """
    s, d = 0, n
    while d % 2 == 0 :
        s += 1
        d //= 2
    return (d,s)

def is_miller_rabin_witness(n,x) :
    """ Tests if x is a Miller-Rabin witness for n.
    Assumes x,n are integers and n > 0. """
    d, s = decompose_even_part(n-1)
    a = pow(x,d,n)
    # inconclusive if x**d % n == 1 
    if a == 1 : return False

    for _ in range(s) :
        # if we get -1 mon n, inconclusive
        if a == n - 1 :
            return False
        a = a**2 % n
        # if the square is 1 but before we were not -1, witness
        if a == 1 :
            return True

    # a is now x**(n-1) % n but it wasn't equal to 1 at the end
    # end of the last loop!
    return True

def probably_prime(n, prob) :
    """ Returns True if n is a prime with probablity greater
    than prob using the Miller-Rabin test. """
    assert isinstance(n, int) and n > 0
    if n == 2 : return True
    if n % 2 == 0 or n == 1 : return False
    # we compute the number of tests we need knowning that
    # x chosen from {1, ..., n-1} has probablity at least 3/4
    # of being an M-R witness
    if prob >= 1. :
        num_tests = 1+(3*(n-1))//4
    else :
        # want (1/4)**num_tests <= 1 - prob
        num_tests = -math.floor(math.log2(1-prob)/2)
    tests = random.sample(range(1,n), num_tests)
    for t in tests :
        if is_miller_rabin_witness(n, t) :
            return False
    return True 

def is_prime(n) :        
    """ Returns True if n is a prime. Assumes the extended Riemann hypothesis. """
    assert isinstance(n, int) and n > 0
    if n == 2 : return True
    if n % 2 == 0 or n == 1 : return False
    # TODO : math.log only works well with n < 2**53 !!!
    test_cutoff = math.floor(2 * math.log(n)**2)
    for t in range(2, test_cutoff  + 1) :
        if is_miller_rabin_witness(n, t) :
            return False
    return True 

