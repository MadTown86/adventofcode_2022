import dotenv
import os
from collections import deque
lp_proj = dotenv.get_key(os.getenv('adventofcode2022'), 'root_local')
fname = lp_proj + "\\" + 'dec7thinput.txt'


class TreeMake:
    class Node:
        __slots__ = '_parent', '_element', '_first_child', '_right_sibling', 'num_children', 'num_siblings'

        def __init__(self, element, parent=None, right_sibling=None, first_child=None):
            self._parent = parent
            self._element = element
            self._first_child = first_child
            self._right_sibling = right_sibling
            self.num_children = 0
            self.num_siblings = 0

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
        # if p._node._parent is p._node:
        #     raise ValueError("p is no longer valid")
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
    def _atroot(self):
        # Return position at root of tree else raise ValueError
        if self._root is None:
            raise ValueError("No root created for this tree")
        return self._make_position(self._root)

    def _atfirst_child(self, p):
        # Return position of first_child of node at position p, else raise ValueError
        node = self._validate(p)
        if node._first_child is None:
            raise ValueError('node at position has no child')
        return self._make_position(node._first_child)

    def _at_last_sibling(self, p):
        node = self._validate(p)
        if node._right_sibling is None:
            return self._make_position(node)
        else:
            while node._right_sibling is not None:
                node = node._right_sibling
            return self._make_position(node)

    def _at_parent(self, p):
        # Return position of parent of node at position p else Raise ValueError
        node = self._validate(p)
        if node._parent is None and self._root is node:
            raise ValueError('node at position is root, no parent')
        return self._make_position(node._parent)

    # Counters
    def _num_children(self, p):
        # Returns num_children attribute of node at p
        node = self._validate(p)
        return node.num_children

    def _num_siblings(self, p):
        # Returns number of siblings stored at first sibling only
        node = self._validate(p)
        if node._parent._first_child is None:
            return 0
        return node._parent._first_child.num_siblings

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
        node._first_child.num_siblings += 1
        node.num_children += 1
        return self._make_position(node._first_child)

    def _add_right_sibling(self, p, e):
        # Add sibling to right of given sibling, if no first sibling, create
        node = self._validate(p)
        if node._right_sibling is not None:
            while node._right_sibling is not None:
                node = node._right_sibling
            node._right_sibling = self.Node(e, parent=node._parent)
            node._parent.num_children += 1
            node._parent._first_child.num_siblings += 1
            return self._make_position(node._right_sibling)
        node._right_sibling = self.Node(e, parent=node._parent)
        node._parent.num_children += 1
        node._parent._first_child.num_siblings += 1
        return self._make_position(node._right_sibling)

    def _replace_value(self, p, e):
        # Replace value at p, return old value
        if not isinstance(p, self.Position):
            raise TypeError("p is not a valid position")
        if p._element is None:
            raise ValueError('p holds no value')
        old = p._element
        p._element = e
        return old

    def _delete(self, p):
        # Delete node at p, return value
        node = self._validate(p)
        if node._parent._first_child is node:
            if node._right_sibling is None:
                node._parent._first_child = None
                return node._value

    def _is_leaf(self, p):
        return p._node.num_children == 0

    def _attach(self, p, t1):
        node = self._validate(p)
        if self._num_children(p) > 0:
            raise TypeError("position must be leaf")
        if not type(self) is type(t1): raise TypeError("Trees must match")
        if not t1.is_empty():
            t1._root = node
            t1._root._first_child._parent = node
            self._size += t1._size
            t1._size = 0

    # Traversal
    def _breadth_yield(self, p):
        #  Traverse accross siblings until None, yields _element
        node = self._validate(p)
        while node._right_sibling is not None:
            yield self._make_position(node)
            node = node._right_sibling
        yield self._make_position(node)

    def _breadth_bin(self, p):
        res = []
        node = self._validate(p)
        while node._right_sibling is not None:
            res.append(node)
            node = node._right_sibling
        res.append(self._make_position(node))
        return res

    def _file_search(self, v):
        q = deque()
        start = self._atroot()
        r_node = self._validate(start)
        if r_node._element == v:
            return start
        if not self._num_children(start) > 0:
            raise ValueError("Empty Tree")
        node = self._validate(start)

        def diver(node, v):
            print(f'DIVER STEP: {node._element}')
            if node._element == v:
                return self._make_position(node)
            while node._first_child is not None:
                print(f'WHILE DIVER STEP: {node._element}')
                if node._element == v:
                    return self._make_position(node)
                if node.num_siblings == 0:
                    node = node._first_child
                    continue
                q.append(node._right_sibling)
                node = node._first_child
            if node._element == v:
                return self._make_position(node)
            if node._right_sibling:
                q.append(node._right_sibling)


        diver(node, v)

        # Finish loop through deck to clear it of everything that doesn't either populate it with more values
        # Is the value looking for
        # Or the deque is empty
        while len(q) > 0:
            node = q.popleft()
            if node == None:
                raise ValueError("Value Not Found") and StopIteration("End Of Tree")
            print(f'QUEUE STEP: {node._element}')
            p = self._make_position(node)
            if node._element == v:
                return self._make_position(node)
            if self._is_leaf(p):
                if self._num_siblings(p) is not None:
                    q.append(node._right_sibling)
            else:
                diver(node, v)

    def first_child(self, p):
        node = self._validate(p)
        if node._first_child:
            return node._first_child._element
        else:
            raise ValueError("No Children")

    def treemake(self, fname):
        with open(fname, 'r') as fp:
            line1 = fp.readline()
            root = self._rootbegin(line1[5:])
            fp.seek(0)
            for line in fp.readlines():
                print(line)
                if line[:1] == '$':
                    if 'cd' in line[:1]:
                        curr_p = self._file_search(line[5:])
                    if 'ls' in line[:1]:
                        continue
                if 'dir' in line:

                    check_bin = self._breadth_bin(curr_p)
                    if line[5:-1] in check_bin:
                        continue
                    else:
                        node = self._validate(curr_p)
                        if node.num_children == 0:
                            self._add_first_child(curr_p, line[5:-1])
                        add_pos = self._at_last_sibling(self._atfirst_child(curr_p))
                        self._add_right_sibling(add_pos, line[5:-1])


if __name__ == "__main__":
    T = TreeMake()
    T.treemake(fname)


    NRoot = T._rootbegin("Root")
    NA1 = T._add_first_child(p=NRoot, e="A1")
    NA2 = T._add_right_sibling(NA1, "A2")
    NA3 = T._add_right_sibling(NA2, "A3")
    NB1 = T._add_first_child(T._atfirst_child(NRoot), "B1")
    NB2 = T._add_right_sibling(NB1, "B2")
    NB3 = T._add_right_sibling(NB2, "B3")
    AB1 = T._add_right_sibling(T._at_parent(NB3), "AB1")

    # for x in T._breadth(NA1):
    #     print(x._element())

    # P = T.first_child(NA1)
    # # print(P)
    # # print(NA1._element())
    # try:
    #     p = T._file_search("AB")
    #     print(p._element())
    # except ValueError as er:
    #     print(er)















