import dotenv
import os

dv = dotenv.DotEnv(os.getenv('localAdvent2022'))
lp_proj = dv.get("root_local")
fname = lp_proj + "\\" + 'dec7thinput.txt'

class TreeMake:
    class Node:
        __slots__ = '_parent', '_element', '_children', '_siblings', 'num_children'

        def __init__(self, parent, element, sibling, child):
            self._parent = parent
            self._element = element
            self._children = child
            self._siblings = sibling
            self.num_children = 0

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def _element(self):
            return self._node._element

        def __eq__(self, other):
            return True if type(self) is type(other) and self._node is other._node else False

        def __ne__(self, other):
            return self == other

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('Not a valid posiition')
        if p._container is not self:
            raise ValueError('Does not belong to this contaienr')
        if p._node._children is None:
            raise ValueError('Position is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node)

    def __init__(self):
        self._root = None
        self._size = 0

    def _is_empty(self):
        return self._size == 0

    def _rootf(self):
        self._root = self.Node(None, None, None)
        self._size += 1
        return self._make_position(self._root)

    def is_root(self):
        return self._root is not None

    def at_root(self):
        if not self.is_root():
            raise Exception('No Root')
        return self._make_position(self._root)

    def get_element(self, p):
        return p._element
    def add_child(self, parent: Node, e):
        parent._children = self.Node(parent, e, None, None)
        parent.num_children += 1
        self._size += 1
        return self._make_position(parent._children)

    def add_sibling(self, sibling: Node, e):
        sibling._siblings = self.Node(sibling._parent, e, None, None)
        self._size += 1
        return self._make_position(sibling._siblings)

    def first_sibling(self, p):
        node = self._validate(p)
        return self._make_position(node._parent._children)

    def has_children(self, p):
        node = self._validate(p)
        return node.num_children != 0

    def after(self, p):
        if self.is_leaf(p):
            return None
        node = self._validate(p)
        return self._make_position(node._siblings)

    def down(self, p):
        if self.is_leaf(p):
            return None
        node = self._validate(p)
        return self._make_position(node._children)

    def traverse(self, p, e):
        if self.get_element(p) is e:
            return p
        else:
            if self.is_leaf(p):
                return None
            while self.




    def change_directory(self, e):
        if not self.is_root():
            raise Exception('No Root')
        walk = self.at_root()





    def is_leaf(self, p):
        node = self._validate(p)
        return node.num_children == 0

    def build(self, fname):
        commands = {
            '$ cd /': lambda: self._rootf()
            '$ ls ':
        }
        with open(fname, 'r') as fp:
            i = fp.read()
            i_shed = []






