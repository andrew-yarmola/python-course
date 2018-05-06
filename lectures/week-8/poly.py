def is_num(x) :
    """ Returns True if x is an int, float, or complex. """
    return isinstance(x, (int, float, complex))

def strip_tail_zeros(p) :
    """ Removes zeros from the end of a list p. Retunrs
        the number of zeros stripped. """
    count = 0
    while len(p) > 0 and p[-1] == 0. :
        p.pop()
        count += 1
    return count

def deg(p) :
    """ Retruns the degree of a polynomial p,
        prepresented as a sequence of floats. """
    return len(p) - 1

def scale(p, a, divide = False) :
    """ By default, multiplies every element of list p by a.
        If divide = True, then divides every element
        of p by a. p is assumed to be a list of floats. """
    for i,v in enumerate(p) :
        if divide :
            p[i] = v/a
        else :
            p[i] = a*v

def subtract_with_shift(p, q, shift) :
    """ Treating p, q as polynomials p(x), q(x)
        this method returns the polynomial 
        p(x) - q(x)*x^shift. """
    if type(shift) is not int or shift < 0 :
        raise ValueError("Shift must be a positive int")
    len_diff = len(q) + shift - len(p)
    if len_diff > 0 :
        p.extend( [0.0] * len_diff )  
    for i, v in enumerate(q) :
        p[i+shift] -= v

def remainder(p,q) :
    """ Treating the sequences of floats p,q as
        polynomials, we return the remainer of
        dividing p by q using floating-point
        arithmetic. """
    if False in map(is_num, q) or \
       False in map(is_num, p) :
        raise ValueError("Input is not polynomial")
    r = list(p)
    q_monic = list(q)
    # sttip starting zeros
    strip_tail_zeros(r) 
    strip_tail_zeros(q_monic)
    if len(q_monic) == 0 :
        raise RuntimeError("Division by zero polynomial")
    # make q_monic actually monic
    scale(q_monic, q_monic[-1], divide = True)
    while deg(r) >= deg(q_monic) :
        t = list(q_monic)
        scale(t, r[-1])
        subtract_with_shift(r, t, deg(r) - deg(t))
        if strip_tail_zeros(r) == 0 :
            raise RuntimeError("Floating point arithmetic failed")

    return tuple(r)

def gcd(p,q) :
    """ Recursive implementation of the gcd
        algorithm for polynomials p,q.
        Returns the monic gcd. """
    if deg(q) > deg(p) :
        p, q = q, p # this is a stanfrad way to swap things
    r = remainder(p,q)
    if len(r) == 0 :
        t = list(q)
        scale(t, t[-1], divide = True) 
        return tuple(t)
    else :
        return gcd(q,r) 

def gcd_v2(p,q) :
    """ Non-recursive implementation of the
        gcd algorithm for polynomials p,q.
        Returns the monic gcd. """
    if deg(q) > deg(p) :
        p, q = q, p # this is a stanfrad way to swap things
    prev = tuple(q) # a copy
    curr = remainder(p,q)
    if len(curr) > 0 :
        prev, curr = curr, remainder(prev, curr)

    t = list(prev)
    scale(t, t[-1], divide = True)
    return tuple(t)
