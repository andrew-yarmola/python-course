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
