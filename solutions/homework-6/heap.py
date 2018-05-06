def is_real_num(x) :
    """ Returns True if x is an int, bool, or float. """
    return isinstance(x, (int, float, bool))

class Heap :
    def __init__(self) :
        self._data_list = []

    @property
    def size(self) :
        return len(self._data_list)

    def _bubble_up(self, c_idx) :
        # since this is a private method, we assume
        # c_idx is a valid and non-negative index
        # we have c_idx == 2*p_idx + 1 or c_idx ==  2*p_idx + 2
        data = self._data_list
        while True :
            if c_idx == 0 : break
            p_idx = (c_idx + 1)//2 - 1
            parent, child = data[p_idx], data[c_idx]
            if parent < child :
                data[p_idx], data[c_idx] = child, parent
                c_idx = p_idx
            else :
                break 

    def _bubble_down(self, p_idx) :
        data = self._data_list
        while True :
            # since this is a private method, we assume
            # p_idx is a valid and non-negative index
            l_idx, r_idx = 2*p_idx + 1, 2*p_idx + 2
            parent = data[p_idx]
            if l_idx < len(data) :
                left = data[l_idx] 
            else : # if no left child, there is none at all
                break
            if r_idx < len(data) :
                right = data[r_idx]
            else : # only a left child, which is also terminal
                if left > parent :
                    data[p_idx], data[l_idx] = left, parent 
                break # left can't have any children
            if left <= parent and right <= parent :
                break # parent dominates
            if left > right :
                data[p_idx], data[l_idx] = left, parent
                p_idx = l_idx
            else : 
                data[p_idx], data[r_idx] = right, parent
                p_idx = r_idx

    def insert(self, value) :
        assert is_real_num(value)
        new_idx = len(self._data_list)
        self._data_list.append(value)
        self._bubble_up(new_idx) 

    def pop_max(self) :
        data = self._data_list
        if self.size > 1 :
            top = data[0]
            data[0] = data.pop()
            self._bubble_down(0)
            return top
        elif self.size == 1 :
            return data.pop() 
        else :
            raise IndexError("pop from empty Heap")

def new_path_with_suffix(path, suffix) :
    split = path.split('.')
    split[len(split) - 2] = split[len(split) - 2] + suffix
    return '.'.join(split)

def sort_all_lines(path) :
    assert isinstance(path, str) and len(path) > 0
    # we create out new file name
    sorted_path = new_path_with_suffix(path, '_sorted')
    # note : fp stands for file pointer
    with open(path, 'r') as read_fp :
        with open(sorted_path, 'w') as write_fp :
            heap = Heap()
            line_count = 0 # only used for error message
            for line in read_fp :
                line_count += 1
                sorted_data = [] 
                try :
                    # note : eval will turn ints into ints
                    # and floats into floats
                    data = map(eval, line.split(','))
                    for v in data :
                        # we reuse the same heap
                        heap.insert(v)
                    while heap.size > 0 :
                        sorted_data.append(heap.pop_max())
                    sorted_data_strs = map(str, sorted_data)
                    write_fp.write(','.join(sorted_data_strs) + '\n')
                except :
                    write_fp.write("Error : line {} is not a ".format(line_count)
                                 + "valid comma separated list of real numbers.\n")
    # the with statements close everything for us
