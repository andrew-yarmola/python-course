def collatz_max(n) :
    """ Returns a pair (a,s) where s in the maximum length
        of a Collatz sequence starting with 0 < x < n and a is
        a starting point of such a sequence. """
    # we use a dictionary to keep track of all of out known
    # Collatz sequence lengths
    known = {1 : 0}
    max_steps = 0
    max_start = 1
    # note that if x < n//2 then the collatz sequence of
    # 2*x is longer and 2*x < n
    for m in range(n//2, n) :
        # We can ignore any m = 4 mod 6 because then
        # (m-1)/3 is odd an less than m. So we will
        # consider some 2^k(m-1)/3 and that will have more steps 
        if m % 6 == 4 :
            continue
        m_steps = 0
        # we will save the seqeunce to save the steps later
        seq = []
        curr = m
        while True :
            # we see if we have already recorded steps for curr
            # note that dict.get(key) will return None if the key is
            # not in the dictionary
            curr_steps = known.get(curr)
            if curr_steps is not None :
                # we now know there are curr_steps more to go
                # so we don't need to waste our time computing
                m_steps += curr_steps
                # record all new steps counts for the sequence
                for idx,val in enumerate(seq) :
                    known[val] = m_steps - idx
                break
            seq.append(curr)
            if curr % 2 == 0 :
                curr = curr // 2
            else :
                curr = 3 * curr + 1
            m_steps += 1
        
        if m_steps > max_steps :
            max_steps = m_steps
            max_start = m

    return (max_start, max_steps)
