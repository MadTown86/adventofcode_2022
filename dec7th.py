import dotenv
import os
from collections import deque
lp_proj = dotenv.get_key(os.getenv('adventofcode2022'), 'root_local')
fname = lp_proj + "\\" + 'dec7thinput.txt'



"""
Note: I only checked the first few directory names to see if they repeated and made an assumption that they did not.

I was wrong, specifically vmtnnfv is repeated many times and so the basis of the tree-make is now bunk.  I will have
to actually incorporate the use of the '$ cd ..' call that I was trying to avoid.  

I know that I can accomplish this change, but believe it may not be worth it now for what this problem actually is.


Lots of useless code now ^^
"""
class TreeMake:
    class Node:
        __slots__ = '_parent', '_element', '_first_child', '_right_sibling', 'num_children', 'num_siblings', 'dir_size'

        def __init__(self, element, parent=None, right_sibling=None, first_child=None):
            self._parent = parent
            self._element = element
            self._first_child = first_child
            self._right_sibling = right_sibling
            self.num_children = 0
            self.num_siblings = 0
            self.dir_size = 0

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
        if isinstance(e, list):
            size_increase = int(e[0])
            while node._parent is not None:
                node._parent.dir_size += size_increase
                node = node._parent
        return self._make_position(node._first_child)

    def _add_right_sibling(self, p, e):
        # Add sibling to right of given sibling, if no first sibling, create
        node = self._validate(p)
        while node._right_sibling is not None:
            node = node._right_sibling
        new_node = self.Node(e, parent=node._parent)
        node._right_sibling = new_node
        node._parent.num_children += 1
        if isinstance(e, list):
            size_increase = int(e[0])
            while node._parent is not None:
                node._parent.dir_size += size_increase
                node = node._parent
        return self._make_position(new_node)

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
        if node._first_child is None:
            return []
        if node is self._root:
            node = self._root._first_child
            while node._right_sibling is not None:
                res.append(node)
                node = node._right_sibling
            res.append(node)
            return res
        pos = node._first_child
        while pos._right_sibling is not None:
            res.append(pos._element)
            pos = pos._right_sibling
        res.append(pos._element)
        return res

    def _breadth_search(self, p, v):
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

    def _file_search(self, v):
        res_bin = []
        q = deque()
        if not self._root:
            raise TypeError("Invalid Tree")
        if v == self._root._element:
            res_bin.append(self._make_position(self._root))
        if self._num_children(self._make_position(self._root)) == 0:
            raise ValueError("Empty Tree")
        q.append(self._root._first_child)
        pos = self._root._first_child
        while pos._right_sibling is not None:
            q.append(pos._right_sibling)
            pos = pos._right_sibling
        q.append(pos)

        while len(q) > 0:
            pos = q.popleft()
            if pos._element == v:
                res_bin.append(self._make_position(pos))
            if pos.num_children > 0:
                q.append(pos._first_child)
                pos = pos._first_child
                while pos._right_sibling is not None:
                    q.append(pos._right_sibling)
                    pos = pos._right_sibling
                q.append(pos)

        return res_bin

    def print_dir_contents(self, n):
        res = []
        if n.num_children > 0:
            curr = n._first_child
            res.append(curr._element)
            while curr._right_sibling is not None:
                res.append(curr._right_sibling._element)
                curr = curr._right_sibling

        return res

    def add_dir_sizes(self, n):
        res = 0
        if n.num_children > 0:
            curr = n._first_child
            res += curr.dir_size
            while curr._right_sibling is not None:
                res += curr._right_sibling.dir_size
                curr = curr._right_sibling

        return res

    def _step_up(self, p):
        node = self._validate(p)
        if node._parent is self._root:
            return self._make_position(self._root)
        return self._make_position(node._parent)

    def treemake(self, fname):
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
                    # check_bin = self._breadth_bin(curr_p)
                    # if line[5:-1] in check_bin:
                    #     continue
                    # else:
                    node = self._validate(curr_p)
                    addval = line[4:-1]
                    if node.num_children == 0:
                        self._add_first_child(curr_p, addval)
                        continue
                    add_posdir = self._atfirst_child(curr_p)
                    self._add_right_sibling(add_posdir, addval)
                    continue
                elif 'cd' and 'dir' not in line:
                    node = self._validate(curr_p)
                    addval = line.split(' ')
                    f_size = int(addval[0])
                    node.dir_size += f_size
                    if node.num_children == 0:
                        self._add_first_child(curr_p, addval)
                    else:
                        add_posfile = self._atfirst_child(curr_p)
                        self._add_right_sibling(add_posfile, addval)

    def treeprint(self):
        if not self._root:
            raise ValueError("Root Empty")
        if not self._root._first_child:
            raise ValueError("Tree Empty")
        q2 = deque()
        q2.append(self._root._first_child)
        node = self._root._first_child
        while node._right_sibling is not None:
            q2.append(node._right_sibling)
            node = node._right_sibling

        while len(q2) > 0:
            node = q2.popleft()
            print(node._element)
            if node._first_child is not None:
                q2.append(node._first_child)
                curr = node._first_child
                while curr._right_sibling is not None:
                    q2.append(curr._right_sibling)
                    curr = curr._right_sibling

    def treecalc(self):
        if not self._root:
            raise ValueError("Root Empty")
        if not self._root._first_child:
            raise ValueError("Tree Empty")
        res = []
        parsed = set()
        q_all = deque()
        q_files = deque()
        q_all.append(self._root._first_child)
        node = self._root._first_child
        while node._right_sibling is not None:
            q_all.append(node._right_sibling)
            node = node._right_sibling

        while len(q_all) > 0:
            node_b = q_all.popleft()
            vh_element = type(node_b._element)
            if not isinstance(node_b._element, list):
                if node_b._first_child is not None:
                    q_all.append(node_b._first_child)
                    curr = node_b._first_child
                    while curr._right_sibling is not None:
                        q_all.append(curr._right_sibling)
                        curr = curr._right_sibling
            if isinstance(node_b._element, list):
                vh_int = int(node_b._element[0])
                vh_fn = node_b._element[1]
                if vh_fn in parsed:
                    continue
                parsed.add(vh_fn)
                if int(node_b._element[0]) >= 0:
                    p_list = []
                    org = node_b._element
                    while node_b is not self._root:
                        if node_b._parent._element != "/":
                            p_list.append(node_b._parent._element)
                        node_b = node_b._parent
                    q_files.append((org, p_list))

        return q_files

    def treecalc2(self):
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
            if 100000 >= node_de.dir_size > 0:
                dir_list.append((node_de, node_de._element, node_de.dir_size))
            if not node_de._first_child:
                continue
            node_de = node_de._first_child
            de.append(node_de)
            while node_de._right_sibling is not None:
                de.append(node_de._right_sibling)
                node_de = node_de._right_sibling

        return dir_list

    def tree_calc3(self):
        node = self._root

    def sum_size(self, q_files):
        ans_dict = {}
        dir_set = set()
        for item in q_files:
            print(item)
            l = [x for x in item[1]]
            for name in l:
                if name != "/":
                    dir_set.add(name)

        for name in dir_set:
            print(name)
            t = 0
            for item in q_files:
                if name in item[1]:
                    t += int(item[0][0])
                    print(f'T: {t}')
            ans_dict[name] = t

        res = 0
        for item, val in ans_dict.items():
            print(item, val)


