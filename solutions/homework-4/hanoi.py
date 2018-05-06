import copy

def num_steps(n) :
    assert n > 0 and type(n) is int
    if n == 1 :
        return 1
    else :
        return 2 * num_steps(n-1) + 1

def append_to_peg(state, peg, value) :
    """ Appends value to the end of the list state[peg].
    Does NOT check if value > max(state[peg])! """
    state[peg].append(value)
    # we don't return anything because we modified state

def switch_pegs(state, some_peg, other_peg) :
    """ Switches values of some_peg and other_peg in state. """
    switched = { some_peg : state[other_peg],
                other_peg : state[some_peg] }
    state.update(switched)
    # we don't return anything because we modified state

def solution_states(n) :
    """ Prints a list of solution states (which are dictionaries)
        to solve the Tower of Hanoi problem with n disks """
    assert n > 0 and type(n) is int
    if n == 1 :
        sol_steps = [ { 'a' : [1], 'b' : [ ], 'c' : [ ] } ,
                      { 'a' : [ ], 'b' : [ ], 'c' : [1] } ]
        return sol_steps
    else :
        # we will use the solution from n - 1 to first
        # move the top n - 1 to peg 'b', then move disk n
        # to peg 'c', and finally reuse the n - 1 solution
        # to move everything to peg 'c' 
        start = solution_states(n-1)
        # we make a deep copy so that when we modify start's
        # elements, we don't change what's in finish ! 
        finish = copy.deepcopy(start)

        for i in range(len(start)) :
            # we add disk n to the 'a' peg and switch 'b', 'c' pegs
            # so that we are moving disks from 'a' to 'b'
            switch_pegs(start[i], 'b', 'c')
            append_to_peg(start[i], 'a', n)
            # we must move disk n to peg 'c' and then use the n - 1
            # solution to move everything from peg 'b' to 'c'.
            # we accomplish this just making finish move disks from 'b'
            # to 'c' and making sure to add disk n onto peg 'c'
            switch_pegs(finish[i], 'a', 'b')
            append_to_peg(finish[i], 'c', n)

        return start  + finish
