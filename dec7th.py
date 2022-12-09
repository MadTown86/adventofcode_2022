import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec7thinput.txt'

class TreeMake:
    class Node:
        __slots__ = '_parent', '_element', '_children', '_sibling', 'num_children'

        def __init__(self, parent, element, sibling, child):
            self._parent = parent
            self._element = element
            self._children = child
            self._sibling = sibling
            self.num_children = 0

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def _element(self):
            return self._node._element

        def _sibling(self):
            return self._node._sibling is True

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            return self == other

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('Not a valid posiition')
        if p._container is not self:
            raise ValueError('Does not belong to this contaienr')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    def __init__(self):
        self._root = None
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def _p_next(self, p):
        if not p._element:
            raise StopIteration
        else:
            node = self._validate(p)
            return node._sibling

    def _rootf(self, e):
        self._root = self.Node(None, e, None, None)
        self._size += 1
        return self._make_position(self._root)

    def is_root(self):
        return self._root is not None

    def at_root(self):
        if not self.is_root():
            raise Exception('No Root')
        return self._make_position(self._root)

    def get_element(self, p):
        org = self._validate(p)
        return org._element
    def add_child(self, e, p: Position):
        original = self._validate(p)
        newnode = self.Node(original, e, None, None)
        original.num_children += 1
        original._children = newnode
        return self._make_position(newnode)

    def add_sibling(self, p, e):
        original = self._validate(p)
        newest = self.Node(original._parent, e, None, None)
        original._sibling = newest
        return self._make_position(newest)

    def first_sibling(self, p):
        node = self._validate(p)
        return self._make_position(node._parent._children)

    def has_children(self, p):
        node = self._validate(p)
        return node.num_children != 0

    def _after(self, p):
        node = self._validate(p)
        if node._sibling is None:
            return None
        return self._make_position(node._sibling)

    def down(self, p):
        if self.is_leaf(p):
            return None
        node = self._validate(p)
        return self._make_position(node._children)

    def breadthprint(self, p):
        ret = []
        while True:
            if self._p_next(p):
                ret.append(self.get_element(p))
                p = self._after(p)
            else:
                ret.append(self.get_element(p))
                break
        return ret

    def traverse(self, p, e):
        if self.get_element(p) is e:
            return p
        else:
            if self.is_leaf(p):
                return None
            while self._after(p) is not None:
                p = self._after(p)
                self.traverse(p, e)
            p = self.first_sibling(p)
            while self._after(p) is not None:
                p = self.down(p)
                self.traverse(p, e)

    def change_directory(self, e):
        if not self.is_root():
            raise Exception('No Root')
        walk = self.at_root()

    def is_leaf(self, p):
        node = self._validate(p)
        return node.num_children == 0

    def build(self, fname):
        commands = {
            '$ cd /': lambda: self._rootf(),
            '$ ls ': None
        }
        with open(fname, 'r') as fp:
            i = fp.read()
            i_shed = []


if __name__ == "__main__":
    T = TreeMake()
    N1 = T.rootf()
    N2 = T.add_child("BB1", N1)
    N3 = T.add_sibling(N2, "BB2")
    N4 = T.add_sibling(N3, "BB3")
    N5 = T.add_sibling(N4, "BB4")
    # N6 = T.first_sibling(N4)
    # N6 = T.add_child("FORALL", N5)
    p = N2
    print(T.breadthprint(p))














