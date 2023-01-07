import dotenv
import os
from collections import deque
lp_proj = dotenv.get_key(os.getenv('adventofcode2022'), 'root_local')
fname = lp_proj + "\\" + 'dec7thinput.txt'

# File system, don't ask me why I did it this way, exercise with creating and traversing a node structure
class TreeMake:
    class Node:
        __slots__ = '_parent', '_element', '_first_child', '_right_sibling', 'num_children', 'dir_size',

        def __init__(self, element, parent=None, right_sibling=None, first_child=None):
            self._parent = parent
            self._element = element
            self._first_child = first_child
            self._right_sibling = right_sibling
            self.num_children = 0
            self.dir_size = 0

    # Position theoretically used for O(1) additions/deletions/replacements - not implemented here
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def _element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return self == other

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('Not a valid posiition')
        if p._container is not self:
            raise ValueError('Does not belong to this contaienr')
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    def is_empty(self, p):
        return p._element == None
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    # Positioners
    def _atfirst_child(self, p):
        # Return position of first_child of node at position p, else raise ValueError
        node = self._validate(p)
        if node._first_child is None:
            raise ValueError('node at position has no child')
        return self._make_position(node._first_child)

    # Accessors
    def _rootbegin(self, e):
        self._root = self.Node(e)
        return self._make_position(self._root)

    def _add_first_child(self, p, e):
        # Add first child, return position
        node = self._validate(p)
        if node._first_child is not None:
            raise ValueError("First child already exists")
        node._first_child = self.Node(e, parent=node)
        node.num_children += 1
        return self._make_position(node._first_child)

    def _add_right_sibling(self, p, e):
        # Add sibling to right of given sibling, if no first sibling, create
        node = self._validate(p)
        while node._right_sibling is not None:
            node = node._right_sibling
        new_node = self.Node(e, parent=node._parent)
        node._right_sibling = new_node
        node._parent.num_children += 1
        return self._make_position(new_node)

    # Traversal
    def _breadth_search(self, p, v):
        # Searches linked list below position for v
        res = []
        node = self._validate(p)
        step = node._first_child
        res.append((step._element, step))
        while step._right_sibling is not None:
            res.append((step._right_sibling._element, step._right_sibling))
            step = step._right_sibling

        for val, node in res:
            if val == v:
                return self._make_position(node)

        return "Not Found"

    def _step_up(self, p):
        # Steps up one level via position._parent
        node = self._validate(p)
        if node._parent is self._root:
            return self._make_position(self._root)
        return self._make_position(node._parent)

    # Public
    def treemake(self, fname):
        # Given input text at file name, instantiates the file system
        with open(fname, 'r') as fp:
            line1 = fp.readline()
            self._rootbegin(line1[5:-1])
            fp.seek(0)
            for line in fp.readlines():
                node, addval = None, None
                if line[:1] == '$':
                    if 'cd' in line:
                        if line[5:-1] == '/':
                            curr_p = self._make_position(self._root)
                            continue
                        if '..' in line:
                            old_p = curr_p
                            curr_p = self._step_up(old_p)
                            continue
                        elif curr_p:
                            old_p = curr_p
                            currval = line[5:-1]
                            curr_p = self._breadth_search(old_p, currval)
                            continue
                    if 'ls' in line:
                        continue
                if 'dir' in line:
                    node = self._validate(curr_p)
                    addval = line[4:-1]
                    if node.num_children == 0:
                        self._add_first_child(curr_p, addval)
                        continue
                    add_posdir = self._atfirst_child(curr_p)
                    self._add_right_sibling(add_posdir, addval)
                    continue
                elif 'cd' and 'dir' not in line:
                    node_file = self._validate(curr_p)
                    addval = line.split(' ')
                    f_size = int(addval[0])
                    node_file.dir_size += f_size
                    node_loop = node_file
                    while node_loop._parent is not None:
                        node_loop._parent.dir_size += f_size
                        node_loop = node_loop._parent
                    if node_file.num_children == 0:
                        self._add_first_child(curr_p, addval)
                    else:
                        add_posfile = self._atfirst_child(curr_p)
                        self._add_right_sibling(add_posfile, addval)

    def system_search_acc(self, limit: int = 100000) -> list:
        # Searches file system, returns list of directories at or below limit argument
        if not self._root:
            raise ValueError("Not a Tree")
        if not self._root._first_child:
            raise ValueError("Empty Tree")

        node = self._root._first_child
        dir_list = []
        de = deque()
        de.append(node)

        while node._right_sibling is not None:
            de.append(node._right_sibling)
            node = node._right_sibling

        while len(de) > 0:
            node_de = de.popleft()
            if limit >= node_de.dir_size > 0:
                dir_list.append((node_de, node_de._element, node_de.dir_size))
            if not node_de._first_child:
                continue
            node_de = node_de._first_child
            de.append(node_de)
            while node_de._right_sibling is not None:
                de.append(node_de._right_sibling)
                node_de = node_de._right_sibling

        return dir_list

    def dir_list(self):
        # Same as system_search_acc except no limit and adds self._root to returned list
        if not self._root:
            raise ValueError("Not a Tree")
        if not self._root._first_child:
            raise ValueError("Empty Tree")
        node = self._root._first_child
        dir_list = []
        de = deque()

        de.append(node)
        while node._right_sibling is not None:
            de.append(node._right_sibling)
            node = node._right_sibling

        dir_list.append((self._root._element, self._root.dir_size))
        while len(de) > 0:
            node_de = de.popleft()
            if isinstance(node_de._element, list):
                continue
            if node_de.num_children > 0:
                dir_list.append((node_de._element, node_de.dir_size))
            node_de = node_de._first_child
            de.append(node_de)
            while node_de._right_sibling is not None:
                de.append(node_de._right_sibling)
                node_de = node_de._right_sibling

        return dir_list

if __name__ == "__main__":
    T = TreeMake()
    T.treemake(fname)
    dir_list_ans1 = T.system_search_acc(999999999999999)
    res1 = 0

    for node, name, val in dir_list_ans1:
        print(node, name, val)
        res1 += val

    print(f'RES1: {res1}') # Part 1 Answer


    tot_size = T._root.dir_size
    minv = abs(70000000 - tot_size - 30000000)
    sl = []
    dl = T.dir_list()
    for dir, size in dl:
        if size >= minv:
            sl.append(size)

    res2 = sorted(sl)[0]
    print(f'RES2: {res2}')















