import random

def rearrange(cond_conv_seq,beta) :
    """ Given a generator cond_conv_seq that yield
    a sequence of conditionally convergent numbers,
    this generator yields a rearearrangement such
    that the rearrangement converges to beta. """
    pos = []
    neg = []
    seq = cond_conv_seq()
    total = 0.
    for a in seq :
        if a > 0. :
            pos.append(a)
        else :
            neg.append(a)
        if total < beta :
            if len(pos) > 0 :
                b = pos.pop(0)
            else :
                continue
        else :
            if len(neg) > 0 :
                b = neg.pop(0)
            else :
                continue
        yield b
        total += b

# a maximum for the abs of the 
# random beta to be chosen in the
# test below
beta_abs_max = 5.
max_seq_steps = 10**10

def test_rearrange(cond_conv_seq, error) :
    """ Return True if in some reasonable finite number of
    steps, a rearearrangement of cond_conv_seq begins to
    converge to a randomly chosen float from the interval
    (- beta_abs_max, beta_abs_max). """
    # we don't declare beta_abs_max and max_seq_steps
    # as globals, becase we don't plan to modiy them
    # and if someone updates this code, they can make
    # local versions named the same thing
    beta = random.uniform(-beta_abs_max, beta_abs_max)
    beta_seq = rearrange(cond_conv_seq,beta)
    total = 0.
    count = 0
    print(beta)
    while abs(beta - total) > error :
        if count > max_seq_steps :
            return False
        total += next(beta_seq)
        count += 1
    return True

def alt_harmonic_seq() :
    """ Generates (-1)^(n+1)/n. """
    n = 1.
    sign = 0
    while True :
        yield (-1)**sign/n
        n += 1.
        sign = 1 - sign