if __name__ == "__main__":
    T = TreeMake()
    T.treemake(fname)
    dir_list = T.treecalc2()
    res = 0
    for node, name, val in dir_list:
        print(T.add_dir_sizes(node), name, val)
        res += val

    print(res)


    #1118405
    #12545514





    # NRoot = T._rootbegin("Root")
    # NA1 = T._add_first_child(p=NRoot, e="1a")
    # NA2 = T._add_right_sibling(NA1, "2a")
    # NA3 = T._add_right_sibling(NA2, "3a")
    # NB1 = T._add_first_child(T._atfirst_child(NRoot), "1ab")
    # NB2 = T._add_right_sibling(NB1, "2ab")
    # NB3 = T._add_right_sibling(NB2, "3ab")
    # NB3ab1 = T._add_first_child(NB3, "3ab1")
    # NB3ab2 = T._add_right_sibling(NB3ab1, "3ab2")
    # NB3ab3 = T._add_right_sibling(NB3ab2, "3ab3")
    # N3a1 = T._add_first_child(NA3, "3a1")
    # N3a2 = T._add_right_sibling(N3a1, "3a2")
    # N3a2a = T._add_first_child(N3a2, "3a2a")
    # N3a2b = T._add_right_sibling(N3a2a, "3a2b")
    # N3a2a1 = T._add_first_child(N3a2a, "3a2a1")
    # AB1 = T._add_right_sibling(T._at_parent(NB3), "AB1")

    # T.treeprint()
    #
    # def pos_printer(p):
    #     node = T._validate(p)
    #     print(node._element)
    #
    # tl = ["2a", "3a", "3ab1", "3ab2", "3a2a1"]
    # for x in tl:
    #     pos_printer(T._file_search(x))

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















