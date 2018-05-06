import random
import string

def partition_gen(n) :
    """ Generates the partitions of a positive
    integer n in reverse lexographic order. """
    assert isinstance(n, int) and n > 0
    part = [n]
    yield tuple(part)
    # last non-unit index
    nu_idx = 0
    while part[0] != 1 :
        # if the previous partition ends with
        # ..., v, 1,1,1,..,1) we replace this tail
        # with ..., v-1, v-1, v-1,..., v-1, r) where
        # r < v-1 and the totals are preserved.
        val = part[nu_idx] - 1
        if val == 1 :
            part[nu_idx] -= 1
            part.append(1)
            nu_idx -= 1
        else :    
            total = val + len(part) - nu_idx
            reps, rest = divmod(total, val)
            part[nu_idx:] = reps*[val]
            if rest > 0 :
                part.append(rest)
            nu_idx = len(part) - 1 - (rest == 1)
        yield tuple(part)

def partitions(n) :
    """ Returns the list of partitions of a positive
    integer n in reverse lexographic order. """
    return [ p for p in partition_gen(n) ]

def random_from_reservoir(item_iter) :
    """ Produces a random item from an non-empty iterator
    item_iter without pior knowldege of the number of items.
    This is called reservoir sampling. """
    selected = None
    count = 0 
    for item in item_iter :
        if random.random() * count < 1 : 
            selected = item
        count += 1
    return selected

def generate_random_text(file_name) :
    """ Writes random words and lines to file_name.
    Attention : overwrites the file if it already exits. """
    num_lines = random.randint(20,100)
    with open(file_name, 'w') as fp :
        for _ in range(num_lines) :
            num_letters = random.randint(10,50)
            part_gen = partition_gen(num_letters)
            random_part = random_from_reservoir(part_gen)
            words = []
            for word_len in random_part :
                chars = [ random.choice(string.ascii_letters)
                          for _ in range(word_len) ]
                words.append(''.join(chars))
            fp.write(' '.join(words) + '\n')

def count_capitals(file_name) :
    """ Returns a dictionary mapping line numbers to
    number of uppercase letter per line in file_name. """
    upper_count = {}
    line_count = 0
    with open(file_name,'r') as fp :
        for line in fp :
            line_count += 1
            num_upper = sum(map(str.isupper, line))
            upper_count[line_count] = num_upper
    return upper_count
