import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
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
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    # Positioners
    def _atroot(self, p):
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
        self._root = e
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
        return p._node._num_children == 0

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

    # Traversal generators
    def _breadth(self, p):
        #  Traverse accross siblings until None, yields _element
        node = self._validate(p)
        while node._right_sibling is not None:
            yield self._make_position(node)
            node = node._right_sibling
        yield self._make_position(node)

    def _d_then_b(self, p, v):
        # Travel breadth first
        if p._element == v:
            return p
        for x in self._breadth(p):
            if p._element == v:
                return p
            elif p._num_children > 0:
                self._d_then_b(p, v)
            else:
                continue

    def treemake(self, e):
        return self._rootbegin(e)





if __name__ == "__main__":
    T = TreeMake()
    NRoot = T.treemake("Root")
    NA1 = T._add_first_child(NRoot, "A1")
    NA2 = T._add_right_sibling(NA1, "A2")
    NA3 = T._add_right_sibling(NA2, "A3")
    NB1 = T._add_first_child(T._atfirst_child(), "B1")
    NB2 = T._add_right_sibling(NB1, "B2")
    NB3 = T._add_right_sibling(NB2, "B3")
    AB1 = T._add_right_sibling(T._at_parent(NB3), "AB1")














