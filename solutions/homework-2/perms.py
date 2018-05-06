def is_perm(p) :
    if type(p) is not tuple :
        return False
    return sorted(p) == list(range(len(p)))

def compose(a,b) :
    if (not is_perm(a)
     or not is_perm(b)
     or len(a) != len(b)) :
        return ()
    result = [ b[a[i]] for i in range(len(a)) ]
    return tuple(result)
