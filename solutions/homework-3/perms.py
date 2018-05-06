def is_perm(p) :
    """ Returns True is the tuple p represents a
    permutation function p[i] of {0,..., len(p)}. """   
    if type(p) is not tuple : return False
    # the sorted p should just be the range
    return sorted(p) == list(range(len(p)))

def compose(a,b) :
    """ Returns the composition of a followed by b, where
    a,b are tupels representing permutation functions. If
    the input is bad, raises an exception. """
    if (not is_perm(a)
     or not is_perm(b)
     or len(a) != len(b)) :
        raise SyntaxError("Input was not composable permutations.")
    result = [ b[a[i]] for i in range(len(a)) ]
    return tuple(result)

def valid_disjoint_cycle_rep(cycles) :
    """ Returns True if the input is a tuple of tuples representing
    a disjoint cycle decomposition of a permutation. """
    if type(cycles) is not tuple or len(cycles) == 0 : return False
    # we pull all the values out of cycles and then see if
    # they have no repeats and are in the right range
    values = []
    for c in cycles :
        if type(c) is not tuple : return False
        for x in c : 
            if type(x) is not int : return False
            values.append(x)
    values = sorted(values)
    expected_range = range(max(values))
    for i in range(len(values)-1):
        if values[i] not in expected_range or \
           values[i] == values[ i + 1 ] :
            return False
    return True

def max_or_minusone(t) :
    """ Tries to returns max(t) ,
    or -1 if max(t) fails. """
    # if you want, you could also just check len(t) > 0
    try :
        return max(t)
    except :
        return -1

def min_perm_size(cycles) :
    """ Returns the minimum permutation size given a tuple
    of tuples representing a disjoint cycle decomposition. Raises a
    SyntaxError on bad input. """
    if not valid_disjoint_cycle_rep(cycles) :
        raise SyntaxError("Bad disjoint cycle representation")
    else :
        return max(map(max_or_minusone, cycles)) + 1

# A more efficient version of valid_disjoint_cycle_rep using sets
def valid_disjoint_cycle_rep_v2(cycles) :
    """ Returns True if the input is a tuple of tuples representing
    a disjoint cycle decomposition of a permutation. """
    if type(cycles) is not tuple or len(cycles) == 0 : return False
    # keep track of seen integers
    seen = set()
    for c in cycles :
        if type(c) is not tuple : return False
        for i in c :
            if type(i) is not int or i < 0 :
                return False
            elif i in seen :
                return False
            else :
                seen.add(i)
    return True

def func_from_disjoint_cycle_rep(cycles) :
    """ Returns the function representation of a permutation
    given a tuple of tuples representing a disjoint cycle
    decomposition. Raises a SyntaxError on bad input. """
    # this will validate input, so I don't have to here
    perm_size = min_perm_size(cycles)
    # start with idenity and modify
    f = list(range(perm_size))
    for cycle in cycles :
        cycle_len = len(cycle)
        for i in range(cycle_len) :
            f[cycle[i]] = cycle[ (i+1) % cycle_len ]
    return tuple(f)

def cycle_rep_from_func(f) :
    """ Returns the disjoint cycle representation of a permutation
    given a tuple as a function reprepresentation.
    Raises a SyntaxError on bad input. """
    if not is_perm(f) :
        raise SyntaxError("Bad function representation")
    # we will use a cycle_start and seen to keep track of the cycles
    cycle_rep = []
    n = len(f)
    seen = [0]*n
    while 0 in seen :
        # find the first non-visited int
        c_start = seen.index(0)
        cycle = [c_start]
        seen[c_start] = 1
        c_next = f[c_start]
        while c_next != c_start :
            cycle.append(c_next)
            seen[c_next] = 1
            c_next = f[c_next]
        if len(cycle) > 1 :
            cycle_rep.append(tuple(cycle))
    if len(cycle_rep) > 0 :
        return tuple(cycle_rep)
    else :
        return ((),)
    
# Again, sets make things a little shorter, cleaner and easier to read
def cycle_rep_erom_func_v2(f) :
    """ Returns the disjoint cycle representation of a permutation
    given a tuple as a function reprepresentation.
    Raises a SyntaxError on bad input. """
    if not is_perm(f) :
        raise SyntaxError("Bad function representation")
    # we will use a cycle_start and seen to keep track of the cycles
    cycle_rep = []
    n = len(f)
    unseen = set(range(n))
    while len(unseen) > 0 :
        c_start = unseen.pop()
        cycle = [c_start]
        c_next = f[c_start]
        while c_next != c_start :
            cycle.append(c_next)
            unseen.discard(c_next)
            c_next = f[c_next]
        if len(cycle) > 1 :
            cycle_rep.append(tuple(cycle))
    if len(cycle_rep) > 0 :
        return tuple(cycle_rep)
    else :
        return ((),)

def get_first(x) :
    """ Returns the fist element of x. Assumes x is not empty. """
    return x[0]

def get_second(x) :
    """ Returns the second element of x. Assumes x as at
        least 2 elements. """
    return x[1]

def rot_to_min(x) :
    """ Given a list or tuple x, returns its cyclical rotation
        starting with the minumum value. Return type is the same as x. """
    # enumerate(x) returns an iterable of paits (idx, val)
    min_idx, x_min = min(enumerate(x), key = get_second)
    # return the rotated version
    return x[min_idx:] + x[:min_idx]

def canonical_disjoint_rep(cycles) :
    """ Returns the canonical cycle decomposition given a tuple
        of tuples representing a disjoint cycle decomposition. All
        empty tuples and singletons are removed. Raises a
        SyntaxError on bad input. """
    if not valid_disjoint_cycle_rep(cycles) :
        raise SyntaxError("Bad disjoint cycle representation")
    # the identity is already canonical
    if cycles == ((),) : return cycles
    # delete any empty or singleton tuples in p
    clean_cycles = [ c for c in cycles if len(c) > 1 ]
    # now we can cyclically rotate each tuple in p
    inner_sorted = map(rot_to_min, clean_cycles)
    # sorting the lists in the inner_sorted iterator
    outer_sorted = sorted(inner_sorted, key = get_first)
    return tuple(outer_sorted)
