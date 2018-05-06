def bits_needed(n) :
    if n == 0 : 
        return 0
    return len('{0:+b}'.format(n))

def is_power_of_2(n) :
    if n < 1 :
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
    if not is_power_of_2(n) :
        return -1
    else :
        return bits_needed(n) - 2
