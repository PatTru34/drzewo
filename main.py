from typing import Any, List, Callable, Union


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any, children: List):
        self.value = value
        self.children = children

    def is_leaf(self) -> bool:
        if (self.children == None):
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def __str__(self) -> str:
        wynik = self.value
        return wynik

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        list = self.children
        while list.__len__() != 0:
            visit(list[0])
            list = list + (list[0].children)
            del list[0]
    # def search(self,value: Any) -> Union['TreeNode', None]:


class Tree:
    root: TreeNode

    def __init__(self, root):
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        TreeNode.add(value, parent_name)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)


def fun(x):
    print(x)


F = TreeNode("F", children=[])
tree = Tree(F)

B = TreeNode("B", children=[])
F.add(B)

A = TreeNode("A", children=[])
B.add(A)

D = TreeNode("D", children=[])
B.add(D)

C = TreeNode("C", children=[])
D.add(C)

E = TreeNode("E", children=[])
D.add(E)

G = TreeNode("G", children=[])
F.add(G)

I = TreeNode("I", children=[])
G.add(I)

H = TreeNode("H", children=[])
I.add(H)

# F.for_each_deep_first(fun)
# F.for_each_level_order(fun)
# tree.for_each_deep_first(fun)
# tree.for_each_level_order(fun)
