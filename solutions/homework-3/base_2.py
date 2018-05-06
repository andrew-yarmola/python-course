def bits_needed(n) :
    """ Returns the number of bits needed to represent the
    integer n in binary including sign. 0 has no sign. """
    if n == 0 : 
        return 0
    return len('{0:+b}'.format(n))

def is_power_of_2(n) :
    """ Returns True if n is an integral power of 2. """
    if n < 1 : # Negative numbers are out
        return False
    # We use the signed formatting binary string
    binary = '{0:+b}'.format(n)
    # binary starts with +1, if there is a 1
    # afterwards, then we are not a power
    if '1' in binary[2:] :
        return False
    else :
        return True

def bad_log_base_2(n) :
    """ Returns -1 if n is not an integral power of 2.
    Returns log_2(b) otherwise. """
    if not is_power_of_2(n) :
        return -1
    else :
        return bits_needed(n) - 2

def float_repr(x) :
    """ Given a float x, returns a pair of ints (c,q)
    such that x = c*2**q exactly. """ 
    # if a function returns a tuple, you can read off
    # the multiple inputs using this syntax
    m, n = x.as_integer_ratio()
    # since n is a power of 2
    q_minus =  bad_log_base_2(n)
    if q_minus < 0 :
        raise RuntimeError("Unexpected denominator in "
                            "float.as_integer_ratio().")
    return (m,-q_minus)

def float_repr_54(x) :
    """ Given a float x, returns a pair of ints (c,q)
    such that x = c*2**q exactly and c has 54 or less
    bits of percision, including sign.  """ 
    c, q = float_repr(x)
    c_bits = bits_needed(c)
    while c_bits > 54 :
        if c % 2 != 0 :
            raise RuntimeError("Numerator not a multiple of 2.")
        c //= 2 # Use integer division!
        q += 1
        c_bits -= 1
    return (c,q)
