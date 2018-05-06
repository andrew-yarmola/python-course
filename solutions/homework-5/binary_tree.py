class Node:
    def __init__(self, data = None, left = None, right = None) :
        self._right = None
        self._left = None
        self._parent = None
        self.data = data
        self.left = left
        self.right = right

    @property
    def data(self) :
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    # publically, parent will be readonly!
    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, set_as_left) :
        if type(set_as_left) is Node or set_as_left is None :
            # we must clean up the parent of the old node 
            if self.left is not None :
                self.left._parent = None
            self._left = set_as_left
            # set outselves as the parent of the new node
            if self.left is not None :
                self.left._parent = self
        else :
            raise ValueError("Left child must be a Node or None")

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, set_as_right) :
        if type(set_as_right) is Node or set_as_right is None :
            # we must clean up the parent of the old node 
            if self.right is not None :
                self.right._parent = None
            self._right = set_as_right
            # set outselves as the parent of the new node
            if self.right is not None :
                self.right._parent = self
        else :
            raise ValueError("Right child must be a Node or None")

    def inorder(self):
        L = []
        C = [self.data]
        R = []
        if self.left is not None:
            L = self.left.inorder()
        if self.right is not None:
            R = self.right.inorder()
        return L + C + R

def test_tree() :
    # here 'up' means go to a parent, and 'nl' mean "no left" for skipping the left
    # node. we keep a current node an keep setting left nodes until we have to go up
    # and can't set a left anymore
    tree_encoding = [8,3,1,'up', 6, 4, 'up', 7, 'up', 'up', 'up', 10, 'nl', 14, 13]

    # using the fact that data is the first argument
    root = Node(tree_encoding[0])
    curr = root
    skip_left = False
    for d in tree_encoding[1:] :
        if d == 'up' :
            curr = curr.parent
            continue
        if d == 'nl' :
            skip_left = True
            continue
        new = Node(d)
        if curr.left is None and not skip_left :
            curr.left = new
        else :
            curr.right = new
        curr = new
        skip_left = False

    return root
